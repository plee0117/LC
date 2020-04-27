class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        inter = []
        l1 = Counter(nums1)
        l2 = Counter(nums2)
        for i in l1.keys():
            if i in l2.keys():
                inter += [i] * min(l1[i], l2[i])
        return inter