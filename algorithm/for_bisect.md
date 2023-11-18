
아니 바이섹트 왤케 빠름???


[10815 숫자 카드](https://www.acmicpc.net/problem/10815)
문제가 이진탐색으로 풀면 실행시간이 오래 걸리길래

bisect라이브러리 사용과 직접 똑같이 구현한걸 제출 해 봄

구현내용은 [cpython bisect.py](https://github.com/python/cpython/blob/3.7/Lib/bisect.py)
동일하게 bisect_left를 사용해서 풀이.

#### bisect 라이브러리 (114472KB, 936ms)
```python
import bisect

n,a,m,b=open(0)
n = int(n)
a = sorted([*map(int, a.split())])
b = [*map(int, b.split())]

ret = []
for x in b:
    r = bisect.bisect_left(a, x)
    if r < n and a[r]==x:
        ret.append(1)
    else:
        ret.append(0)
print(*ret)

```


#### 직접 동일하게 구현 (112404KB, 1696ms)
```python
def bisect_left(a, x, lo=0, hi=None):
    if lo<0:
        return -1
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: lo = mid+1
        else: hi = mid
    return lo

n,a,m,b=open(0)
n = int(n)
a = sorted([*map(int, a.split())])
b = [*map(int, b.split())]

ret = []
for x in b:
    r = bisect_left(a, x)
    if r < n and a[r]==x:
        ret.append(1)
    else:
        ret.append(0)
print(*ret)
```
