class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #dp[i] = max profit if i sell up to day i
        #dp[i] = prices[i] - m
        dp = [0] * len(prices)
        minimum = float('inf')
        maxprofit = 0
        for i in range (len(prices)):

            minimum = min(minimum, prices[i])
            profit = prices[i] - minimum
            maxprofit = max(maxprofit, profit)
        return maxprofit


            
                



            