class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # r * c has to be a product m * n
        if len(nums) == 0 or r * c != len(nums) * len(nums[0]):
            return nums
        res = []
        for i in range(r):
            res.append([None] * c)
        print res

        # add all elements to a queue from matrix 1
        queue = []

        for row in nums:
            for val in row:
                queue.append(val)
        print queue

        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = queue.pop(0)

        return res


if __name__ == '__main__':
    mat = [[1,2],[3,4]]
    r = 1
    c = 4
    testObj = Solution()
    print(testObj.matrixReshape(mat, r, c))