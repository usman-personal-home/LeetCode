class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fmax = smax = tmax = float('-inf')

        for i in nums:
            if i > fmax:
                tmax = smax
                smax = fmax
                fmax = i
            elif smax < i < fmax:
                tmax = smax
                smax = i
            elif tmax < i < smax:
                tmax = i

        if tmax == float('-inf'):
            return fmax
        else:
            return smax

if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    nums = [12, 2, 3, 6, 3]
    testObj = Solution()
    print(testObj.thirdMax(nums))
