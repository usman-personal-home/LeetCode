class Solution(object):

    def twoSumSorted(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = []
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                indices = [i,j]
                break
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1

        return indices

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = []
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                print("found")
                indices = map[nums[i]],i
        print(map)
        return indices


if __name__ == '__main__':
    nums = [3,2,4]
    testObj = Solution()
    print(testObj.twoSum(nums, 5))
