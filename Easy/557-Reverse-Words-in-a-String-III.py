class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_arr = s.split(" ")
        print str_arr
        for i,s in enumerate(str_arr):
            s = s[::-1]
            str_arr[i] = s

        print str_arr
        return " ".join(str_arr)


if __name__ == '__main__':
    str = "Let's take LeetCode contest"
    testObj = Solution()
    print(testObj.reverseWords(str))