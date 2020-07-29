class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        s = sum(nums)
        running = 0
        for idx, val in enumerate(nums):
            if running == s - val:
                return idx
            else:
                running += val
                s -= val
        return -1