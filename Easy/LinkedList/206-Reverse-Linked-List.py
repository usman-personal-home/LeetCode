# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from linkedlist import OrderedList
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head

        # a->b->c
        # c->b->a

        while cur is not None:
            # get a copy of next to set the current value at the end
            next = cur.getNext()

            # set the cur to the previous
            cur.setNext(prev)

            # move previous forward by 1 for next time
            prev = cur

            # move cur by 1
            cur = next

        # set the head of the list
        head = prev

        return head


if __name__ == '__main__':
    lo = OrderedList()
    lo.add(1)
    lo.add(2)
    lo.add(3)
    lo.add(4)
    lo.add(5)
    lo.add(6)
    lo.add(7)
    lo.add(8)
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

    testObj = Solution()
    cur = testObj.reverseList(lo.head)
    while cur is not None:
        print(cur.getVal())
        cur = cur.getNext()
