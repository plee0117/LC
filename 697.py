class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        these = {}
        for idx, num in enumerate(nums):
            if num in these:
                these[num][0] += 1
                these[num][2] = idx
            else:
                these[num] = [1, idx, idx]
        out = len(nums)
        freq = {}
        freqh = 0
        for key, val in these.items():
            if val[0] == freqh:
                freq[key] = val
            elif val[0] > freqh:
                freq = {}
                freq[key] = val
                freqh = val[0]
        for key, val in freq.items():
            out = min(out, val[2] - val[1] + 1)
        return out