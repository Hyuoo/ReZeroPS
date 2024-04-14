"""
Solving Date    : 2024.03.21
Solving Time    : 39m
Title           : HTML 파싱
tags            : 구현, 문자열, 파싱, 정규 표현식
url             : https://www.acmicpc.net/problem/22859
runtime         : 100 ms
memory          : 32560 KB
"""

import sys

def transform_paragraph(text):
    buf = ""
    i = 0
    while i < len(text):
        if text[i] == "<":
            i = text.find(">", i) + 1
            continue
        buf += text[i]
        i += 1
    buf = buf.strip()
    buf = " ".join(buf.split())
    return buf

def substitution_paragraph(text):
    # substitution "<p>~</p>" to "#" from HTML
    paras = []
    ret = ""
    i = 0
    while i < len(text):
        if text[i:i+3] == "<p>":
            s = i + 3
            e = text.find("</p>", i)
            paras.append(transform_paragraph(text[s:e]))
            i = e + 4
            ret += "#"
            continue
        ret += text[i]
        i += 1
    
    return (ret, iter(paras))

def extract_div(text):
    div = []
    i = 0
    while i < len(text):
        if text[i:i+4] == "<div":
            e = text.find("</div>", i)
            div.append(text[i:e])
            i = e + 5
            continue
        i += 1
    return div

def get_div_title(text):
    s = text.find('title="')+7
    e = text.find('"', s)
    return text[s:e]


if __name__ == "__main__":
    text = sys.stdin.readline()
    stdout = ""

    text, paragraph_iter = substitution_paragraph(text)

    for div in extract_div(text):
        title = get_div_title(div)
        stdout += f"title : {title}\n"
        for _ in range(div.count("#")):
            stdout += next(paragraph_iter) + "\n"
    
    sys.stdout.write(stdout)


"""
100ms까지밖에 안나오넹

방법 1.
div 파싱 후, p 파싱하여 p.text를 처리하기

방법 2.
p를 모두 치환 및 처리 한 뒤, div 파싱하여 치환된 p.text출력하기


방법 1로 처음 했다가 질문 게시판을 보고
<diving>같은 페이크 태그가 있을 경우도 있다고 해서
엄격한 처리를 하기보다

입력 자체가 p태그 사이에만 다른 태그가 오기 때문에
이를 간소화시켜서 처리하는 방법 2로 다시 풀이 함.

===
방법1에서 처리할 땐
어차피 여는 태그는 예외사항 없으니, 닫는 태그만 ">"를 붙여서 검사하여 통과

===
방법1에서 하위태그를 추출하는 공통 함수를 만들어서 코드 자체는 더 짧음
방법2는 입력에 대한 예외가 발생하기 힘듦.
"""