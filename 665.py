class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        ct = 0
        l = len(nums)
        for idx, n in enumerate(nums[:-1]):
            if n > nums[idx + 1]:
                if ct > 0:
                    return False
                elif idx == 0:
                    ct += 1
                elif idx + 2 == l:
                    return True
                elif nums[idx - 1] < nums[idx + 1]:
                    ct += 1
                elif n <= nums[idx + 2]:
                    ct += 1
                else:
                    return False
        return True