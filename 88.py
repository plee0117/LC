class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ni = 0
        mi = 0
        while ni < n:
            if mi == m + ni:
                for i in range(ni,n):
                    nums1.insert(mi,nums2[ni])
                    nums1.pop()
                    print(nums1)
                    ni += 1
                    mi += 1
                    break
            elif nums1[mi] > nums2[ni]:
                nums1.insert(mi,nums2[ni])
                nums1.pop()
                print(nums1)
                ni += 1
                mi += 1
            else:
                mi += 1