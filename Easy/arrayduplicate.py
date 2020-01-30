class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_dict = {}
        for i in nums:
            if i not in my_dict.keys():
                my_dict[i] = 1
            else:
                return True
        return False




if __name__ == '__main__':


    testObj = Solution()
    print(testObj.containsDuplicate(A))