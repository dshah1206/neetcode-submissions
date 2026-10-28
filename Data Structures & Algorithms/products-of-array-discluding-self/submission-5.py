class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """T.C - O(N^2), S.C - O(N)"""
        # result = [0] * len(nums)
        # print(result)
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         prod = prod*nums[j]
        #     result[i] = prod
        # return result
        """T.C - O(N), S.C - O(N)"""
        # prod = 1
        # zero_cnt = 0

        # for num in nums:
        #     if num:
        #         prod *= num
        #     else:
        #         zero_cnt += 1
        
        # if zero_cnt > 1:
        #     return [0]*len(nums)

        # result = [0]*len(nums)

        # for i, num in enumerate(nums):
        #     # Case if there is 1 zero then rest index get zero and 
        #     # the index carrying zero gets the prod
        #     if zero_cnt:
        #         if num != 0:
        #             result[i] = 0
        #         else:
        #             result[i] = prod
        #     else:
        #         result[i] = prod//num
        # return result

        """T.C - O(N), S.C - O(N) - Prefix and Suffix"""
        n = len(nums)
        prefix_array = [0] * n
        suffix_array = [0] * n
        result = [0] * n

        prefix_array[0] = suffix_array[n-1] = 1

        for i in range(1, n):
            prefix_array[i] = prefix_array[i-1] * nums[i-1]
        
        for j in range(n-2,-1,-1):
            suffix_array[j] = suffix_array[j+1] * nums[j+1]
        
        for k in range(n):
            result[k] = prefix_array[k] * suffix_array[k]
        
        return(result)

            

                



        