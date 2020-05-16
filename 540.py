class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        l = len(nums) - 1
        while i < l:
            if nums[i] != nums[i + 1]:
                return nums[i]
            else:
                i += 2
        return nums[-1]