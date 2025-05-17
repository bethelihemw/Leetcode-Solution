class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        l = 0
        r = 0
        while l < len(s):
            if r < len(spaces) and l == spaces[r]:
                result.append(" ")
                r += 1
            result.append(s[l])
            l += 1

        return "".join(result)