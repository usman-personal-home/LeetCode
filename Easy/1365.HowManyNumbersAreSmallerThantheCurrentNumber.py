class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {}
        sort_nums = sorted(nums)

        # just storing the first occourance of element in sorted list
        for i, num in enumerate(sort_nums):
            #count.setdefault(num, i)
            if num not in count:
                count[num] = i
        print count
        res = []
        for i in nums:
            res.append(count[i])

        return res

    def bruteSmallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [None] * len(nums)
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] > nums[j]:
                    counter += 1
            res[i] = counter
        return res


if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    testObj = Solution()
    print(testObj.smallerNumbersThanCurrent(nums))
