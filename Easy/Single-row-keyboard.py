class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        kb_dict = {}
        for idx in range(len(keyboard)):
           kb_dict[keyboard[idx]] = idx
        print kb_dict

        start_idx = 0
        time = 0
        for i in word:
            time += abs(kb_dict[i] - start_idx)
            start_idx = kb_dict[i]

        return time
if __name__ == '__main__':
    #nums = [3, 6, 1, 0]
    nums = [12, 2, 3, 6]
    keyboard = "abcdefghijklmnopqrstuvwxyz"
    testObj = Solution()
    print(testObj.calculateTime(keyboard, "abce"))