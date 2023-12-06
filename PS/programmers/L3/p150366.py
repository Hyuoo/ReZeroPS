"""
Solving Date    : 2023.12.03
Solving Time    : 2h
Title           : 표 병합
tags            : implement, data_structure
url             : https://school.programmers.co.kr/learn/courses/30/lessons/150366
runtime         : -
memory          : -
"""

from enum import Enum

class cell_stat(Enum):
    NULL = 0
    ALLOC = 1
    MERGED = 2

class cell():
    def __init__(self):
        self.stat = cell_stat.NULL
        self.value = ""
        self.refer = []
        self.merged = set()

    def __str__(self):
        return f"[{self.stat}, {self.value}, {self.refer}, {self.merged}]"


class table_object():
    def __init__(self):
        self.table = [[cell() for j in range(51)] for i in range(51)]

    def get_cell(self, r, c, refer=True):
        cell = self.table[r][c]
        if refer and cell.stat == cell_stat.MERGED:
            cell = self.get_cell(*cell.refer)

        return cell

    def set_cell(self, cell, stat=cell_stat.NULL, value="", refer=[], merged=set()):
        cell.stat = stat
        cell.value = value
        cell.refer = refer
        cell.merged = merged

    def update(self, r, c, value):
        cell = self.get_cell(r, c)
        if cell.stat == cell_stat.NULL:
            cell.stat = cell_stat.ALLOC
        cell.value = value

        return [cell]

    def update_all(self, value1, value2):
        cells = []
        for i in range(1, 51):
            for j in range(1, 51):
                cell = self.get_cell(i, j)
                if cell.stat == cell_stat.ALLOC and cell.value == value1:
                    cell.value = value2
                    cells.append(cell)

        return cells

    def merge(self, r1, c1, r2, c2):
        if (r1, c1) == (r2, c2):
            return

        base_cell = self.get_cell(r1, c1, refer=False)
        cell1 = self.get_cell(r1, c1)
        cell2 = self.get_cell(r2, c2)

        value = ""
        if cell2.value:
            value = cell2.value
        if cell1.value:
            value = cell1.value

        merged = cell1.merged | cell2.merged | {(r1, c1), (r2, c2)}

        for r, c in merged:
            tmp_cell = self.get_cell(r, c, refer=False)
            self.set_cell(tmp_cell, stat=cell_stat.MERGED, refer=[r1, c1])

        self.set_cell(base_cell, stat=cell_stat.ALLOC, value=value, merged=merged)

        return [base_cell]

    def unmerge(self, r, c):
        cell = self.get_cell(r, c, refer=False)
        refer_cell = self.get_cell(r, c)
        tmp_value = refer_cell.value

        if refer_cell.stat == cell_stat.NULL:
            return []

        for tmp in refer_cell.merged:
            tmp_cell = self.get_cell(*tmp, refer=False)
            self.set_cell(tmp_cell)
        self.set_cell(refer_cell)
        self.set_cell(cell, stat=cell_stat.ALLOC, value=tmp_value)

        return [cell]


def solution(commands):
    answer = []
    table = table_object()
    for command in commands:
        op, *v = command.split()
        if op == "UPDATE":
            # table[r][c] = value
            if len(v) == 2:
                t = table.update_all(*v)
            # table.replace(value1, value2)
            elif len(v) == 3:
                v = int(v[0]), int(v[1]), v[2]
                t = table.update(*v)
        elif op == "MERGE":
            # r1 c1 | r2 c2
            # 둘다 값 있으면 r1 c1이 값 기준.
            v = map(int, v)
            t = table.merge(*v)

        elif op == "UNMERGE":
            # r c의 모든 병합을 해제.
            # 해제 후 r, c제외 모든 값 NULL
            v = map(int, v)
            t = table.unmerge(*v)
        elif op == "PRINT":
            v = map(int, v)
            cell = table.get_cell(*v)

            if cell.value:
                answer.append(cell.value)
            else:
                answer.append("EMPTY")

        # print("=====",op, *v,"=====")
        # for c in t:
        #     print(c, end="\t")
        # print()

    return answer

"""
2023 KAKAO BLIND RECRUITMENT

왠지 본격적인 느낌으로다가 만들고 싶었다.
시키는대로 구현하면 되는 문제.
union-find로 푸는게 가장 이상적이라고 생각함
"""