class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # trying to find the highest price to sell and lowest price to buy
        # only that one must buy the stock first before selling it.

        curMaxProfit = 0

        l = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            curMaxProfit = max(curMaxProfit, prices[r] - prices[l])
        
        return curMaxProfit