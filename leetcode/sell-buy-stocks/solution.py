from typing import List
class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        lowest_seen_so_far = prices[0]
        max_profit = -1
        for price in prices:         
            lowest_seen_so_far = min(price, lowest_seen_so_far)
            max_profit = max(max_profit, price - lowest_seen_so_far)
        
        return max_profit
        


examples = [[7,1,5,3,6,4], [7,6,4,3,1]]

sol = Solution()
for ex in examples:
    print(sol.maxProfit(ex))