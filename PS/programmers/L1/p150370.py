"""
Solving Date    : 2023.12.17
Solving Time    : 20m
Title           : 개인정보 수집 유효기간
tags            : string
url             : https://school.programmers.co.kr/learn/courses/30/lessons/150370
runtime         : -
memory          : -
"""

def solution(today, terms, privacies):
    results = []
    today_i = int("".join(today.split(".")))

    terms_dict = {t: int(m) for t, m in map(str.split, terms)}

    for i, p in enumerate(privacies):
        date, term = p.split()

        y, m, d = map(int, date.split("."))
        m += terms_dict[term] - 1
        y = y + m // 12
        m = m % 12 + 1

        if y * 10000 + m * 100 + d <= today_i:
            results.append(i + 1)

    return results

"""
2023 KAKAO BLIND RECRUITMENT > 개인정보 수집 유효기간

n개의 개인정보에 각 약관만큼 달 수를 더해서
오늘 날짜 이전인지 파악하는 문제.
 
기한이 한달 기준으로 되기 때문에
1일에 수집했으면, 한달 뒤에 저장가능한 날짜는 말일이다.
- 파기 일자가 오늘 일(day)을 포함 한 이전 날짜면 파기한다.

- 12월을 처리 안해서 에러가 다소 났다.
"""