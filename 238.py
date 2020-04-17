class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        for i in range(len(nums) - 1):
            left.append(left[i] * nums[i])
            right.append(right[i] * nums[-1 - i])
        out = []
        for j in range(len(nums)):
            out.append(left[j] * right[-1 - j])
        return out