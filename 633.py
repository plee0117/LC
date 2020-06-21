class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s = 0
        idx = 0
        jdx = 0
        sqs = [0]
        while s < c:
            jdx += 1
            s = jdx ** 2
            sqs.append(s)
        if s == c:
            return True
        else:
            while s != c and idx < jdx:
                if s < c:
                    idx += 1
                else:
                    jdx -= 1
                s = sqs[idx] + sqs[jdx]
            if s == c:
                return True
            else:
                return False