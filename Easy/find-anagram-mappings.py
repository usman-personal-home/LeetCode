class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = []
        d = {}
        for i,b in enumerate(B):
            if b not in d:
                d[b] = []
            d[b].append(i)
        print d
        for i,a in enumerate(A):
            print d[a]
            res.append(d[a].pop())


        return res


if __name__ == '__main__':
    A = [12, 28, 46, 32, 50, 32]
    B = [32, 50, 12, 32, 46, 28]

    testObj = Solution()
    print(testObj.anagramMappings(A, B))