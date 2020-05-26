class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def peel(matrix):
            out = []
            inner = []
            left = []
            rlast = len(matrix) - 1
            clen = len(matrix[0])
            for rdx, row in enumerate(matrix):
                if rdx == 0:
                    out += row
                elif rdx == rlast:
                    out += row[::-1]
                elif clen >= 2:
                    left.append(row[0])
                    out.append(row[-1])
                    inner.append(row[1:-1])
                else:
                    out += row
            if left:
                out += left[::-1]
            if inner:
                return out + peel(inner)
            else:
                return out
        if matrix:
            return peel(matrix)
        else:
            return []