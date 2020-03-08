from collections import Counter
class Solution(object):
    def frequentChars(self, A):
        """
        :type A: A[str]
        :rtype: A[str]
        """
        counter = 0
        num = List[0]

        for i in A:
            curr_frequency = A.count(i)
            if curr_frequency > counter:
                counter = curr_frequency
                num = i

        return num


if __name__ == '__main__':

    words = [1,2,3,4,1,3,1,1,4,4,6]
    testObj = Solution()
    print(testObj.frequentChars(words))