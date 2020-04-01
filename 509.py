class Solution:
    def fib(self, N: int) -> int:
        fns = [0, 1]
        if N > 1:
            for i in range(2,N + 1):
                fns.append(fns[i - 2] + fns[i - 1])
        return fns[i]