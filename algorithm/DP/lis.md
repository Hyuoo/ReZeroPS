
> [[ 참고 블로그 | 알고리즘 - 최장 증가 부분 수열(LIS) 알고리즘 ]](https://chanhuiseok.github.io/posts/algo-49/)

## 최장 증가 부분 수열
(LIS; Longest Increasing Subsequence)

특정 수열에서 일부 원소만으로 만든 부분 수열에서
모든 숫자가 증가하는 수열
중에 그 길이가 가장 긴 부분 수열의 길이를 찾는 알고리즘

`[6, 2, 5, 1, 7, 4, 8, 3]` 이란 배열이 있을 경우
최장 증가 부분 수열은 `[2, 5, 7, 8]` 이 된다.

이를 계산하는 방식으로는   
- DP배열을 이용해서 2중 반복문으로 푸는 `O(n^2)`
- 이분탐색을 활용한 `O(nlogn)`

***

### DP를 이용해서 2중반복

`dp[i]`는 i번째 인덱스에서 끝나는 최장 증가 부분 수열의 길이이다.

```python
ar = [6, 2, 5, 1, 7, 4, 8, 3]
n = len(ar)
dp = [1 for _ in range(n)]
for k in range(n):
    for i in range(k):
        if ar[i] < ar[k]:
            dp[k] = max(dp[k], dp[i]+1)
# answer: max(dp)
```
(블로그에 나온 방법은 이 방법이지만,
아래 방법도 동일하게 풀린다.)

인덱스를 한칸씩 증가시키면서 해당 칸까지의(k) 최장 길이(DP) 값을 계산한다.

각 dp[k]는 k미만의 인덱스(i)를 반복하여   
만약, 길이 갱신이 가능하다면(값이 증가) `(ar[i] < ar[k])`

- dp[i]까지 계산 한 값에서 1 증가 한 값
- 현재 dp[k]의 값

둘 중에서 큰 값으로 `dp[k]`를 갱신한다

<br>

```python
ar = [6, 2, 5, 1, 7, 4, 8, 3]
n = len(ar)
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        if ar[i] < ar[j]:
            dp[j] = max(dp[j], dp[i]+1)
# answer: max(dp)
```
위와는 접근순서가 다른 방식.

인덱스를 한 칸씩 증가시키면서
해당 칸(i) 이후에 있는 더 큰 값들(증가된)에 +1을 시켜준다.

마찬가지로, 갱신이 가능하면 `(ar[i] < ar[j])`
- dp[i]까지 계산 한 값에서 1 증가 한 값
- 현재 dp[j]의 값

둘 중에 큰 값으로 `dp[j]`를 갱신한다.

<br>

#### 숏코딩..
```python
ar = [6, 2, 5, 1, 7, 4, 8, 3]
dp = [0 for _ in range(max(ar)+1)]
for i in ar:
    dp[i] = max(dp[:i])+1
# answer: max(dp)
```
이 방법으로 풀려면 원소가 되는 값범위를
넣을 수 있는 배열이 필요함.

원리는 동일하게
- 앞서 나온 작은 숫자들 중
    - 가장 긴 길이 +1

로 dp를 갱신하는 방법.

***

### 이분탐색을 이용한 풀이

```python
import bisect

ar = [6, 2, 5, 1, 7, 4, 8, 3]
lis = [ar[0]]
for i in ar[1:]:
    if lis[-1] < i:
        lis.append(i)
    else:
        d = bisect.bisect_left(lis, i)
        lis[d] = i
# answer: len(lis)
```
이분탐색을 이용해서
앞서 나온 숫자들 사이에서
최장길이를 갱신하는 방법.

(*lis 배열에 LIS 수열 자체를 저장하 는 건 아님.)

- 같은 길이면 작은 숫자가 더 큰 증가수열을 만들 수 있다.

해서 계속 갱신하고, 계속해서 수열 전체가 바뀌면서
새로운 숫자가 최장길이를 갱신하게 되면
lis배열의 길이를 하나 늘리게 된다.

좀 쉽게 설명하면
- 최장 부분 수열을 만들면서
  다른 가능 한 최선이 있을 경우
  수열을 덮어쓰기 하면서
  길이가 더 길면 자연스럽게 "길게 덮어쓰기"
  되는 알고리즘.


***

### 관련 문제

- [[G5] 전깃줄](https://www.acmicpc.net/problem/2565) [[풀이 코드](/PS/baekjoon_online_judge/gold/5/BOJ%202565.py)]
- [[G2] 반도체 설계](https://acmicpc.net/problem/2352) [[풀이 코드](PS/baekjoon_online_judge/gold/2/BOJ%202352.py)]