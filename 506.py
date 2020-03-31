class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        rnk = sorted(nums, reverse = True)
        medals = {0: 'Gold Medal', 1: 'Silver Medal', 2: 'Bronze Medal'}
        return [medals[rnk.index(i)] if rnk.index(i) in medals else str(rnk.index(i) + 1) 
                for i in nums]