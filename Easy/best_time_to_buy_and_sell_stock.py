'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_prof = 0
        for val in prices:
            if val < min_price:
                min_price = val
            elif (val-min_price) > max_prof:
                max_prof = val-min_price
        return max_prof
        
    '''
    # Brute force
    
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <= 1:
            return 0
        max = 0
        for i in range(length-1):
            for j in range(i+1, length):
                tmp = prices[j]-prices[i]
                if tmp > max:
                    max = tmp
        return max
    '''    
    