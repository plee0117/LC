class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        if nums:
            running = [0]
            for i, n in enumerate(nums):
                running.append(running[i] + n)
            print(running)
            for idx, n in enumerate(running[1:]):
                total += running[:idx + 1].count(n - k)
        return total