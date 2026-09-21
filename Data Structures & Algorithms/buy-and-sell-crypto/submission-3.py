class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftP, rightP = 0, 1
        profit = 0

        while rightP < len(prices):
            if prices[leftP] > prices[rightP]:
                leftP = rightP
                rightP += 1
            else:
                profit = max(profit, prices[rightP] - prices[leftP])
                rightP += 1
        
        return profit
            
 

        