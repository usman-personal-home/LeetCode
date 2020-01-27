class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evenNums = 0  # type: int
        for number in nums:
            count = 0
            while number > 0:
                number = number // 10
                count = count + 1
            if count % 2 == 0:
                evenNums += 1

        print(evenNums)
        return evenNums


if __name__ == '__main__':
    nums = [12, 345, 2, 6, 7896]
    testObj = Solution()
    testObj.findNumbers(nums)
