class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stk = []
        for i,c in enumerate(S):
            if stk and stk[-1] == c:
                stk.pop(-1)
            else:
                stk.append(c)
        return stk

if __name__ == '__main__':
    str = "abbaca"
    testObj = Solution()
    print(testObj.removeDuplicates(str))