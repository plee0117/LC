class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        if len(set(nums)) == len(nums):
            return False
        for i in range(max(length-k,1)):
            lim = min(i+k+1,length)
            # print(i, i+k, nums[i:i+k+1])
            if len(set(nums[i:lim])) < len(nums[i:lim]):
                return True
        return False