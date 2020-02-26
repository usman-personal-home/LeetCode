class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        mysum = 0

        for i in range(len(s)):
            # check if this is not the last element of the array
            if i != len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                mysum -= roman[s[i]]
            else:
                mysum += roman[s[i]]

        return mysum

if __name__ == '__main__':
    address = "MCMXCIV"
    testObj = Solution()
    print(testObj.romanToInt(address))