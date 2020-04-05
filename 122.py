class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        hold = None
        for idx, p in enumerate(prices[:-1]):
            if p > prices[idx + 1]:
                if hold != None:
                    profit += p - hold
                    hold = None
            elif p < prices[idx + 1]:
                if hold == None:
                    hold = p
        if hold != None:
            profit += prices[-1] - hold
        return profit