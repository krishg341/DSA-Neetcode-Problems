class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        g=sorted(s)
        k=sorted(t)
        if g==k:
            return True
        else:
            return False
        