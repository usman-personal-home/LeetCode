import collections

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rc = collections.Counter(ransomNote)
        mc = collections.Counter(magazine)

        for letter in ransomNote:
            if mc[letter] < rc[letter]:
                return False
        return True



if __name__ == '__main__':
    s1 = "aaa"
    s2 = "aab"
    testObj = Solution()
    print(testObj.canConstruct(s1, s2))
