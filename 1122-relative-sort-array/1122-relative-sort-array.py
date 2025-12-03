class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    result.append(arr1[j])

        leftovers = [y for y in arr1 if y not in arr2]
        leftovers.sort()
        result.extend(leftovers)
        return result