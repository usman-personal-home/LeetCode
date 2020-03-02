class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        [-4,-1,0,3,10]
        """
        l,r = 0, len(A) - 1
        res = []
        while l <= r:
            #print l
            #print r
            print(abs(A[l]))
            print(abs(A[r]))
            print("####")
            if abs(A[l]) > abs(A[r]):
                res.append(A[l] ** 2)
                l += 1
            else:
                res.append(A[r] ** 2)
                r -= 1

        return res[::-1]
"""    left = 0
    right = len(a)-1
    res = []
    while right >= left:
        if abs(a[left]) > abs(a[right]):
            res.append(a[left]**2)
            left += 1
        else:
            res.append(a[right]**2)
            right -= 1
    return res[::-1]"""

if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    testObj = Solution()
    print(testObj.sortedSquares(nums))