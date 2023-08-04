class Solution:
    s: str
    wordDict: List[str]
    check: List[bool]

    def word_cmp(self, idx: int) -> List[int]:
        ret = []
        for word in self.wordDict:
            if self.s[idx:].startswith(word):
                ret.append(len(word))
        return ret
    
    def word_check(self, idx: int) -> bool:
        if len(self.s)==idx:
            return True
        if self.check[idx]:
            return False
        self.check[idx] = True
        nxt = self.word_cmp(idx)
        flag = False
        if nxt:
            for i in nxt:
                flag |= self.word_check(idx+i)
        return flag

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.check = [False for _ in range(len(s))]
        self.wordDict = wordDict
        return self.word_check(0)
'''
139. Word Break

문자열 사전에 있는 모든 단어로 문자열을 표현할 수 있는지.

접근:
문자열 대치하는건 겹치는 부분이 있어 불가능
어차피 결국 맨처음부터 싹다 조회해야되니 처음부터 모든 케이스 파악

풀이:
1. 앞에서부터 읽어서 가능한 문자열 있으면 해당 인덱스만큼 진행해서 반복.
  - 가능한 Dict체크 함수 -> 진행되는 인덱스 리스트
  - 재귀로 잘린 문자열을 Dict체크 함수로 넘겨주는 역할

문제점:
"aaaaaaaaaaaaaaaaaaaaa", ["a", "aa", "aaa", "aaaa", ..]
이런 케이스에서 실패함. -> 시간초과
모든부분이 겹치다보니 재귀에서 시간이 너무 오래걸림
  -> 어차피 특정인덱스까지 도달하면 중간과정과 상관없이 이후(남은) 문자열 처리하면 되니
    인덱스별 체크를 해서 이미 처리된 부분이면 스킵.

'''
