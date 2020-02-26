class Solution(object):
    def countLetters(self, S):
        """
        :type address: str
        :rtype: str
        """
        res = 0
        same_count = 1
        for i, c in enumerate(S):
            if i > 0:
                if S[i - 1] == c:
                    same_count += 1
                    print same_count
                else:
                    same_count = 1
            res += same_count

        return res
"""     
        mysum = 1
        result = 0

        for i, c in enumerate(chars):
            if i == len(chars) - 1 or chars[i + 1] != c:
                print c
                #print i
                print mysum
                fct = 1
                for i in range(1,mysum + 1):
                    fct *= i
                result += fct
                mysum = 1
            else:
                mysum += 1
        return result
"""


if __name__ == '__main__':
    address = "aaa"
    testObj = Solution()
    print(testObj.countLetters(address))


