class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [None] * n
        if n % 2 != 0:
            res[n/2] = 0

        l = 0
        r = n - 1
        num_to_add = 1
        while l < r:
            res[l] = -num_to_add
            res[r] = num_to_add
            num_to_add += 1
            r -= 1
            l += 1

        return res


if __name__ == '__main__':
    n = 25
    testObj = Solution()
    print(testObj.sumZero(n))