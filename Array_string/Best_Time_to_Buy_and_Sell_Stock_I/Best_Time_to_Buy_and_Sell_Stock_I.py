class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0
        max_prices = []
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price
                max_prices.append(max_profit)
                max_profit = 0
                min_price = price

        return sum(max_prices)


solution = Solution()

prices = [1,2,3,4,5]

print(solution.maxProfit(prices))
