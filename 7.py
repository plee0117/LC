class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            return conv(x)
        elif x < 0:
            return -conv(-x)

def conv(x):
    strint = str(x)
    j = ''
    for i in range(len(strint)):
        j += strint[-1-i]
    j = int(j)
    if j <= 2**31 -1 and j >= -2**31:
        return j
    else:
        return 0