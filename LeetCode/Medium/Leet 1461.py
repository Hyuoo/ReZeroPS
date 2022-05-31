class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        a = [0 for _ in range(pow(2,k))]
        for i in range(len(s)-k+1):
            a[int("0b"+str(s[i:i+k]),2)] = 1
        if 0 in a:
            return False
        return True
