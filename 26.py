class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        k = 0
        l = len(nums)
        while k < l:
            while i < l:
                if nums[k] < nums[i]:
                    nums[k+1] = nums[i]
                    k += 1
                i += 1
            return k+1