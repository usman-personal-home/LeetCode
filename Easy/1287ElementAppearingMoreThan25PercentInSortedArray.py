from __future__ import print_function


class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ct, l = 1, len(arr)
        thres = int(l // 4)
        for i in range(l - 1):
            if arr[i + 1] == arr[i]:
                ct += 1
            else:
                if ct > thres:
                    return arr[i]
                ct = 1

        return arr[-1]

        # [5,3,4,2,8,6,7,1,3]
if __name__ == '__main__':
    nums = [1,2,2,6,6,6,6,7,102]
    testObj = Solution()
    print(testObj.findSpecialInteger(nums))