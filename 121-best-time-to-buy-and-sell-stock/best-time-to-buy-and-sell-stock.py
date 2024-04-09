class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit =0 
        minprice = 999999
        for i in range(len(prices)):
            minprice =min(minprice, prices[i])
            maxprofit = max(maxprofit , prices[i]-minprice)
        return maxprofit
