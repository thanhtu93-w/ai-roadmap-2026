class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice =prices[0]
        maxProfit=0
        for p in prices:
            minPrice = min(minPrice,p)
            maxProfit =max(maxProfit, p-minPrice)
        return maxProfit
