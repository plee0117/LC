class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d.pop(n)
            else:
                d[n] = 1
        return d.popitem()[0]