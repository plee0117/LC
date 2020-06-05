class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        down = {}
        up = {}
        for pair in prerequisites:
            if pair[1] in down:
                if pair[0] in down[pair[1]]:
                    return False
            if pair[0] in down:
                down[pair[0]].add(pair[1])
                if pair[1] in down:
                    down[pair[0]].update(down[pair[1]])
                    for i in down[pair[1]]:
                        up[i].update(up[pair[1]])
                    up[pair[1]].add(pair[0])
                    up[pair[1]].update(up[pair[0]])
                else:
                    down[pair[1]] = set()
                    up[pair[1]] = set([pair[0]]).union(up[pair[0]])
                for i in up[pair[0]]:
                    down[i].update(down[pair[0]])
            else:
                down[pair[0]] = set([pair[1]])
                up[pair[0]] = set()
                if pair[1] in down:
                    up[pair[1]].add(pair[0])
                    down[pair[0]].update(down[pair[1]])
                    for i in down[pair[1]]:
                        up[i].update(up[pair[1]])
                else:
                    down[pair[1]] = set()
                    up[pair[1]] = set([pair[0]])
        return True