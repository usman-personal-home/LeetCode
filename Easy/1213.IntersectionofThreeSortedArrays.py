class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        A = []
        sum = arr1 + arr2 + arr3
        d = {}

        for i in sum:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for key, value in d.items():
            if value == 3:
                A.append(key)

        return A

    def arraysIntersection2(self, arr1, arr2, arr3):
        if not arr1 or not arr2 or not arr3:
            return []

        p1 = 0
        p2 = 0
        p3 = 0

        result = []

        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):

            if arr1[p1] == arr2[p2] == arr3[p3]:
                result.append(arr1[p1])
                p1, p2, p3 = p1 + 1, p2 + 1, p3 + 1
                continue

            max_of_three = max(arr1[p1], arr2[p2], arr3[p3])

            if arr1[p1] < max_of_three:
                p1 += 1

            if arr2[p2] < max_of_three:
                p2 += 1

            if arr3[p3] < max_of_three:
                p3 += 1

        return result


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [1, 3, 4, 5, 8]
    testObj = Solution()
    print(testObj.arraysIntersection2(arr1, arr2, arr3))
