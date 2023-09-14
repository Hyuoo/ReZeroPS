from collections import defaultdict
import sys
input = sys.stdin.readline

child_rooms = defaultdict(set)
output = ""

def print_rooms(now_hash, depth):
    global output
    for next in sorted(child_rooms[now_hash]):
        # print("--"*depth, next, sep="")
        output+="--"*depth+next+"\n"
        print_rooms((now_hash<<2) + hash(next), depth+1)

for _ in range(int(input())):
    _, *rooms = input().split()
    now_hash = 0

    for room in rooms:
      # if room not in child_rooms[now_hash]:  # 얘는 있든없든 별 차이 없다.
      child_rooms[now_hash].add(room)
      now_hash = (now_hash<<2) + hash(room)

print_rooms(0, 0)
print(output)

"""
14725 개미굴
풀이시간 : 30m

딱봐도 트라이 문제
하지만 난 트라이같은거 구현뚝딱 몰라 걍 딕셔너리 쓰면 편할듯?
딕셔너리 여러개 생기는것도 싫은데
해시값 겹쳐서 딕셔너리 하나로 퉁치자

문제점:
- hash + next_val 이런식으로 해버려서 A-B와 B-A가 같아서 비트연산<<2해버림
"""
