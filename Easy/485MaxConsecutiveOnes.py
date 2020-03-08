class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0
        cur_max = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cur_max += 1
                max1 = max(cur_max, max1)
            else:
                cur_max = 0

        return max1




if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    nums = [1,1,0,1,1,1]
    testObj = Solution()
    print(testObj.thirdMax(nums))
