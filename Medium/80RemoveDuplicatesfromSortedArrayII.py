class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize the counter and the second pointer.
        j, count = 1, 1

        # Start from the second element of the array and process
        # elements one by one.
        for i in range(1, len(nums)):

            # If the current element is a duplicate,
            # increment the count.
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                # Reset the count since we encountered a different element
                # than the previous one
                count = 1

            # For a count <= 2, we copy the element over thus
            # overwriting the element at index "j" in the array
            if count <= 2:
                print("Index i " + str(i) + " Index j " + str(j))
                print("Copying " + str(nums[i]) + " to " + str(nums[j]))
                print("######")
                print nums
                nums[j] = nums[i]
                print nums
                print
                print("######")
                j += 1

        print nums
        return j

    def removeD(self, nums):

        return j

if __name__ == '__main__':
    nums = [1,1,1,2,3]
    testObj = Solution()
    print(testObj.removeDuplicates(nums))