class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of nums1.
        nums1_copy = nums1[:m]
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1 = 0
        p2 = 0

        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        print p1
        print p2
        print nums1[p1 + p2:]
        print nums1_copy[p1:]
        print nums1
        print nums2[p2:]
        # if there are still elements to add
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1 = nums1 + nums2[p2:]
            #nums1[p1 + p2:] = nums2[p2:]
        print nums1[p1 + p2:]
        print nums1


if __name__ == '__main__':

    nums1 = [1, 2, 3]
    m = 3
    nums2 = [2, 5, 6, 9]
    n = 3

    testObj = Solution()
    print(testObj.merge(nums1, 3, nums2, 3))