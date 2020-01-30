class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True

        i = 0
        j = len(s) - 1
        half = len(s) // 2

        while i <= half:
            if s[i] != s[j]:
                sub1 = s[i:j]
                print(sub1)
                sub2 = s[i + 1:j + 1]
                print(sub2)

                return (sub1 == sub1[::-1]) or (sub2 == sub2[::-1])

            i += 1
            j -= 1


if __name__ == '__main__':

    A = "cbadabccbaabc"
    testObj = Solution()
    print(testObj.validPalindrome(A))