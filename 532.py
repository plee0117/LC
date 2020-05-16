class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ct = 0
        if k == 0:
            from collections import Counter
            for v in Counter(nums).values():
                if v > 1:
                    ct += 1
        elif k > 0:
            u = list(set(nums))
            u.sort()
            i = 0
            l = len(u) - 1
            while i < l:
                if u[i] + k in u[i + 1:]:
                    ct += 1
                i += 1
        return ct