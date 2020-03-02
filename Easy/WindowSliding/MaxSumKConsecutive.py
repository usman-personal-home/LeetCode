import sys

class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int

        n = len(nums)
        max_sum = 0

        for i in range(n - k + 1):
            #print("Index : " + str(i) + " Number : " + str(nums[i]))
            cur_sum = 0
            for j in range(i, i + k):
                print("Index J : " + str(j) + " Number : " + str(nums[j]))
                cur_sum += nums[j]
            print("#####")
            max_sum = max(max_sum, cur_sum)

        return max_sum
        """
        n = len(nums)
        # n must be greater than k
        if not n > k:
            print("Invalid")
            return -1

        # Compute sum of first window of size k
        max_sum = 0
        window_sum = sum([nums[i] for i in range(k)])
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        # Compute sums of remaining windows by
        # removing first element of previous
        # window and adding last element of
        # current window.
        #for i in range(n - k):
            #print("Index : " + str(i) + " Number : " + str(nums[i]))
        for i in range(n - k):
            print("Index I : " + str(i) + " Index I + K: " + str(i + k))
            print("Window Sum Before : " + str(window_sum))
            window_sum = window_sum - nums[i] + nums[i + k]
            print("Window Sum After : " + str(window_sum))
            print("$$$$$$")
            max_sum = max(window_sum, max_sum)

        return max_sum

if __name__ == '__main__':
    nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    testObj = Solution()
    print(testObj.maxSum(nums, 4))
