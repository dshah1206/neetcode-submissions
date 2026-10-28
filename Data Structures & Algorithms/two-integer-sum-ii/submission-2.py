class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """ 
        T.C: O(N) & S.C: O(1) - Two Pointer Approach
        """
        # l = 0
        # r = len(numbers) - 1

        # while l<r:
        #     if numbers[l] + numbers[r] > target:
        #         r -= 1
        #     elif numbers[l] + numbers[r] < target:
        #         l += 1
        #     else:
        #         return [l+1, r+1]
        # return []
        """ 
        T.C: O(N^2) & S.C: O(1) - Brute Force Approach
        """
        # for i in range(len(numbers)):
        #     for j in range(i, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        # return []

        """ 
        T.C: O(N Log N) & S.C: O(1) - Binary Search Approach
        """
        # for i in range(len(numbers)):
        #     l, r = i+1, len(numbers)-1
        #     complement = target - numbers[i]
        #     while l<=r:
        #         mid = l + (r-l)//2
        #         if numbers[mid] == complement:
        #             return [i+1, mid+1]
        #         elif numbers[mid] > complement:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        # return []

        """ 
        T.C: O(N Log N) & S.C: O(1) - Binary Search Approach
        """
        results_hashmap = {}
        complement = 0

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in results_hashmap:
                return [results_hashmap[complement], i + 1]
            results_hashmap[numbers[i]] = i + 1
        return []
        
        