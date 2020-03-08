class Solution(object):

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            # check if the number is negative at the temp i ndex, meaning it has been encountered before
            # hence a duplicate
            if nums[temp] < 0:
                res.append(temp + 1)
            # mark i-1 index to negative
            else:
                nums[temp] *= -1
            print nums
        return res

    def hashfindDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        my_hash = {}
        for num in nums:
            if num in my_hash:
                my_hash[num] += 1
                if num not in res:
                    res.append(num)
            else:
                my_hash[num] = 1
        return res


if __name__ == '__main__':

    nums = [4,3,2,7,8,2,3,1,1]
    testObj = Solution()
    print(testObj.findDuplicates(nums))