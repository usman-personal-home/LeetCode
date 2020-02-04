class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ss = (s + s)[1:-1]
        print ss
        exit()
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1

        keys = d.keys()
        if len(keys) == 1:
            return True
        for key in keys:
            print key


        return False

if __name__ == '__main__':
    A = "abab"
    #A = "aaaaaaaa"
    testObj = Solution()
    print(testObj.repeatedSubstringPattern(A))