from pprint import pprint
import sys


def print_grid(grid):
    for row in grid:
        for e in row:
            print(" " + str(e)),
        print


class Solution(object):
    def kWeakestRows(self, grid, k):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = []
        for i in mat:
            ans.append(i.count(1))
        final = []
        print ans
        for i in range(k):
            idx = ans.index(min(ans))
            # print(idx)
            final.append(idx)
            ans[idx] += sys.maxsize
            print ans
        return final


if __name__ == '__main__':
    mat = [ [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1]]
    testObj = Solution()
    print(testObj.kWeakestRows(mat, 3))
