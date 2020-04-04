class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def fact(n):
            f = 1
            for i in range(1, n + 1):
                f = i * f
            return f
        l = []
        for idx in range(rowIndex + 1):
            l.append(fact(rowIndex)//fact(idx)//fact(rowIndex-idx))
        return l