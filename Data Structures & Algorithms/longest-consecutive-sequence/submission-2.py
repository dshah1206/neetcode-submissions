class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        T.C = O(N^2), S.C = O(N): Brute Force
        """
        # res = 0
        # seen = set(nums)

        # for n in nums:
        #     streak, curr = 0, n
        #     while curr in seen:
        #         streak += 1
        #         curr += 1
        #     res = max(res, streak)
        # return res

        """
        T.C = O(N Log N), S.C = O(N) or O(1): Sort

        nums = [2,3,4,4,5,10,20]
        res = 4 (2,3,4,5)
        """
        if not nums:
            return 0
        res = 0
        nums.sort()

        curr = nums[0]
        streak = 0
        i = 0

        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and curr == nums[i]:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res




        



        