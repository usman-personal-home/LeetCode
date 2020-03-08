class Solution(object):

    def threeSum(self, nums, target):
        nums.sort()
        print nums

        length = len(nums)
        for i in xrange(length-2):
            l, r = i + 1, length - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return True

                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return False


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4, -1, 2, 2]
    target = 9
    testObj = Solution()
    print(testObj.threeSum(nums, target))
