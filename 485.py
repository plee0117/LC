class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        c = 0
        for i in nums:
            if i == 0:
                m = max(m, c)
                c = 0
            else:
                c += 1
        m = max(m, c)
        return m