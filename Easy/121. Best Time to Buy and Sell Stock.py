class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit, cost = (0, float('inf'))

        for price in prices:

            cost = min(price, cost)  # set the lowest possible cost
            print(cost, price)
            cur_profit = price - cost
            profit = max(profit, cur_profit)
            print(profit)

        return profit


if __name__ == '__main__':
    A = [7,1,5,3,6,4]

    testObj = Solution()
    print(testObj.maxProfit(A))