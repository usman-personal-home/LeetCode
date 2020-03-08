class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_res = 0
        count = 0
        for i in range(len(nums)):
            if i == 0 or nums[i-1] < nums[i]:
                count += 1
                max_res = max(max_res, count)
            else:
                count = 1

        return max_res


if __name__ == '__main__':
    nums = [1,3,5,4,7,9,10]
    testObj = Solution()
    print(testObj.findLengthOfLCIS(nums))