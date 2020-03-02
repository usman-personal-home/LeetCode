class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        b = sorted(arr)
        rank = {}
        res = []
        print b
        j = 0
        for i in range(len(b)):
            if not b[i] in rank:
                rank[b[i]] = j + 1
                j += 1

        print rank
        for i in range(len(arr)):
            res.append(rank[arr[i]])
        return res

    # [5,3,4,2,8,6,7,1,3]
if __name__ == '__main__':
    nums = [37,12,28,9,100,56,80,5,12]
    testObj = Solution()
    print(testObj.arrayRankTransform(nums))