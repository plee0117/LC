class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = sum(nums[:k])
        p = sum(nums[:k])
        for idx, n in enumerate(nums[:-k]):
            p = p - n + nums[idx + k]
            m = max(m, p)
        return m / k