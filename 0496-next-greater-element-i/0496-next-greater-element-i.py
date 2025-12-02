class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        net ={}

        for n in nums2:
            while stack and n > stack[-1]:
                small = stack.pop()
                
                net[small] = n
            stack.append(n)

        for n in  stack:
            net[n] = -1

        return [net[n] for n in nums1]