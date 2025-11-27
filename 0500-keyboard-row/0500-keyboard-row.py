class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            lower = set(word.lower())
            if lower.issubset(row1) or lower.issubset(row2) or lower.issubset(row3):
                result.append(word)
        
        return result
        