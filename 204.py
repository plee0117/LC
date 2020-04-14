class Solution:
    def countPrimes(self, n: int) -> int:
        a = [False, False] + [True]*(n-2)
        upto = int(math.sqrt(n))+1
        for i in range(2,upto):
            for j in range(2*i,n,i):
                a[j] = False
        return sum(a)