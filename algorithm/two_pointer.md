## two_pointer (투 포인터)

#### 인덱스 두개를 가지고 푸는 문제. 유동적인 범위 탐색에서 사용된다.

포인터라는 말에 쪼는 사람들이 있는데, 말이 포인터지.   
그냥 인덱스 값 2개면, 데이터를 가리키는 포인터 2개. 투 포인터.

- 문제에 따라서 포인터가 움직이는 전략과 방향 등이 달라진다.
    - 배열의 왼쪽과 오른쪽에서 시작해서 서로 좁혀오는 경우
    - 배열의 같은 위치(`[0]`)에서 시작해서 진행 속도가 다른 경우

이런 방식의 차이에 따라서 직관적인 포인터 이름을 선언하도록 한다.   
ex) `i, j`, `left, right`, `start, end`

<br>

> <i>.. 근데 투포인터가 이분탐색이랑
> 굉장히 비슷한 모양새가 되는 문제가 많은 것 같다.</i>
> - <i>인덱스 2개 잡혀있고</i>
> - <i>인덱스 기준으로 탐색하고 (대소비교)</i>
> - <i>비교에 따라 인덱스 위치 조정하고</i>

---

> 종종 <b>슬라이딩 윈도우<i>(Sliding Window)</i></b>랑 분류가 같이 나오는 경우가 있는데, 
> 슬라이딩 윈도우는 간격이 <u><b>고정</b></u>되어 이동하는 경우라 
> 엄밀히 따지면 다르다.   
> 고정간격이기 때문에 슬라이딩 윈도우는 인덱스 하나만 있어도 풀리는 경우가 많다.

---

### 관련 문제

- [S4 | 수들의 합 2](https://www.acmicpc.net/problem/2003) [[풀이 코드](/baekjoon_online_judge/200_silver/4_300/BOJ%202003.py)]
- [S3 | 두 수의 합](https://www.acmicpc.net/problem/3273)
- [G5 | 두 용액](https://www.acmicpc.net/problem/2470)