class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        start = len(B) // len(A)
        if B in A * start:
            return start
        elif B in A * (start + 1):
            return start + 1
        elif B in A * (start + 2):
            return start + 2
        else:
            return -1