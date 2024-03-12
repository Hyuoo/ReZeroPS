/*
Solving Date    : 2024.03.04
Title           : 연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기
tags            : GROUP BY
url             : https://school.programmers.co.kr/learn/courses/30/lessons/284528
*/

WITH bonus_table AS (
    SELECT
        emp_no,
        CASE
            WHEN score>=96 then 'S'
            WHEN score>=90 then 'A'
            WHEN score>=80 then 'B'
            ELSE 'C'
        END as grade,
        CASE
            WHEN score>=96 then 0.2
            WHEN score>=90 then 0.15
            WHEN score>=80 then 0.1
            ELSE 0
        END as bonus_percent
    FROM (SELECT emp_no, avg(score) as score FROM hr_grade GROUP BY emp_no) as t
    )

SELECT emp_no, emp_name, grade, (sal*bonus_percent) as bonus
FROM hr_employees JOIN bonus_table USING(emp_no)
ORDER BY emp_no;