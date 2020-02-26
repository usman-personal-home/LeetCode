class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        #print address.split(".")
        return "[.]".join(address.split("."))


if __name__ == '__main__':
    address = "1.1.1.1"
    testObj = Solution()
    print(testObj.defangIPaddr(address))


