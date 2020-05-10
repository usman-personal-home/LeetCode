class Solution(object):

    def majorityElementTrick(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # If the majority element is more than half,
        return nums[len(nums)/2]


    def hashMajorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if dic[num] > len(nums)/2:
                return num

    def sortMajorityElement(self, nums):
        nums.sort()
        print nums
        maxval = nums[0]
        # set count to 1
        count = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            print nums[i]
            print count
            print
        return


if __name__ == '__main__':

    nums = [2,2,2,1,1,1,1]
    testObj = Solution()
    print(testObj.sortMajorityElement(nums))