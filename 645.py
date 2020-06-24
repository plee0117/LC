class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        out = [0, 0]
        nums.sort()
        if nums[0] != 1:
            out[1] = 1
        if nums[-1] != len(nums):
            out[1] = len(nums)
        for idx, num in enumerate(nums[:-1]):
            if num == nums[idx + 1]:
                out[0] = num
                if out[1] > 0:
                    return out
            elif num == nums[idx + 1] - 2:
                out[1] = num + 1
                if out[0] > 0:
                    return out
        return out