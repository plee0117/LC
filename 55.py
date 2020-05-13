class Solution:
    def canJump(self, nums: List[int]) -> bool:
        block = 0
        nums.pop()
        while nums:
            if nums[-1] <= block or nums[-1] == 0:
                block += 1
            else:
                block = 0
            nums.pop()
        return block == 0