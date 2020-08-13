class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ct = 0
        for s in S:
            if s in J:
                ct += 1
        return ct