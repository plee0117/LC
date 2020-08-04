class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        big1 = [0, 0]
        big2 = 0
        for idx, n in enumerate(nums):
            if n > big1[0]:
                big2 = big1[0]
                big1 = [n, idx]
            elif n > big2:
                big2 = n
        if big1[0] >= big2 * 2:
            return big1[1]
        else:
            return -1