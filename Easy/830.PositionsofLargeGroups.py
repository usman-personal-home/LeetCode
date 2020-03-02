class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        count = 1
        res = []
        start = 0
        for i in range(1, len(S)):
            # Keep counting if the chars are the same
            if S[i] == S[i - 1]:
                count += 1

            # The char changes
            else:
                # Only append to result if count is greater than 3
                if count >= 3:
                    res.append([start, i - 1])
                count = 1
                start = i
        # This is for the case where all chars are the same 'aaa'
        if count >= 3:
            res.append([start, len(S) - 1])
        return res



if __name__ == '__main__':
    chars = "abbxxxx"
    testObj = Solution()
    print(testObj.largeGroupPositions(chars))

