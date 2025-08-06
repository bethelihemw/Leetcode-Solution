class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        min_val = min(nums)
        max_val = max(nums)
        
        new_min = min_val + k
        new_max = max_val - k
        score = new_max - new_min

        return max(0, score)