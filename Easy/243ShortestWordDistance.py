class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ind1, ind2 = -1, -1
        min_distance = len(words)

        for i, word in enumerate(words):
            if word == word1:
                ind1 = i
            elif word == word2:
                ind2 = i

            # Check if both indices have been set at least once
            if ind1 != -1 and ind2 != -1:
                min_distance = min(min_distance, abs(ind1 - ind2))
        return min_distance


if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    testObj = Solution()
    print(testObj.shortestDistance(words, word1, word2))
