class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ctmap = {}
        for c in s:
            if c not in ctmap:
                ctmap[c] = 1
            else:
                ctmap[c] += 1
        print ctmap
        res = 0

        for key in ctmap:
            if ctmap[key] % 2 == 0:
                # nothing to add to result because even values
                continue
            else:
                # Adding odd values, can only have 1 odd otherwise cannot be a palindrome
                res += 1

        return res <= 1


if __name__ == '__main__':

    A = "maham"
    testObj = Solution()
    print(testObj.canPermutePalindrome(A))