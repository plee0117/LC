class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        small = [m,n]
        for i in ops:
            small = [min(small[0],i[0]),min(small[1],i[1])]
        return small[0] * small[1]