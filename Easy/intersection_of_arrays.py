class Solution(object):

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mydict = {}
        result = []
        for i in nums1:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        for i in nums2:
            if i in mydict and i not in result:
                result.append(i)
        #print mydict
        #print result
        return result


if __name__ == '__main__':
    nums1 = [12, 345, 2, 6, 7896]
    nums2 = [12, 344, 2, 6, 786]
    testObj = Solution()
    print(testObj.intersection(nums1, nums2))