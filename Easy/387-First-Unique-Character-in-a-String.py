class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for i, val in enumerate(s):
            if d[val] == 1:
                return i

        return -1


if __name__ == '__main__':

    A = "leetcodel"
    testObj = Solution()
    print(testObj.firstUniqChar(A))