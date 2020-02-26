class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd_max = even_max = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                even_max += nums[i]
            else:
                odd_max += nums[i]

        print even_max
        print odd_max
        return max(even_max, odd_max)

if __name__ == '__main__':

    nums = [1,2,3,1]
    testObj = Solution()
    print(testObj.rob(nums))