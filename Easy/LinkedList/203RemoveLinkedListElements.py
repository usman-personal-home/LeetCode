

from linkedlist import UnorderedList
from Node import Node

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        sentinel = Node(0)
        sentinel.next = head
        prev, cur = sentinel, head

        while cur is not None:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        # The sentinel is a dummy node, sentinel.head will actually return the
        return sentinel.next


if __name__ == '__main__':
    lo = UnorderedList()

    lo.add(6)
    lo.add(3)
    lo.add(4)
    lo.add(5)
    lo.add(6)
    lo.add(2)
    lo.add(6)
    lo.add(6)
    lo.add(6)
    print("***********************")
    #lo.lprint()
    print("***********************")
    print(lo.search(40))
    print("***********************")
    #print(lo.search(8))
    #print(lo.size())
    lo.lprint()
    print(lo.toArray())
    print("***********************")
    to_remove = 6
    testObj = Solution()
    cur = testObj.removeElements(lo.head, to_remove)
    while cur is not None:
        print(cur.getVal())
        cur = cur.getNext()