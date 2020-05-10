from collections import Counter
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        counter = Counter(arr1)
        print counter
        res = []
        for val in arr2:
            res.extend([val] * counter.pop(val))
            print res

        print res
        print counter
        tail = []
        print counter.most_common()
        for k,c in counter.most_common():
            tail.extend([k] * c)
        print tail
        res.extend(sorted(tail))
        return res

if __name__ == '__main__':
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]

    testObj = Solution()
    print(testObj.relativeSortArray(arr1, arr2))