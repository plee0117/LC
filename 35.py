class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = 0
        for i in nums:
            if i >= target:
                return n
            else:
                n += 1
        return n