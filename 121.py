class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        low = prices[0]
        profit = 0
        for price in prices:
            if price < low:
                low = price
            elif price - low > profit:
                profit = price - low
        return profit