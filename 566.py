class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums[0]) * len(nums) != r * c:
            return nums
        else:
            mid = []
            for n in nums:
                mid += n
            last = [mid[c * i: c * (i + 1)] for i in range(r)]
            return last