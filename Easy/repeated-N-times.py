class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = {}
        for a in A:
            if a not in d:
                d[a] = 1
            else:
                return a


if __name__ == '__main__':
    A = [2,1,2,5,3,2]

    testObj = Solution()
    print(testObj.repeatedNTimes(A))