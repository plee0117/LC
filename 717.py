class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        l = len(bits)
        idx = 0
        while idx < l - 1:
            if bits[idx] == 1:
                idx += 2
            else:
                idx += 1
        if bits[idx:] == [0] or bits[idx:] == [0, 0]:
            return True
        else:
            return False