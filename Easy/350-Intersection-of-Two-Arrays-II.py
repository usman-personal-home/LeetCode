class Solution(object):

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        res = []
        for i in nums1:
            d[i] = d.get(i, 0) + 1
        print d
        for i in nums2:
            if i in d and d[i] > 0:
                res.append(i)
                d[i] -= 1

        return res


if __name__ == '__main__':

    nums1 = [3, 6, 1, 0, 2, 3, 3]
    nums2 = [3, 6, 1, 0, 3]
    testObj = Solution()
    print(testObj.intersect(nums2, nums1))