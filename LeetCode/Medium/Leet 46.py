class Solution:
    def rec(self, ret: List[List[int]], nums: List[int], p: List[int], check: Set) -> None:
        if len(p)==len(nums):
            ret.append(p)
        for n in nums:
            if n not in check:
                self.rec(ret, nums, p+[n], check|{n})

    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.rec(ret, nums, [], set())
        return ret

# 46. Permutations
# 중복체크 단순 리스트검사 -> 셋 -> add/remove 제거
# 44 ms  16.2 MB
