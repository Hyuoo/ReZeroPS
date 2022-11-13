'''
문자열 a, b 무한반복해서 똑같은지 yes, no 출력
- a, b가 똑같으려면 시작부터 똑같아야함
- 각 반복되는 문자열 찾아서 똑같으면 yes
나는 그냥 긴 문자열 갯수만큼 짧은 문자열 내용 똑같이 반복되는지 체크만 했다.
aaabaaa, aaab같은 경우가 나올 수 있어서
순회 이후에도 짧은게 한바퀴 돌동안 일치하는지 min(~)을 추가해줬다.
'''
T = int(input())
for test_case in range(1, T + 1):
    a,b = input().split()
    flag = True
    for i in range(max(len(a),len(b))+min(len(a),len(b))):
        if a[i%len(a)] != b[i%len(b)]:
            flag = False
            break
    print("#{} {}".format(test_case, "yes" if flag else "no"))
