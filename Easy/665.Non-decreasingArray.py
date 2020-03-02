class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        count = 0
        j = 1
        anchor = 1
        found = False
        for i in range(len(nums) - 1):
            if arr[i] > arr[i + 1]
                if i > 0:
                    if (arr[i - 1] <= arr[i + 1])
                        arr[i] = arr[i - 1];
                else
                        arr[i + 1] = arr[i];
                count + +;
                if (count > 1)
                    return false;
                }
            }


        print count
        return count <= 1
        """

if __name__ == '__main__':
    nums = [3, 4,2]
    testObj = Solution()
    print(testObj.checkPossibility(nums))
