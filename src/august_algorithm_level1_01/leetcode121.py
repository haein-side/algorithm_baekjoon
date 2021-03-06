import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = math.inf
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)
        return profit