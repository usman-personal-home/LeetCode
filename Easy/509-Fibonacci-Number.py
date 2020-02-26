class Solution(object):

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N - 1) + self.fib(N - 2)


if __name__ == '__main__':
    testObj = Solution()
    print(testObj.fib(5))
