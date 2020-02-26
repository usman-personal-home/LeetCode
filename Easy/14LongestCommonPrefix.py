class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type s: str
        :rtype: int
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        # initial current comparison is the first string
        current = strs[0]

        for i in range(1, len(strs)):
            temp = ""
            if len(current) == 0:
                break
            for j in range(len(strs[i])):
                if j < len(current) and current[j] == strs[i][j]:
                    temp += current[j]
                else:
                    break
            # reset the prefix to common between current and the next string
            current = temp
            # print current
        return current


if __name__ == '__main__':
    address = ["flower","flow","flight"]
    testObj = Solution()
    print(testObj.longestCommonPrefix(address))