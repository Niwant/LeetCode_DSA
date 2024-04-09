class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        maxprofit = 0 
        minprice = prices[0]
        for i in range(1,len(prices)):
            minprice = min(minprice,prices[i])
            maxprofit = max(maxprofit , prices[i]-minprice)
            if i+1 < len(prices) and prices[i] > prices[i+1]:
                minprice = 999999
                profit+=maxprofit
                maxprofit=0
        return profit+maxprofit
        