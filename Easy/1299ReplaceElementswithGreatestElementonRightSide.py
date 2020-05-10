class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]

        for i in range(len(arr)):
            maximum = 0
            for j in range(i+1, len(arr)):
                maximum = max(maximum, arr[j])
            arr[i] = maximum
        arr[-1] = -1
        return arr
        [17, 18, 5, 4, 6, 1]
        [18, 6, 6, 6, 1, -1]
        """
        maxn = arr[-1]
        for i in range(len(arr)-1,-1,-1):
            print
            print maxn
            print arr[i]

            if maxn < arr[i]:
                # update max, arr[i] becomes the previous max
                maxn, arr[i] = arr[i], maxn
            else:
                arr[i] = maxn
            print arr
            print
        arr[-1] = -1
        return arr


if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    testObj = Solution()
    print(testObj.replaceElements(arr))