# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from linkedlist import OrderedList
from linkedlist import UnorderedList

from Node import Node

class Solution(object):
    def hasCycle(self, head, pos):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print slow.getVal()
                print fast.getVal()
                bool = True
        """
        # To find the start of the loop.
        if (bool) {
            count = 0;
            temp = head;
             while (temp != slow) {
                temp = temp.next;
                slow = slow.next;
        count++;
             }
            return count;
        }
        """
        return False

    def hashhasCycle(self, head, pos):
        """
        :type head: ListNode
        :rtype: bool
        """
        dic = {}
        while head:
            if head in dic:
                print dic
                return True
            dic[head] = 0
            head = head.next
        return False

if __name__ == '__main__':
    lo = UnorderedList()
    lo.add(4)
    lo.add(0)
    lo.add(2)
    lo.add(3)
    n1 = None
    n2 = None
    cur = lo.head
    while cur is not None:
        if cur.getVal() == 4:
            n1 = cur
        elif cur.getVal() == 2:
            n2 = cur
        cur = cur.next

    # Extension:

    n1.setNext(n2)
    l1 = UnorderedList()
    l1.add(4)
    l1.add(0)
    l1.add(2)
    l1.add(3)
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
    cur = testObj.hasCycle(lo.head, 2)
    print(cur)

