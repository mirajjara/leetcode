# Miraj Jara - October 3, 2024
# Best Time To Buy And Sell Stock
# Easy problem
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# iterate backwards while keeping track of the biggest value seen
# subtract current value during iteration from biggest seen and store the biggest difference
# return the biggest difference

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        biggest_seen = prices[-1]
        biggest_diff = 0
        
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > biggest_seen:
                biggest_seen = prices[i]
                continue
            
            curr_diff = biggest_seen - prices[i]
            if curr_diff > biggest_diff:
                biggest_diff = curr_diff
            
        return biggest_diff