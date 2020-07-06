class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        big = 1
        ct = 1
        for idx, n in enumerate(nums[:-1]):
            if n >= nums[idx + 1]:
                big = max(big, ct)
                ct = 1
            else:
                ct += 1
        return max(big, ct)