class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for elem in vowels:
            S = (S.replace(elem, ""))

        print S
        return S


if __name__ == '__main__':
    testObj = Solution()
    testObj.removeVowels("leetcodeisacommunityforcoders")
