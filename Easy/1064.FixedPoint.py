class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i] == i:
                return i
        return -1


if __name__ == '__main__':
    nums = [-10,-5,0,3,7]
    testObj = Solution()
    print(testObj.fixedPoint(nums))
