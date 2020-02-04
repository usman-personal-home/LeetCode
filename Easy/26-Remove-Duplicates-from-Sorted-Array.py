class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1,len(nums)):

            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            print(nums)
            print i
            print(j)
            print("%%%%%%")
        return i + 1



if __name__ == '__main__':
    nums = [1,1,2,2,2,3,3,3,3,4]
    testObj = Solution()
    print(testObj.removeDuplicates(nums))