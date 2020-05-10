class Solution(object):
    def sortArrayByParityII(self, a):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0  # pointer for even misplaced
        j = 1  # pointer for odd misplaced
        sz = len(a)

        # invariant: for every misplaced odd there is misplaced even
        # since there is just enough space for odds and evens

        while i < sz and j < sz:
            if a[i] % 2 == 0:
                i += 2
            elif a[j] % 2 == 1:
                j += 2
            else:
                # a[i] % 2 == 1 AND a[j] % 2 == 0
                print("swapping")
                a[i], a[j] = a[j], a[i]
                i += 2
                j += 2
            print i
            print j
            print a
        return a


if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    nums = [12, 1, 3, 6, 6, 7]
    testObj = Solution()
    print(testObj.sortArrayByParityII(nums))

