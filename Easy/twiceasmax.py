import sys

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        maxValue = max(nums)
        maxIndex = nums.index(maxValue)
        for i in nums:
            if i == maxValue:
                continue
            if maxValue < (2*i):
                maxIndex = -1

        return maxIndex
        """
        minInt = -sys.maxsize - 1
        maxValue = minInt
        secondMaxValue = minInt
        maxIndex = -1
        for i in range(len(nums)):
            if nums[i] > maxValue:
                secondMaxValue = maxValue
                maxValue = nums[i]
                maxIndex = i
            if maxValue > nums[i] > secondMaxValue:
                secondMaxValue = nums[i]
                print "im here"

            print "########"
            print maxValue
            print maxIndex
            print secondMaxValue
            print "########"
        if maxValue >= 2*secondMaxValue:
            return maxIndex
        else:
            return -1



if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    nums = [12, 2, 3, 6]
    testObj = Solution()
    print(testObj.dominantIndex(nums))
