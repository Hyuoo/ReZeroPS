k=[1 for _ in range(26)]
kval=lambda x:((ord(x)|32)-97)

for _ in range(int(input())):
    str=input()
    # print(str)

    idxs = [0]
    tmp = 0
    while str.find(" ",tmp)!=-1:
        tmp = str.find(" ",tmp)+1
        idxs.append(tmp)

    idxs.extend(range(len(str)))
    next_idx = iter(idxs)
    # print(idxs)

    for i in next_idx:
        if str[i]==" ":
            continue
        if k[kval(str[i])]:
            k[kval(str[i])] = 0
            new_str = ""
            for j in range(len(str)):
                if j==i:
                    new_str += f"[{str[j]}]"
                else:
                    new_str += str[j]
            print(new_str)
            break
    else:
        print(str)

'''
단축키 지정
풀이시간 : 31m
#KDT_코테스터디

문자열에서
일정 규칙으로
단축키가 될 수 있는 단어 찾고
변환해서 출력하기

문제 지시사항대로 구현하면 되는 문제.
근데 순서가 좀 섞여있어서
단축키로 지정될 문자를 매번 찾으면 코드가 더러워 질 것 같아서
옵션별로 시퀀스를 생성한 뒤 시퀀스 순서대로 검사한다.

시퀀스는 문자 위치를 알아야하기때문에 인덱스로.

풀이:
1. 시퀀스 생성.
  1.1. 단어 단위로
  1.2. 0부터 끝까지
2. 두개 합쳐서 iter로 만들어서 검사+변환
  2.1. 공백문자 스킵
  2.2. 단축키에 사용 안된 알파벳이라면
    - 해당 인덱스만 대괄호로 감싸서 새로운 단어 생성
- iter에서 성립하는게 하나도 없으면 문자 그대로 출력 (단축키없음)
'''
