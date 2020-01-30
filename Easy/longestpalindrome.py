class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ctmap = {}
        for c in s:
            if c not in ctmap:
                ctmap[c] = 1
            else:
                ctmap[c] += 1
        print ctmap
        ret = 0
        singleCharFound = 0
        for key in ctmap:
            if ctmap[key] % 2 == 0:
                ret += ctmap[key]
            else:
                ret += ctmap[key] - 1
                singleCharFound = 1

        return ret + singleCharFound


if __name__ == '__main__':

    A = "cbc"
    testObj = Solution()
    print(testObj.longestPalindrome(A))