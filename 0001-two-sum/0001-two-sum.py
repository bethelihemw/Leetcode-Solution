class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
    
        for index, value in enumerate(nums):
            sums = target - value
            
            if sums in seen:
                return [seen[sums], index]
            
            seen[value] = index