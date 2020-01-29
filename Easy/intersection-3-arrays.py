import sys
class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        result = []
        dict = {}
        combo = list(set(arr1)) + list(set(arr2)) + list(set(arr3))  # make it unique
        print combo
        for i in combo:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for keys,vals in dict.items():
            if vals >= 3:
                result.append(keys)

        return result

if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    nums1 = [1,1,2,3,4,5,6]
    nums2 = [1,2,3,4,25,26]
    nums3 = [1,2,3,4,14,15,20]

    testObj = Solution()
    print(testObj.arraysIntersection(nums1, nums2, nums3))
