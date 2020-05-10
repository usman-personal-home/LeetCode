
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        result = ""

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

    str1 = "ABABAB"
    str2 = "ABAB"
    testObj = Solution()
    print(testObj.gcdOfStrings(str1, str2))
