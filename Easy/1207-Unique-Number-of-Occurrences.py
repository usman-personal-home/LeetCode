import collections

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool

        Counter({1: 3, 2: 2, 3: 1})
        3
        3
        True
        """
        c = collections.Counter(arr)
        print c
        print(len(c))
        print(c.values())
        print(len(set(c.values())))
        # Compare the keys of the dictionary, with set(unique) values
        return len(c) == len(set(c.values()))


if __name__ == '__main__':

    nums = [1,2,2,1,1,3]
    testObj = Solution()
    print(testObj.uniqueOccurrences(nums))