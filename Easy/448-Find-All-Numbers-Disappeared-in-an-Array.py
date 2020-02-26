class Solution(object):

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        print nums
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)

        return res


if __name__ == '__main__':

    nums = [4,3,2,7,8,2,3,1]
    testObj = Solution()
    print(testObj.findDisappearedNumbers(nums))