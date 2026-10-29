class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        T.C: O(N^3), S.C: O(M)
        """
        # result = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 result.add(tuple([nums[i],nums[j],nums[k]]))
        # return [list(i) for i in result]

        """
        T.C: O(N^2), S.C: O(1) or O(N)
        """
        result = []
        nums.sort()

        for i,a in enumerate(nums):
            if a>0:
                break
            if i>0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, len(nums) - 1
            while l<r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return result




                 

        