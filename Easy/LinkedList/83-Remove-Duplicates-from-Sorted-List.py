# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from linkedlist import OrderedList
class Solution(object):
    def removeDuplicates(self, li):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = li.head
        while cur.next is not None:

            #Compare the element with the next one
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return li



if __name__ == '__main__':
    lo = OrderedList()
    lo.add(1)
    lo.add(1)
    lo.add(2)
    lo.add(4)
    lo.add(4)
    lo.add(6)
    lo.add(6)
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
    li = testObj.removeDuplicates(lo)
    li.lprint()
