class Solution(object):
    def rotate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    nums = [1,2,3,4,5,6,7]
    k = 3
    testObj = Solution()
    print(testObj.rotate(nums, k))
