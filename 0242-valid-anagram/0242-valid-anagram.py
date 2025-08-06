class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        from collections import Counter
        return Counter(s) == Counter(t)