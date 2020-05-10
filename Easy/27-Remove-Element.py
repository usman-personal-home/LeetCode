class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        for j in range(0,len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                print i
        return i


if __name__ == '__main__':
    nums = [3,2,2,3]
    testObj = Solution()
    print(testObj.removeElement(nums,3))