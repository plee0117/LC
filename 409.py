class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        long = 0
        odd = 0
        for i in Counter(s).values():
            long += (i // 2) * 2
            if i % 2 == 1:
                odd = 1
        return long + odd