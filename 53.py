class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        maxi = nums[0]
        pos = 0
        maybe  = 0
        abandoned = nums[0]
        for idx, num in enumerate(nums[1:]):
            if num < 0:
                if maxi < 0 and num > maxi:
                    maxi = num
                elif maxi > 0 and maybe + num < -1 * maxi:
                    abandoned = max(abandoned,maxi)
                    maxi = num
                    maybe = 0
                else:
                    maybe += num
            elif num > 0:
                if maxi <= 0:
                    maxi = num
                    maybe = 0
                elif maybe + num > 0:
                    maxi += maybe + num
                    maybe = 0
                else:
                    maybe += num
            else:
                if maxi < 0:
                    maxi = num
                    maybe = 0
        return max(abandoned,maxi)