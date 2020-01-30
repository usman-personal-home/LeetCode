class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        size = len(s)
        s = list(s)
        for i in (range(len(s)/2)):
            s[i], s[size - i - 1] = s[size - i - 1],s[i]

        return "".join(s)

        print s
if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    str = "hello"
    testObj = Solution()
    print(testObj.reverseString(str))
