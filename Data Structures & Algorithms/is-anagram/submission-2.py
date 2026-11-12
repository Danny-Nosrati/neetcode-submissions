class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sl = sorted(list(s))
            tl = sorted(list(t))
            return sl == tl
        return False