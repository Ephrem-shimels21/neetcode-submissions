class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        if len(prices) <= 1:
            return profit

        slow, fast = 0, 1

        while fast < len(prices):
            if prices[fast] > prices[slow]:
                profit = max(profit, prices[fast] - prices[slow])
                            
            else:
                slow = fast
            
            fast += 1
        
        return profit

            
            

        