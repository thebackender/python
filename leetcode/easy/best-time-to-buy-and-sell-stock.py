#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2:
            return 0
        minprice = prices[0]
        profit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            if price - minprice > profit:
                profit = price - minprice
        return profit
print(Solution().maxProfit([7,1,5,3,6,4]))