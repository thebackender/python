#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        i = 0
        for i, price in enumerate(prices):
            if i + 1  < len(prices):
                if price < prices[i+1]:
                    profit += prices[i+1] - price #add growth differense between this and next price
        return profit
print(Solution().maxProfit([1,2,3,4,5]))