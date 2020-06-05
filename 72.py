class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        biggest = len(word1) + len(word2)
        out = []
        if not(word1 or word2):
            return 0
        elif not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        for idx, ltr in enumerate(word2):
            temp = []
            for j, l in enumerate(word1):
                if idx == 0:
                    up = j + 1
                else:
                    up = out[idx - 1][j] + 1
                if j == 0:
                    left = idx + 1
                else:
                    left = temp[-1] + 1
                if l == ltr:
                    if idx * j == 0:
                        if idx + j == 0:
                            same = 0
                        else:
                            same = max(j, idx)
                    else:
                        same = out[idx - 1][j - 1]
                else:
                    if idx * j == 0:
                        same = max(j, idx) + 1
                    else:
                        same = out[idx - 1][j - 1] + 1
                temp.append(min(left, up, same))
            out.append(temp)
        return out[-1][-1]