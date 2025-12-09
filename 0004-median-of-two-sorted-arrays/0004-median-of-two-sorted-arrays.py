import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        
        # Ensure nums1 is the shorter array (m <= n) for simplified binary search
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        
        # Calculate the size of the required left half partition
        # If N is odd, this is the index of the single median element.
        # If N is even, this is the index of the first of the two median elements.
        half = (m + n + 1) // 2
        
        low, high = 0, m  # Binary search on the partition size 'i' in nums1
        
        while low <= high:
            # i: number of elements taken from nums1 for the left half (partition index)
            i = (low + high) // 2
            
            # j: number of elements taken from nums2 for the left half
            # half = i + j
            j = half - i
            
            # Define the boundary elements of the partition. Use float('inf') for boundary cases.
            
            # Element just left of the partition in nums1 (A_left)
            A_left = nums1[i - 1] if i > 0 else float('-inf')
            # Element just right of the partition in nums1 (A_right)
            A_right = nums1[i] if i < m else float('inf')
            
            # Element just left of the partition in nums2 (B_left)
            B_left = nums2[j - 1] if j > 0 else float('-inf')
            # Element just right of the partition in nums2 (B_right)
            B_right = nums2[j] if j < n else float('inf')
            
            
            # Check for the correct partition (Order Check)
            if A_left <= B_right and B_left <= A_right:
                # Correct partition found!
                
                # Case 1: Odd total length (Median is the largest element in the left half)
                if (m + n) % 2 == 1:
                    return max(A_left, B_left)
                
                # Case 2: Even total length (Median is the average of the two central elements)
                else:
                    left_max = max(A_left, B_left)
                    right_min = min(A_right, B_right)
                    return (left_max + right_min) / 2.0
            
            # Refine the Binary Search (Partition in nums1 is too far right)
            elif A_left > B_right:
                high = i - 1
            
            # Refine the Binary Search (Partition in nums1 is too far left)
            else: # B_left > A_right
                low = i + 1
        
        # This line should technically never be reached if the input is valid.
        return 0.0