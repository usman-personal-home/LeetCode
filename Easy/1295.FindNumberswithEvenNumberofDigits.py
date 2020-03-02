# -*- coding: utf-8 -*-

"""
Given an array nums of integers, return how many of them contain an even number of digits.
Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:
Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.
"""


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
