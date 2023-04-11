# 중위수식 문자열 넣어서, 중위/후위 문자열 반환 또는 계산결과 
class stack_calc:

	# 초기화 시 입력된 수식으로 각 표기법, 결과를 바로 저장
	def __init__(self, expr_infix_str="0": str):
		self.expr_infix_tokens = self.split_tokens(expr_infix_str)
		self.expr_postfix_tokens = self.infix_to_postfix(self.expr_infix_tokens)
		self.ans = self.evaluate_postfix(self.expr_postfix_tokens)

	# 문자열로 된 중위표기법 수식 리턴
	def get_expr_infix_str(self, sep="": str) -> str:
		return self.tokens_to_str(self.expr_infix_tokens, sep)

	# 문자열로 된 후위표기법 수식 리턴
	def get_expr_postfix_str(self, sep="": str) -> str:
		return self.tokens_to_str(self.expr_postfix_tokens, sep)

	# 계산 결과 리턴 (정수인지 유리수인진 몰루?)
	def get_result(self) -> (int,float):
		return self.ans

	# 토큰화되어 리스트로 저장된 내용을 합쳐서 문자열로 리턴
	def tokens_to_str(self, tokens: list, sep: str) -> str:
		result_str = ""
		f = False
		for token in tokens:
			if f:
				result_str += sep
			if type(token) in (int, float):
				result_str += str(token)
			else:
				result_str += token
			f = True
		return result_str

	# 문자열을 연산자, 피연산자 나눠서 리스트로 저장하여 리스트를 리턴
	def split_tokens(self, expr_str: str) -> list:
		tokens = []
		val = 0
		val_processing = False
		for ch in expr_str:
			if ch==" ":
				continue
			elif ch in "0123456789":
				val = val*10 + int(ch)
				val_processing = True
			else:
				if val_processing:
					tokens.append(val)
					val = 0
				val_processing = False
				tokens.append(ch)
		if val_processing:
			tokens.append(val)

		return tokens

	# 토큰화된 중위표기법을 토큰화된 후위표기법으로 변환/리턴
	def infix_to_postfix(self, infix_expr_tokens: list) -> list:
		preced = {
			"*":5, "/":5,
			"+":3, "-":3,
			"(":1,
		}
		s = []
		postfix_expr_tokens = []
		for ch in infix_expr_tokens:
			if type(ch) in (int, float):
				postfix_expr_tokens.append(ch)
			elif ch in "+-*/":
				while s and preced[s[-1]]>=preced[ch]:
					postfix_expr_tokens.append(s.pop())
				s.append(ch)
			elif ch == "(":
				s.append(ch)
			elif ch == ")":
				while s and s[-1]!="(":
					postfix_expr_tokens.append(s.pop())
				s.pop()

		while s:
			postfix_expr_tokens.append(s.pop())

		return postfix_expr_tokens

	# 토큰화된 후위표기법을 계산하여 결과값 리턴
	def evaluate_postfix(self, postfix_expr_tokens: list) -> (int, float):
		s = []

		for ch in postfix_expr_tokens:
			if type(ch) in (int, float):
				s.append(ch)
			elif ch in "+-*/":
				b = s.pop()
				a = s.pop()
				if ch == "+":
					s.append(a+b)
				elif ch == "-":
					s.append(a-b)
				elif ch == "*":
					s.append(a*b)
				elif ch == "/":
					s.append(a/b)

		return s[0]


expr = [
	"1 + 2 * 3",
	"3 + 4 * 2 - 1 / 1",
	"4 * 3 + 2",
	"4 * ( 3 + 2 )",
	"( 1 + 2 ) * ( 3 + 4 )",
	"2 + 6 * 4 / ( 5 * 3 - 7 ) + 8",
]
correct = [
	7,
	10,
	14,
	20,
	21,
	13,
]

if __name__ == "__main__":
	l = max(map(lambda x:len(x),expr))
	for expr_str, corr_ans in zip(expr, correct):
		sc = stack_calc(expr_str)
		print(sc.get_expr_infix_str(),"=>",
			  sc.get_expr_postfix_str(),"=>",
			  sc.get_result(),
			  sc.get_result() == corr_ans)
