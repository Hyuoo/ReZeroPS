#https://school.programmers.co.kr/learn/courses/30/lessons/60057

def f(n):
    c=0
    while n:
        n//=10
        c+=1
    return c

def solution(s):
    ans = len(s)
    for i in range(1,len(s)//2+1):
        count = 0
        zip_count = 1
        word = [s[j:j+i] for j in range(0,len(s),i)]+[""]
        
        for j in range(len(word)-1):
            if word[j]==word[j+1]:
                zip_count+=1
            else:
                if zip_count>1:
                    count += f(zip_count)
                count += len(word[j])
                zip_count = 1
        
        # print(word, count)
        if ans>count:
            ans = count
    return ans
'''
문자열 압축
풀이시간 : 약 30분?
#KDT_코테스터디

옛날에 푼 이력이 있는 문제긴한데 몰루?

문자열 절반길이 이상으로 압축하면 절대 효율나올수없기에
압축길이 len(s)//+1까지만 고려

압축길이 i(1~len(s)//2+1)로 반복하면서:
  word에 i로 단위로 문자열 다 잘라서 저장
    # 후처리 없애고 일반화시키기 위해 끝에 [""]추가
  다음 문자열과비교하여 같으면 압축
  다르면 길이 그대로
반복
'''
