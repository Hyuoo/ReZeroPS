"""
# KMP
- (Knuth, Morris, Prett) 세 명이서 만든 알고리즘.

문자열에서 패턴이 일치하는 인덱스를 **모두** 찾는 알고리즘.
근데, 매우 빠르게 O(N+M) 시간에 문자열 검색을 할 수 있다.
(N: 텍스트의 길이, M: 패턴의 길이)
단순/무식하게 완전탐색으로 검색하는 방법은 O(NM)

접두사(prefix) 접미사(suffix)를 활용하여 풀이.

=====
### pi배열
pi[i] == i인덱스까지
prefix == suffix가 될 수 있는 부분 문자열 중
가장 긴 것의 길이.
(단, prefix != i까지 부분문자열)

[출처: https://bowbowbow.tistory.com/6]
"""
# pi.
# string p의 길이 i인 서브스트링에서 가장 긴 prefix==suffix 길이 리스트로 반환.
def getpi(p:str)->list:
    m = len(p)
    j = 0
    pi = [0 for _ in range(m)]
    for i in range(1,m):
        while j>0 and p[i]!=p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi

# kmp.
# string s에서 pattern p 등장 위치 인덱스 리스트로 반환.
def kmp(s:str, p:str)->list:
    ans:int = []
    pi = getpi(p)
    n = len(s)
    m = len(p)
    j = 0
    for i in range(0,n):
        while j>0 and s[i]!=p[j]:
            j = pi[j-1]
        if s[i]==p[j]:
            if j==m-1:
                ans.append(i-m+1)
                j = pi[j]
            else:
                j+=1
    return ans

if __name__ == "__main__":
    text = "ABCABABCDEFAAABC"
    pattern = "ABC"
    p_l = len(pattern)
    k=kmp(text, pattern)

    tmp = [" "]*len(text)
    for i in k:
        tmp[i] = "*"
    print(text)
    print("".join(tmp))

    print("search count:", len(k))
    print("search indexes:", k)

    if "getpi examples" and 0:
        s = ["ABCDABCDABEED",
             "ABCABCACC",
             "ABCDCBA",
             "ABCDABCD",
             "ABABABABA",
             "ABABABABAB",
             "ABABCABCABD",
             "ABCAABCABCABC"]
        print("\ngetpi examples:")
        for i in s:
            print(*i)
            print(*getpi(i))
            print(kmp(i, "ABC"))
            print("-"*40)