class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results_hashmap = {}
        complement = 0

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in results_hashmap:
                return [results_hashmap[complement], i]
            results_hashmap[nums[i]] = i
            



                
        