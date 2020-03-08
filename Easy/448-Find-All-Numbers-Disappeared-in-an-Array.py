class Solution(object):

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            # find the index 1 less than the number and set it to negative if its positive
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
            print nums

        # add 1 to i and append all positive numbers to result
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res

    def hashfindDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        my_hash = {}

        for num in nums:
            if num in my_hash:
                my_hash[num] += 1
            else:
                my_hash[num] = 1

        print my_hash

        for num in range(1, len(nums) + 1):
            if num not in my_hash:
                res.append(num)

        return res

if __name__ == '__main__':

    nums = [4,3,2,7,8,2,3,1]
    testObj = Solution()
    print(testObj.findDisappearedNumbers(nums))