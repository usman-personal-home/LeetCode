class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        sum = 0

        for i in range(0, len(nums),2):
            print i
            sum += nums[i]
        return sum

if __name__ == '__main__':
    A = [1,4,6,7,8,9]
    testObj = Solution()
    print(testObj.arrayPairSum(A))

