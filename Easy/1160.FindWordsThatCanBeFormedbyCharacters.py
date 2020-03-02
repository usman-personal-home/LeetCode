import collections
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        for word in words:
            found = True
            for i in word:
                if word.count(i) > chars.count(i):
                    found = False
                    break
            if found:
                res += len(word)
        return res




if __name__ == '__main__':

    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"

    testObj = Solution()
    print(testObj.countCharacters(words,chars))
