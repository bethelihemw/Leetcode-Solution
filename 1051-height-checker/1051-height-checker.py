class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorteds = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorteds[i]:
                count += 1
        
        return count