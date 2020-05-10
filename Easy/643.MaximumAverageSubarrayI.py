class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == k:
            return sum(nums)/float(k)
        s = 0
        for i in range(k):
            s += nums[i]
        max_sum = max(s,float('-inf'))
        for i in range(k,len(nums)):
            print s
            print

            s = s + nums[i] - nums[i-k]
            max_sum = max(s,max_sum)
        print ("###")
        print max_sum
        return float(max_sum)/k




if __name__ == '__main__':
    arr = [9,7,3,5,6,2,0,8,1,9]
    k = 6
    # arr = [5]
    # k = 1
    t = Solution()
    print(t.findMaxAverage(arr, k))