class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = []
        for x in nums:
            if not arr or arr[-1] != x:
                arr.append(x)

        count = 0
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:   # hill
                count += 1
            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]: # valley
                count += 1

        return count