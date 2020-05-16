class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        imax = len(matrix[0])
        jmax = len(matrix)
        
        def insideEdge(x,y):
            # print(x,y)
            if x < 0:
                return False
            elif y < 0:
                return False
            elif y == jmax:
                return False
            elif x == imax:
                return False
            else:
                return True
            
        def mat(x,y):
            return matrix[y][x]
        runthru = 1
        again = True
        while again:
            again = False
            new = list()
            for j in range(jmax):
                row = []
                for i in range(imax):
                    neighbor = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
                    if matrix[j][i] < runthru:
                        row.append(matrix[j][i])
                    else:
                        nval = filter(lambda x: insideEdge(*x), neighbor)
                        dist = min(list(map(lambda x: mat(*x), nval))) + 1
                        if dist > runthru:
                            again = True
                        row.append(dist)
                new.append(row)
            matrix = new
            runthru += 1
        return new