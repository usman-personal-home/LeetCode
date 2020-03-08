# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from linkedlist import UnorderedList

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        cur = head

        while cur != None:
            print cur.getVal()
            cur = cur.next

        return None

if __name__ == '__main__':
    lo = UnorderedList()
    lo.add(1)
    lo.add(0)
    lo.add(1)
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
    cur = testObj.getDecimalValue(lo.head)
    while cur is not None:
        print(cur.getVal())
        cur = cur.getNext()