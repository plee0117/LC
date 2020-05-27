class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numsort = sorted(nums)
        front = 0
        l = len(nums)
        while front <= l:
            if front == l:
                return 0
            elif nums[front] == numsort[front]:
                front += 1
            else:
                break
        back = 0
        while back < l:
            if nums[-1 - back] == numsort[-1 - back]:
                back += 1
            else:
                break
        return l - (front + back)