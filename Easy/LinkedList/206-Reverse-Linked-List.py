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
        cur = head
        prev = None

        while cur is not None:
            # Save a copy of next
            next = cur.next

            # set previous to the next 0f current
            cur.next = prev

            # increment previous for next time
            prev = cur

            # increment cur
            cur = next

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
    print(testObj.reverseList(lo.head))
