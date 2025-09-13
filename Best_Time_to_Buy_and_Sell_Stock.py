class Solution:
    def maxProfit(self, prices) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
    

prices = [10,1,5,6,7,1]

test= Solution()
print(test.maxProfit(prices))