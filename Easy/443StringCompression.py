
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # Anchor is the starting of a new character sequence 
        anchor = write = 0
        new_chars = []
        for i, c in enumerate(chars):
            # all changes happen when the char changes
            if i  == len(chars) - 1 or chars[i + 1] != c:
                chars[write] = chars[anchor]
                # increment write index in the array
                write += 1
                if i > anchor:
                    for digit in str(i - anchor + 1):
                        chars[write] = digit
                        write += 1
                # change the anchor to the new character
                anchor = i + 1
        print chars
        return write

if __name__ == '__main__':
    address = ["a","a","b","b","c","c","c"]
    testObj = Solution()
    print(testObj.compress(address))
