
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        bal = 0
        result = 0

        for i in s:
            if i == "R":
                bal -= 1
            else:
                bal += 1

            if bal == 0:
                result += 1
        return result


if __name__ == '__main__':
    address = "RLRl"
    testObj = Solution()
    print(testObj.balancedStringSplit(address))


