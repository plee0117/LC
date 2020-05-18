class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for idx, num in enumerate(nums):
            if idx % 2 == 0:
                s += num
        return s