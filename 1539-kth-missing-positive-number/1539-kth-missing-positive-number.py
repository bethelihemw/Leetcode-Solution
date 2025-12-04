class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i, num in enumerate(arr):
            missing = num - (i + 1)
            if missing >= k:
                return k + i
        return k + len(arr)
        