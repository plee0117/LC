class Solution:
    def findLHS(self, nums: List[int]) -> int:        
        from collections import Counter        
        c = Counter(nums)
        long = 0
        key = list(c.keys())
        key.sort()
        for idx, n in enumerate(key[:-1]):
            # print(pair)
            if key[idx + 1] - n == 1:
                long = max(long, c[key[idx + 1]] + c[n])
        return long