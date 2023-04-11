#중위수식 문자열 넣어서, 중위/후위 문자열 반환 또는 계산결과 
class stack_calc:

	def __init__(self, expr_infix_str="0"):
		self.expr_infix_tokens = self.split_tokens(expr_infix_str)
		self.expr_postfix_tokens = self.infix_to_postfix(self.expr_infix_tokens)
		self.ans = self.evaluate_postfix(self.expr_postfix_tokens)

	def get_expr_infix_str(self, sep=""):
		return self.tokens_to_str(self.expr_infix_tokens, sep)

	def get_expr_postfix_str(self, sep=""):
		return self.tokens_to_str(self.expr_postfix_tokens, sep)

	def get_result(self):
		return self.ans

	def tokens_to_str(self, tokens, sep):
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

	def split_tokens(self, expr_str):
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

	def infix_to_postfix(self, infix_expr_tokens):
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

	def evaluate_postfix(self, postfix_expr_tokens):
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
