class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        m = nums[0]
        iters = 0
        for i, n in enumerate(nums[1:]):
            iters += (nums[i] - n) * (i + 1)
        return iters