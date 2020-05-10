
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        ["a","a","b","b","c","c","c"]
        ["a","2","b","2","c","3"]
        """
        write = 0
        read = 0
        for i,c in enumerate(chars):
            if i == len(chars) - 1 or chars[i+1] != c:
                # all changes happen when the char changes
                chars[write] = chars[read]
                # increment write index in the array
                write += 1
                if i > read:
                    for c in str(i - read + 1):
                        chars[write] = c
                        write += 1

                # change the anchor to the new character
                read = i + 1

        return chars















        # Anchor is the starting of a new character sequence 
        anchor = write = 0
        new_chars = []
        for i, c in enumerate(chars):
            # all changes happen when the char changes
            if i == len(chars) - 1 or chars[i + 1] != c:
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
    address = ["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]
    testObj = Solution()
    print(testObj.compress(address))
