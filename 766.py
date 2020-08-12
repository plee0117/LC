class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for rdx, row in enumerate(matrix[:-1]):
            for cdx, e in enumerate(row[:-1]):
                if e != matrix[rdx + 1][cdx + 1]:
                    return False
        return True