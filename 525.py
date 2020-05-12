class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2:
            return 0
        s = [0]
        for n in nums:
            if n == 1:
                s.append(s[-1] + 1)
            else:
                s.append(s[-1] - 1)
        ids = dict()
        for pos, val in enumerate(s):
            if val in ids:
                ids[val].append(pos)
            else:
                ids[val] = [pos]
        biggest = 0
        for k, v in ids.items():
            biggest = max(v[-1] - v[0], biggest)
        return biggest