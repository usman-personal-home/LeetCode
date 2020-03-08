import os
from os.path import basename
import pprint
import random


def main():
    mylist = [1, 11, 3, 5, 4, 6, 7, 10, 9, 8, 12, 13, ]
    new_list = new_bin_search(sorted(mylist), 12)
    print(new_list)
    #list1 = binarySearchIterative(sorted(mylist), 13)
    #print(sorted(mylist))
    #print(list1)

# a[start:end] # items start through end-1
# a[start:]    # items start through the rest of the array
# a[:end]      # items from the beginning through end-1
# a[:]         # a copy of the whole array


def bin_search(alist, item):
    print("\n\n Coming IN")
    print (alist)
    print (len(alist))
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)/2
        print("***********")
        print("item : {}   midpoint : {}  alist[midpoint]: {}".format(item, midpoint, alist[midpoint]))

        if alist[midpoint] == item:
            # If item is st [midpoint] then return True
            return True
        else:
            if item < alist[midpoint]:
                # items start through midpoint-1
                return bin_search(alist[:midpoint], item)
            else:
                # items midpoint + 1 through the rest of the array
                return bin_search(alist[midpoint+1:], item)


def binarySearchIterative(sequence, value):
    lo, hi = 0, len(sequence) - 1
    mid = (lo + hi) // 2
    print(sequence)

    while lo <= hi:
        print("item : {}  low:{}  midpoint : {}  hi: {}  alist[midpoint]: {}".format(value, lo, mid, hi, sequence[mid]))
        mid = (lo + hi) // 2
        print("item : {}   midpoint : {}  alist[midpoint]: {}".format(value, mid, sequence[mid]))
        if sequence[mid] < value:
            lo = mid + 1
        elif sequence[mid] > value:
            hi = mid - 1
        else:
            return mid

    return None


def new_bin_search(lst, target):
    if len(lst) == 0:
        return False
    else:
        mid = len(lst)/2
        if lst[mid] == target:
            return True

        else:
            if lst[mid] > target:
                return new_bin_search(lst[:mid], target)
            else:
                return new_bin_search(lst[mid + 1:], target)


    """
        found = False
    end = len(alist) - 1
    mid = len(alist) // 2
    start = 0

    while start < end and not found:
        print("\n\n Coming IN")
        print("Start:{}  End:{}  Mid:{}".format(start, end, mid))
        print(alist)
        mid = (start + end) / 2
        print("Start:{}  End:{}  Mid:{}".format(start, end, mid))
        if alist[mid] == item:
            found = True
        elif item < alist[mid]:
            end = mid
        else:
            start = mid + 1

    return found

    """



def binarySearchIndex():
    pass

if __name__ == '__main__':
    main()


