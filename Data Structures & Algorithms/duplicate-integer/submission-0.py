class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in range(0, len(nums)):
            if nums[n] not in seen:
                seen.add(nums[n])
            else:
                return True
        return False


        