"""
open()
파일 오픈.

백준에서 사용 시 open(0) 이런식으로 input()대신 사용한다.
# 0: stdin, 1: stdout, 2: stderr

# 2줄 입력이 주어 질 때 아래처럼 하면 줄단위로 언패킹된다.
a, b = open(0)

# 2줄 이상에서 b에 나머지 몰빵.
a, *b = open(0)

# 다중으로 들어오는 입력이 '\n'을 포함하여 문자열로 들어온다.
a = open(0).read()

#
a = open(0).readline()

# '\n'단위로 언패킹. '\n'를 포함한 리스트로 변환 -> lines
[*open(0)]

"""