#You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
#You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
#Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 0
        j = 1
        while j < len(prices):
            if prices[i] < prices[j]:
                if prices[j] - prices[i] > res:
                    res = prices[j] - prices[i]
            else:
                i = j
            j += 1
        return res
        
