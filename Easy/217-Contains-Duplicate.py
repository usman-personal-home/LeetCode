class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] == nums[i]:
                    return True
        return False

    def containsDuplicateSorted(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        print nums

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                    return True
        return False

    def containsDuplicateDict(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print d
        for k,v in d.items():
            if v > 1:
                return True

        return False


if __name__ == '__main__':

    nums = [4,1,3,2,4]
    testObj = Solution()
    print(testObj.containsDuplicateDict(nums))