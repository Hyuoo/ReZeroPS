"""
Solving Date    : 2023.11.27
Solving Time    : 6m
Title           : 잘못된 버블정렬
tags            : 애드 혹, 해 구성하기
url             : https://www.acmicpc.net/problem/30010
runtime         : 44 ms
memory          : 31120 KB
"""

print(*([1]+[0]*(int(input())-1)))

"""
제 1회 선린 프로그래밍 챌린지 Open Contest

버블정렬 특성을 이해하면 쉽게 풀리는 문제

주어진 코드의 경우
가장 오른쪽 쌍은 1번만 비교가 되므로
최댓값이 가장 오른쪽 또는 오른쪽에서 두번째가 아닐 경우
정렬이 되지 않는다.
"""