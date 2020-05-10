class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        l = len(nums2)
        for n in nums1:
            idx = nums2.index(n)
            found = False
            while idx < l:
                if nums2[idx] > n:
                    out.append(nums2[idx])
                    found = True
                    break
                idx += 1
            if not found:
                out.append(-1)
        return out