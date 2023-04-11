#띄어쓰기로 구분된 중위수식 -> 후위수식 변환 리스트 반환
def infix_to_postfix(infix):
	preced = {
    "*":5, "/":5,
    "+":3, "-":3,
    "(":1,
  }
	s = []
	postfix = []
	for ch in infix.split():
		if ch in "+-*/":
			while s and preced[s[-1]]>=preced[ch]:
				postfix.append(s.pop())
			s.append(ch)
		elif ch == "(":
			s.append(ch)
		elif ch == ")":
			while s and s[-1]!="(":
				postfix.append(s.pop())
			s.pop()
		else:
			postfix.append(ch)

	while s:
		postfix.append(s.pop())
  
	return postfix


exp = [
	"1 + 2 * 3",
	"3 + 4 * 2 - 1 / 1",
	"4 * 3 + 2",
	"4 * ( 3 + 2 )",
	"( 1 + 2 ) * ( 3 + 4 )"
  "2 + 3 * 4 / ( 5 * 6 - 7 ) + 8"
]
correct = [
  7,
  10,
  14,
  20,
  21,
]

l = max(map(lambda x:len(x),exp))
for i in exp:
  #print(f"{i.replace(' ',''):>12} => {''.join(infix_to_postfix(i))}")
  print("{:>12} => {}".format(i.replace(" ",""), "".join(infix_to_postfix(i))))
