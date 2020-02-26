class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(list("aeiouAEIOU"))
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            # print s[i]
            # print s[j]
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                j -= 1
                i += 1
            elif s[j] not in vowels:
                j -= 1
            elif s[i] not in vowels :
                i += 1

        return "".join(s)


if __name__ == '__main__':
    str = "hello"
    testObj = Solution()
    print(testObj.reverseVowels(str))
