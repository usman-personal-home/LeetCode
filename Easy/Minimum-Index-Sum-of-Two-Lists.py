import sys
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        rlist = []
        rdict = {}

        for i,r in enumerate(list1):
            rdict[r] = i

        best = sys.maxint
        for i,r in enumerate(list2):
            if r in rdict:
                cur_best = i + rdict[r]
                print cur_best
                if best > cur_best:
                    best = cur_best
                    rlist = [r]
                elif best == cur_best:
                    rlist.append(r)
        return rlist


if __name__ == '__main__':
    A = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    B = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

    testObj = Solution()
    print(testObj.findRestaurant(A,B))