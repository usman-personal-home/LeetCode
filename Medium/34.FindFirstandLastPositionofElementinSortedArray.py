class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        # loop forward to find first char
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
                break
        # if the res is populated we didnt find the target hence return -1,-1
        if len(res) != 1:
            return [-1,-1]

        # loop backwards to find last char
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                res.append(j)
                break

        return res



if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8

    testObj = Solution()
    print(testObj.searchRange(nums, target))