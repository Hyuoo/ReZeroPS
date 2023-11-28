"""
LCS (Longest Common Subsequence)
최장 공통 부분 수열
    혹은, 최장 공통 문자열 (Longest Common Substring)
"""

"""
+ LCS의 길이만 구하는 알고리즘
+ 계산 한 LCS_DP를 기반으로 LCS자체를 찾는 알고리즘
+ 모든 LCS를 구하는 알고리즘

a, b 문자열의 길이를 각각 n, m이라고 할 때
시간복잡도는 O(n*m),
공간복잡도는 O(n*m)에서 줄이면 O(min(n*m))까지

참고:
https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence
https://www.techiedelight.com/ko/longest-common-subsequence-finding-lcs/
https://ko.wikipedia.org/wiki/%EC%B5%9C%EC%9E%A5_%EA%B3%B5%ED%86%B5_%EB%B6%80%EB%B6%84_%EC%88%98%EC%97%B4
"""
ln = lambda:print("-"*60)


"""
먼저, 최장 공통 문자열을 찾는 방법. (부분 X)

양 문자열을 비교하면서 같은 문자가 있을 경우 +1 해주는 방식.

2차원으로 보면, 연속으로 일치하는 부분만 1 2 3 식으로 늘어난다.
"""
def get_longest_common_substring(a, b):
    # 최장 공통 문자열 DP배열 구하기
    # time:O(m*n), memory:O(n*m)
    n, m = len(a), len(b)
    lcs = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1

    return lcs


"""
최장 공통 부분 수열을 계산한 2차원 배열 구하기

문자열을 비교해서 같으면 연속문자열과 동일하게 +1

*부분*이기 때문에 연속되지 않아도 되어서
문자열이 같지 않더라도 max((x-1, y), (x, y-1))로 갱신을 해준다. 
"""
def get_longest_common_subsequence(a, b):
    # 최장 공통 부분 수열 DP배열 구하기
    # time:O(n*m), memory:O(n*m)
    n, m = len(a), len(b)
    lcs = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    return lcs


def get_lcs_length_bottom_up(a, b):
    # LCS의 길이값 구하기
    # 길이만필요, 공간 최적화, 상향식
    # 길이만 필요로 할 경우 모든 배열을 생성 할 필요가 없음.
    # time:O(n*m), memory:O(min(n, m))
    if len(a) < len(b): a, b = b, a

    n, m = len(a), len(b)
    dp = [0 for _ in range(m+1)]

    # 처음 dp를 다 0으로 초기화 했기 때문에 i는 0부터 시작해도 되지만,
    # 이해를 쉽게 하기 위해서 j인덱스와 맞춰줌
    for i in range(n+1):
        p = 0
        for j in range(1, m+1):
            t = dp[j]
            if a[i-1] == b[j-1]:
                dp[j] = p+1
            else:
                dp[j] = max(dp[j], dp[j-1])
            p = t

    return dp[-1]


def get_lcs_length_top_down(a, b):
    # LCS의 길이값 구하기
    # 길이만필요, 공간 최적화, 하향식
    # time:O(n*m), memory:O(n*m)

    # 재귀를 사용해서 공통 부분 수열 경로를 탐색한다.
    def lcs_length(x, y):
        if x==0 or y==0:
            return 0

        key = (x, y)

        if key not in memoi:
            if a[x-1] == b[y-1]:
                memoi[key] = lcs_length(x-1, y-1) + 1
            else:
                memoi[key] = max(lcs_length(x-1, y), lcs_length(x, y-1))

        return memoi[key]

    # 메모를 안하면 호출이 O(2^(n+m))
    memoi = dict()

    return lcs_length(len(a), len(b))


"""
lcs를 계산 한 2차원 배열을 기반으로
역으로 최장부분공통문자열(LCS)를 계산하는 방법.
(하나의 LCS)

- 일치하지 않을 경우 max(위, 왼쪽)
- 일치 할 경우에만 대각선+1
로 계산 한 점을 이용한다.

- 위, 왼쪽 중 현재 값과 같은 값이 있다면 그냥 이동.
- 없다면 대각선으로 이동, 해당위치 문자열 추가.
"""
def search_lcs_sequence(a, b):
    # LCS 수열 구하기
    lcs = get_longest_common_subsequence(a, b)
    x, y = len(a), len(b)

    ret = ""
    # 구현 1
    # 위 설명에 충실한 구현 방법.
    # while x!=0 and y!=0:
    #     if lcs[x][y] == lcs[x-1][y]:
    #         x, y = x-1, y
    #     elif lcs[x][y] == lcs[x][y-1]:
    #         x, y = x, y-1
    #     else:
    #         # lcs[x][y]-1 == lcs[x-1][y-1]
    #         ret += a[x-1]
    #         x -= 1
    #         y -= 1

    # 구현 2
    # 구현 2의 경우엔
    # 어차피 a, b의 위치가 같으면 +1이 되었기 때문에 이를 이용함.
    # 그렇지 않을 경우 (위, 왼쪽) 중 큰 곳으로 이동.
    while x!=0 and y!=0:
        if a[x-1] == b[y-1]:
            ret += a[x-1]
            x, y = x-1, y-1
        else:
            if lcs[x-1][y] > lcs[x][y-1]:
                x, y = x-1, y
            else:
                x, y = x, y-1

    return ret[::-1]


"""
모든 lcs를 구하는 방법.

문자열이 같은 경우 외에,
(위, 왼쪽)이 같은 경우 한쪽만 이동하는데
모든 방향으로 이동하면서 모든 lcs를 계산 함.
"""
def search_lcs_sequence_all(a, b):
    # 모든 LCS 수열 구하기
    def get_all_lcs(x, y):
        if x == 0 or y == 0:
            return [""]

        ret = []
        if a[x - 1] == b[y - 1]:
            tmp = get_all_lcs(x - 1, y - 1)
            for i in range(len(tmp)):
                tmp[i] += a[x - 1]
            return tmp

        if lcs[x][y] == lcs[x - 1][y]:
            ret.extend(get_all_lcs(x - 1, y))
        if lcs[x][y] == lcs[x][y - 1]:
            ret.extend(get_all_lcs(x, y - 1))

        return ret

    lcs = get_longest_common_subsequence(a, b)
    x, y = len(a), len(b)
    all_lcs = get_all_lcs(x, y)
    # print(all_lcs)

    return list(set(all_lcs))




if __name__ == "__main__":
    # 현재 문자열로만 해 놓음.
    str_set = [
        ("bbcdef", "abcefg"),
        ("XMJYAUZ", "MZJAWXU"),
        ("ABCBDAB", "BDCABA")
        ][2]
    print(*str_set)

    t = get_longest_common_substring(*str_set)
    for i in t:
        print(i)

    ln()

    t = get_longest_common_subsequence(*str_set)
    for i in t:
        print(i)

    ln()

    t = search_lcs_sequence(*str_set)
    print(t)

    ln()

    print(search_lcs_sequence_all(*str_set))

    ln()

    print(get_lcs_length_bottom_up(*str_set))
    print(get_lcs_length_top_down(*str_set))
