import os
import pprint


def main():
    lst2 = [-2,1,-3,4,-1,2,1,-5,4]
    p1 = maxsubarraysum(lst2)
    print(p1)
    """
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    """


def maxsubarraysum(nums):
    n = len(nums)
    curr_sum = max_sum = nums[0]
    for i in range(1, n):
        if curr_sum + nums[i] > nums[i]:
            curr_sum += nums[i]
        else:
            curr_sum = nums[i]
        #curr_sum = max(nums[i], curr_sum + nums[i])

        max_sum = max(max_sum, curr_sum)
        # print curr_sum
        # print max_sum
        # print("######")

    return max_sum
## Kadane's algorithm- Dynamic Programming
def maxsubarraysumK(lst):

    current_max = 0
    max_so_far = 0

    for i in range(len(lst)):
        current_max += lst[i]

        if current_max > max_so_far:
            max_so_far = current_max

        if current_max < 0:
            current_max = 0

    return max_so_far



if __name__ == '__main__':
    #print("hello")
    main()