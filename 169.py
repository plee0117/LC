class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cut = len(nums)//2 + 1
        dic_ = {}
        for num in nums:
            if num in dic_:
                dic_[num] += 1
            else:
                dic_[num] = 1
            if dic_[num] == cut:
                return num