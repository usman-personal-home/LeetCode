import os
from __future__ import print_function
import collections
import sys

class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ic = collections.Counter(A)
        max_val = -sys.maxint - 1
        
        for key, val in ic.items():
            if val == 1:
                max_val = max(max_val, key)
        return max_val


if __name__ == '__main__':
    nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    testObj = Solution()
    print(testObj.largestUniqueNumber(nums))