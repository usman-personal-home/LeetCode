class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1

        for key, val in mydict.items():
            if val > len(nums) // 2:
                return key



if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    nums = [12, 2, 3, 6]
    testObj = Solution()
    print(testObj.majorityElement(nums))