from pprint import pprint
import sys


def print_grid(grid):
    for row in grid:
        for e in row:
            print(" " + str(e)),
        print


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r > 0 and c > 0 and matrix[r][c] != matrix[r-1][c-1]:
                    return False
        return True


if __name__ == '__main__':

    matrix = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ]
    testObj = Solution()
    print(testObj.isToeplitzMatrix(matrix))
