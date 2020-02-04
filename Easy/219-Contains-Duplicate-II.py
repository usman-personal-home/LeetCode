class Solution(object):
    def containsDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        print dic
        return False


if __name__ == '__main__':

    nums = [1,2,3,1,5,6,7,8,9]
    testObj = Solution()
    print(testObj.containsDuplicate(nums, 8))