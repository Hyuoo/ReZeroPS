def get_avg(arr):
	m = arr[0]
	lp, rp = 0, 0
	M = 0
	ret = m
	while m<=arr[-1]:
		while lp<n and arr[lp]<m-2:
			lp+=1
		while rp<n and arr[rp]<=m+2:
			rp+=1
		if M<rp-lp:
			M = rp-lp
			ret = m
		m+=1
	return ret

n = int(input())
a = get_avg(sorted(map(int,input().split())))
b = get_avg(sorted(map(int,input().split())))

print(a,b)
print("good" if a > b else "bad")

'''
https://level.goorm.io/exam/49101/%ED%99%98%EA%B2%BD%EA%B3%BC-%EC%A5%90-%ED%81%AC%EA%B8%B0%EC%9D%98-%EC%83%81%EA%B4%80%EA%B4%80%EA%B3%84/quiz/1
환경과 쥐 크기의 상관관계
풀이시간 : 안쟀는데 한 20~30분 정도?

범위안에 값들을 세려면..
한 10초정도 누적합이 떠오르다가
밑에값 위에값 틀 잡으면 한번 돌면 되겠다 해서 인덱스 두개 잡고 시작
그리고 인덱스위치로 갯수 확인 후 최댓값만 갱신
'''
