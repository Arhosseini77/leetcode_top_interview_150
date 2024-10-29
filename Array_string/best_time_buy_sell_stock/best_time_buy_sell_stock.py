class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_dis = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] > prices[i]:
                    dis = prices[j] - prices[i]
                    if dis > max_dis:
                        max_dis = dis

        return max_dis

solution = Solution()

prices = [2,4,1]

print(solution.maxProfit(prices))