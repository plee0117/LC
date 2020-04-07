class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums)
        while i > 0:
            i -= 1
            if nums[i] == val:
                nums.pop(i)
        return len(nums)