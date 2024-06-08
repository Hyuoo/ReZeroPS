/*
Solving Date    : 2024.06.09
Title           : 부모의 형질을 모두 가지는 대장균 찾기
tags            : SELECT, SELF JOIN, BIT MASK
url             : https://school.programmers.co.kr/learn/courses/30/lessons/301647
*/

SELECT a.ID, a.GENOTYPE, p.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA a
LEFT JOIN ECOLI_DATA p ON a.PARENT_ID = p.ID
WHERE p.GENOTYPE - (a.GENOTYPE & p.GENOTYPE) = 0
ORDER BY ID
;

/*
p.GENOTYPE - (a.GENOTYPE & p.GENOTYPE) = 0
이 식을
(a.GENOTYPE & p.GENOTYPE) = p.GENOTYPE
이렇게 하는게 더 낫네
*/