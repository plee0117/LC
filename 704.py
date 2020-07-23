class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ldx = 0
        hdx = len(nums)
        while hdx > ldx:
            mid = (hdx + ldx) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                ldx = mid + 1
            else:
                hdx = mid
        return -1