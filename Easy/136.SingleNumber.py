class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # use the set to get unique values and multiply by 2
        # subtract the sum of nums from above
        return 2*sum(set(nums))-sum(nums)

    def singleNumberHash(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return key


if __name__ == '__main__':

    nums = [2,2,2,1]
    testObj = Solution()
    print(testObj.singleNumberHash(nums))