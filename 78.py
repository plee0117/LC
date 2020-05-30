class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        out = []
        for r in range(len(nums) + 1):
            temp = combinations(nums, r)
            out += [list(i) for i in temp]
        return out