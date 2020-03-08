class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ind1, ind2 = -1, -1
        min_distance = len(self.words)

        for i, word in enumerate(self.words):
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

    # Your WordDistance object will be instantiated and called as such:
    obj = WordDistance(words)
    param_1 = obj.shortest(word1,word2)
    print param_1