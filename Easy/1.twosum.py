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
        print nums
        indices = []
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[target - nums[i]] = i
            else:
                print("found")
                indices.append((dict[nums[i]],i))
            print indices
            print(dict)
        return indices

    def twosumpointer(self, nums, target):
        nums.sort()
        i = 0
        j = len(nums) - 1
        indices = []

        while i < j:
            if nums[i] + nums[j] == target:
                indices = [i,j]
                break
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1

        return indices


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    testObj = Solution()
    print(testObj.twosumpointer(nums, 9))
