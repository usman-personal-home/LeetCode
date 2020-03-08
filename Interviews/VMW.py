# "" Valid
# "ab" Valid
# "abab" or "aabb" Valid
# "ababab" or "aabbab" or "aaabbb" or "abaabb" Valid
# "abba" Invalid
#
# 1. Always start with empty string ""
# 2. Go on inserting 'ab' as a single unit into existing string, "ab" is atomic (not 'a' or 'b' or 'ba')
# 3. "ab" can go anywhere in existing string
#
# "aabbbaab" Invalid
#
# Write a function
# boolean isValid(String)
# returns true for a valid string
#         false otherwise
# abab

class Test(object):

    # without extra space
    def isValid2(self, S):
        # Empty string
        if len(S) == 0:
            return True

        # If a or b is missing completely
        if S.count('a') == 0 or S.count('b') == 0:
            return False

        # If there is unequal number of a' and b's
        if S.count('a') != S.count('b'):
            return False

        a_count = 0
        b_count = 0
        for i in range(len(S)):
            if S[i] == 'a':
                a_count += 1
            elif S[i] == 'b':
                b_count += 1
            if a_count < b_count:
                return False

        return True


    def isValid(self, S):

        # Empty string
        if len(S) == 0:
            return True

        # If a or b is missing completely
        if S.count('a') == 0 or S.count('b') == 0:
            return False

        # If there is unequal number of a' and b's
        if S.count('a') != S.count('b'):
            return False

        # Create a stack for a's, pop if you see a b
        res_stack = []

        for i in range(len(S)):
            if S[i] == 'a':
                res_stack.append(S[i])
            elif S[i] == 'b' and res_stack:
                res_stack.pop(-1)
        print res_stack

        # Check if the size of the stack is 0
        if len(res_stack) == 0:
            return True

        return False


if __name__ == '__main__':

    st1 = "aabb"
    testObj = Test()
    print(testObj.isValid2(st1))