# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from linkedlist import OrderedList
from linkedlist import UnorderedList

from Node import Node

class Solution(object):
    def merge2sortedlists(self, li, lj):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prehead = Node(-1)
        prev = prehead

        while li is not None and lj is not None:

            # add the elements as per the values from l1 and l2
            if li.val <= lj.val:
                prev.next = li
                li = li.next
            else:
                prev.next = lj
                lj = lj.next

            # Increment previous to keep 1 step behind the current list
            prev = prev.next

        # append the non-empty list to prev
        print(type(li))
        print(type(lj))
        prev.next = li if li is not None else lj

        return prehead.next



if __name__ == '__main__':
    lo = OrderedList()
    lo.add(1)
    lo.add(2)
    lo.add(4)

    l1 = OrderedList()
    l1.add(1)
    l1.add(3)
    l1.add(4)

    print("***********************")
    #lo.lprint()
    print("***********************")
    #print(lo.search(40))
    print("***********************")
    #print(lo.search(8))
    #print(lo.size())
    #lo.lprint()
    #print(lo.toArray())
    print("***********************")

    testObj = Solution()
    cur = testObj.merge2sortedlists(lo.head, l1.head)
    li = UnorderedList()

    li.head = cur
    li.lprint()
