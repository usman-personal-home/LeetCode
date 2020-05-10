class Solution(object):
    def majorityElementSorted(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = 1

        for i in range(len(nums)):
            if i == 0:
                continue
            if nums[i] == nums[i-1]:
                freq += 1
                if freq >= len(nums) // 2:
                    return True
            else:
                freq = 1
        return False





if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    nums = [12, 2, 3, 6, 6, 6, 6, 6]
    nums.sort()
    print nums
    testObj = Solution()
    print(testObj.majorityElementSorted(nums))
    hello()