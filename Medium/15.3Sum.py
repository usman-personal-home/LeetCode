class Solution(object):

    def threeSum(self, nums):
        res = []
        nums.sort()
        print nums

        length = len(nums)
        for i in xrange(length-2): #[8]
            if nums[i] > 0:
                break #[7]
            # Loop for duplicates in i
            if i > 0 and nums[i] == nums[i-1]:
                print ("same i " + str(nums[i]))
                continue  #[1]

            l, r = i + 1, length - 1  #[2]
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0: #[3]
                    l += 1
                elif total > 0: #[4]
                    r -= 1
                else: #[5]
                    res.append([nums[i], nums[l], nums[r]])
                    # Loop for duplicates
                    while l < r and nums[l] == nums[l+1]: #[6]
                        print("in here same l " + str(nums[l]))
                        l += 1
                    # Loop for duplicates
                    while l < r and nums[r] == nums[r-1]: #[6]
                        print("in here same r " + str(nums[l]))
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4, -1, 2, 2]
    testObj = Solution()
    print(testObj.threeSum(nums))
