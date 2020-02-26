class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return -1
        if len(haystack) < len(needle):
            return 0
        schar = needle[0]
        found = True
        for i in range(len(haystack)):
            if haystack[i] == schar:
                k = i
                for j in range(len(needle)):
                    if needle[j] == haystack[k]:
                        k += 1
                    else:
                        found = False
                        break
                if found:
                    return i
        return -1


if __name__ == '__main__':
    str = "aaa"
    testObj = Solution()
    print(testObj.strStr(str, "aaaa"))