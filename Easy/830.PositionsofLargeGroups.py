class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]

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
        # This is for the case where all chars are the same 'aaa' or the same numbers are at the end of the array
        if count >= 3:
            res.append([start, len(S) - 1])
        """
        res = []
        count = 1
        start = 0
        for i in range(1,len(S)):
            if S[i] == S[i-1]:
                count += 1
            else:
                # the char has changed
                if count >= 3:
                    res.append([start, i - 1])
                count = 1
                start = i

        if count >= 3:
            res.append([start, len(S) - 1])

        return res


    def largeGroupPositions2(self, S):
        count = 1
        res = []
        start = 0
        for i in range(len(S) - 1):
            print start
            print S[i]
            if S[i] == S[i + 1]:
                count += 1
            # Char changes
            else:
                if count > 3:
                    #print S[i]
                    res.append([start, i])
                count = 1
                start = i + 1
        # This is for the case where all chars are the same 'aaa' or the same numbers are at the end of the array
        if count >= 3:
            res.append([start, len(S) - 1])
        return res

    def largeGroupPositions3(self, S):
        ans = []
        i = 0
        for j in xrange(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans

if __name__ == '__main__':
    chars = "abbbbccccceee"
    testObj = Solution()
    print(testObj.largeGroupPositions(chars))

