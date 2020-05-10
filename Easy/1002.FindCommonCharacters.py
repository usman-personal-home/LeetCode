from collections import Counter
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        # Get the first word in a dict
        d = {i: A[0].count(i) for i in A[0]}
        print d
        for i in A[1:]:
            for j in d.keys():
                if i.count(j) < d[j]:
                    d[j] = i.count(j)
        print d
        n = ''
        for i in d.keys():
            n += i * d[i]
        print n
        return [i for i in n]


if __name__ == '__main__':

    words = ["bella","label", "hello"]
    testObj = Solution()
    print(testObj.commonChars(words))