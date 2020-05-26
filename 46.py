class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        p = permutations(nums)
        return p