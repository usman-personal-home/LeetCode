from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #return sorted(s) == sorted(t)
        c1 = Counter(s)
        c2 = Counter(t)
        print len(c1 - c2)

        if cmp(c1, c2) == 0:
            return True
        else:
            return False



if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    testObj = Solution()
    print(testObj.isAnagram(s,t))