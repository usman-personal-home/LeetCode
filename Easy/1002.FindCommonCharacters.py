from collections import Counter
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        ans = []
        d1 = Counter(A[0])
        print d1
        for i in range(1, len(A)):
            d2 = Counter(A[i])
            d1 = d1 & d2
            print d2
            print d1
        ans = list(d1.elements())

        return ans

if __name__ == '__main__':

    words = ["bella","lpppbelj","roller"]
    testObj = Solution()
    print(testObj.commonChars(words))