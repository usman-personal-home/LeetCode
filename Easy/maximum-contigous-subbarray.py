import os
import pprint


def main():
    lst2 = [-2, -3, 4, -1, -2, 1, 5, -3]
    p1 = maxsubarraysum(lst2)
    print(p1)

## Kadane's algorithm
def maxsubarraysum(lst):

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