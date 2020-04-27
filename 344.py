class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s) - 1
        h = (l + 1) // 2
        i = 0
        while i < h:
            t = s[i]
            s[i] = s[l - i]
            s[l - i] = t
            i += 1