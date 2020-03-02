from pprint import pprint


def print_grid(grid):
    for row in grid:
        for e in row:
            print(" " + str(e)),
        print


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #print_grid(grid)
        result = 0
        for i in range(len(grid)):
            #print grid[i]
            row = grid[i]
            for j in range(len(row)):
                #print grid[i][j]
                if grid[i][j] < 0:
                    result += 1

            #print("####")
        return result

if __name__ == '__main__':
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    testObj = Solution()
    print(testObj.countNegatives(grid))
