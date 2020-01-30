class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # print(nums)
        sum = 0

        for i in xrange(0, len(nums), 2):
            sum += nums[i]

        return sum


if __name__ == '__main__':
    A = [1,4,6,7]

    testObj = Solution()
    print(testObj.arrayPairSum(A))