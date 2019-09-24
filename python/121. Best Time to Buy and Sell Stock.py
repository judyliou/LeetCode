class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        min_price = prices[0]
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            profit = p - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
