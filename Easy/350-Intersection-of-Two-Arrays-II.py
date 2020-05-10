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
                # decrement count so all the duplicates are added
                d[i] -= 1

        return res

    def intersectSort(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Algorithm
        Sort nums1 and nums2.
        Initialize i, j and k with zero.
        Move indices i along nums1, and j through nums2:
        Increment i if nums1[i] is smaller.
        Increment j if nums2[j] is smaller.
        If numbers are the same, copy the number into nums1[k], and increment i, j and k.
        Return first k elements of nums1.
        """
        # Sort nums1 and nums2
        nums1.sort()
        nums2.sort()

        # Initialize i, j and k with zero.
        i = j = k = 0

        # Move indices i along nums1, and j through nums2
        while i < len(nums1) and j < len(nums2):
            # If numbers are the same, copy the number into nums1[k], and increment i, j and k.
            if nums1[i] == nums2[j]:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
            # Increment i if nums1[i] is smaller
            elif nums1[i] < nums2[j]:
                i += 1
            # Increment j if nums2[j] is smaller
            elif nums1[i] > nums2[j]:
                j += 1
        # Return first k elements of nums1
        return nums1[:k+1]



if __name__ == '__main__':

    nums1 = [1,2,2,1,2]
    nums2 = [2,2]
    testObj = Solution()
    print(testObj.intersectSort(nums2, nums1))