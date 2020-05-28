class Solution:
    def countBits(self, num: int) -> List[int]:
        out = [0]
        poftwo = 1
        if num == 0:
            return out
        
        for i in range(1, num + 1):
            if i == poftwo * 2:
                poftwo *= 2
            out.append(1 + out[i - poftwo])
        return out