from pprint import pprint
import sys


def print_grid(grid):
    for row in grid:
        for e in row:
            print(" " + str(e)),
        print


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []

        a = []
        for i in range(len(A[0])):
            a.append([None] * len(A))
        M, N = len(A), len(A[0])
        ans = [[None] * M for _ in xrange(N)]
        print_grid(A)
        print_grid(ans)
        print_grid(a)
        for i, row in enumerate(A):
            for j, val in enumerate(row):
                ans[j][i] = val
        return ans
if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6]]
    testObj = Solution()
    print(testObj.transpose(mat))
