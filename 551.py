class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        cons = 0
        for idx, ltr in enumerate(s):
            if ltr == 'A':
                cons = 0
                if a == 1:
                    return False
                else:
                    a += 1
            elif ltr == 'P':
                cons = 0
            elif ltr == 'L':
                cons += 1
                if cons == 3:
                    return False
        return True