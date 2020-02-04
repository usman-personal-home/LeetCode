import sys

class Solution(object):

    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] % 2 != 0 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            elif A[i] % 2 == 0:
                i += 1
            else:
                j -= 1

        return A

if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    nums = [12, 2, 3, 6]
    testObj = Solution()
    print(testObj.sortArrayByParity(nums))
