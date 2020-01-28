class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        prod = 1
        while n > 0:
            dig = n % 10
            print dig
            sum = sum + dig
            prod = prod * dig
            n = n // 10

        return prod - sum


if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    #nums = [12, 2, 3, 6]
    testObj = Solution()
    print(testObj.subtractProductAndSum(234))