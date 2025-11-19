class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        first = {}
        last = {}

        for i, n in enumerate(nums):
            count[n] = count.get(n, 0) + 1
            
            if n not in first:
                first[n] = i
            
            last[n] = i
        
        degree = max(count.values())
        res = len(nums)
        
        for n in count:
            if count[n] == degree:
                res = min(res, last[n] - first[n] + 1)
        
        return res