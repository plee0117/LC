class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        return [item[0] for item in Counter(nums).most_common(k)]