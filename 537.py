class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def csplit(x):
            i, j = x.split('+')
            i = int(i)
            j = int(j[:-1])
            return i, j
        ax, ay = csplit(a)
        bx, by = csplit(b)
        return str(ax * bx - ay * by) + '+' + str(ax * by + ay * bx) + 'i'