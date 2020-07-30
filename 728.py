class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        these = []
        num = left
        while num <= right:
            divisors = set([int(d) for d in str(num)])
            if 0 in divisors:
                num += 1
            elif all(map(lambda x: num % x == 0, divisors)):
                these.append(num)
                num += 1
            else:
                num += 1
        return these