"""
문자열 탐색 트리 Trie
(=radix tree, prefix tree, retrieval tree)

문자열을 효율적으로 저장 및 탐색하기 위한 트리 형태의 자료구조
자동완성이나 사전검색 등의 문자열 탐색에 특화되어 있다.

탐색시간에 장점이 있지만, 저장공간은 너무 많이 먹는다.

최대 L 길이, M개 문자열을 트라이에 모두 저장한다면
- 생성 시간 복잡도 : O(M*L)
    - 각 문자열 삽입은 O(L)
- 탐색 시간 복잡도 : O(L)

출처:
https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8A%B8%EB%9D%BC%EC%9D%B4-Trie
"""


class Node:
    def __init__(self, data=None):
        self.children = {}
        self.data = data


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        # 노드가 없으면 추가, 마지막일 경우 데이터 삽입
        cur = self.root

        for ch in string:
            if ch not in cur.children.keys():
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.data = string

    def insert_recursive(self, string, cur=None):
        # 존재 유무만 저장
        if not string:
            cur.data = "_"
            return
        if cur == None:
            cur = self.root
        a, *b = string
        if a not in cur.children.keys():
            cur.children[a] = Node()
        self.insert_recursive(b, cur.children[a])

    def find(self, string):
        # 노드가 있으면 계속 탐색 후 데이터 유무 검사
        cur = self.root

        for ch in string:
            if ch in cur.children.keys():
                cur = cur.children[ch]
            else:
                return -1

        if cur.data:
            return cur.data
        else:
            return -1

    def find_recursive(self, string, cur=None):
        # 존재 유무만 판단
        if not string:
            if cur.data:
                return True
            else:
                return False
        if cur == None:
            cur = self.root

        a, *b = string
        if a in cur.children.keys():
            return self.find_recursive(b, cur.children[a])
        else:
            return False


if __name__ == "__main__":
    t = Trie()
    tt = Trie()

    a = ["tea", "tech", "to", "ten", "a", "ab", "b", "aab", "in"]
    b = ["tea", "tecc", "a", "bb", "aa", "aaa", "aab", "i"]

    for i in a: t.insert(i)
    for i in b: print(i, t.find(i))

    print("="*30)

    for i in a: tt.insert_recursive(i)
    for i in b: print(i, tt.find_recursive(i))

