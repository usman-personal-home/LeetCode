class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        k = 3;
        1,2,3,4,5,6,7 reverse(nums, 0, nums.length -1 )
        7,6,5,4,3,2,1 reversing the entire array.  Reverse(noms, 0, k-1);
        5 6 7 4 3 2 1 reversing the first k elements reverse(noms, k, noms.length -1)
        5 6 7 1 2 3 4 reverse k + 1 till the end
        """

        # reverse the whole array
        self.reverse(nums, 0, len(nums) - 1)

        #
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums) - 1)
        return nums

    def reverse(self, arr, i, j):
        print i
        print j
        while i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
        print arr
        return arr


if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    nums = [1,2,3,4,5,6,7]
    #print(nums[-1])
    for i in range(len(nums)-1, -1, -1):
        print i
    exit()
    k = 3
    testObj = Solution()
    print nums
    print(testObj.rotate(nums, k))

