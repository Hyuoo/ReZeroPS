'''
https://school.programmers.co.kr/learn/courses/30/lessons/42577
문제 분류가 "해시"인 전화번호 목록 문제.

보자마자 Trie를 떠올렸는데 그정도를 요하는 문제는 아닐 것 같아서
정렬해놓고 그냥 뒷녀석이 더 긴 배열일테니까 뒷녀석과 비교하는 방식으로 풀었다.

처음 아래와같은 코드를 만들어냈다가 효율성 문제(효율성2/4정답)로 실패
def solution(phone_book):
    phone_book.sort()
    for i, a in enumerate(phone_book):
        for j in range(i+1,len(phone_book)):
            if a[0]!=phone_book[j][0]:
                break
            if a==phone_book[j][:len(a)]:
                return False
    return True
생각해보니 정렬된거라 가장 유사한게 i+1일텐데
i+1도 아닌데 i->j비교를 위해 멀리까지 갈 필요가 없다.
그래서 아래처럼 그냥 다음거만 같은지 보는 코드로 만들었더니 됐다.
'''
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True
