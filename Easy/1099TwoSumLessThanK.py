class Solution(object):
    def twoSumLessThanK(self, a, K):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = sorted(a)

        i, j = 0, len(a) - 1

        ans = -1
        while i < j:
            if a[i] + a[j] < K:
                ans = max(ans, a[i] + a[j])
                i += 1
            else:
                j -= 1
        return ans


if __name__ == '__main__':
    nums = [34,23,1,24,75,33,54,8]
    testObj = Solution()
    print(testObj.twoSumLessThanK(nums, 60))
