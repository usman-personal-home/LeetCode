# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from linkedlist import OrderedList
class Solution(object):
    def merge2sortedlists(self, li, lj):
        """
        :type head: ListNode
        :rtype: ListNode
        """





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
    print(lo.search(40))
    print("***********************")
    #print(lo.search(8))
    #print(lo.size())
    lo.lprint()
    print(lo.toArray())
    print("***********************")

    testObj = Solution()
    li = testObj.merge2sortedlists(lo, l1)
    li.lprint()
