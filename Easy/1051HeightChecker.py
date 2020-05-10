class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = sorted(heights)
        counter =  0

        for i in range(len(heights)):
            if heights[i] != res[i]:
                counter += 1

        return counter


if __name__ == '__main__':
    heights = [1,1,4,2,1,3]

    testObj = Solution()
    print(testObj.heightChecker(heights))