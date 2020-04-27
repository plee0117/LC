class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ct = 0
        more = (matrix != [])
        rmax = len(matrix) - 1
        while more:
            more = False
            ones = False
            cmax = len(matrix[0]) - 1 - ct
            for rdx, row in enumerate(matrix[:rmax + 1]):
                for cdx, element in enumerate(matrix[rdx][:cmax + 1]):
                    if rdx == rmax and cdx == cmax:
                        if int(element) == 1:
                            ones = True
                    elif rdx == rmax:
                        if int(element) + int(matrix[rdx][cdx + 1]) > 0:
                            ones = True
                    elif cdx == cmax:
                        if int(element) + int(matrix[rdx + 1][cdx]) > 0:
                            ones = True
                    else:
                        if (int(element) + int(matrix[rdx + 1][cdx]) + 
                            int(matrix[rdx][cdx + 1]) + int(matrix[rdx + 1][cdx + 1])) > 0:
                            ones = True
                        new = (int(element) * int(matrix[rdx + 1][cdx]) * 
                               int(matrix[rdx][cdx + 1]) * int(matrix[rdx + 1][cdx + 1]))
                        matrix[rdx][cdx] = new
                        if new > 0:
                            more = True
            if ones:
                ct += 1
            rmax -= 1
        return ct ** 2