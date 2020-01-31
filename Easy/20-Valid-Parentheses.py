class Solution(object):

    def bracket_match(self, a, b):
        if a == '{' and b == '}':
            return True
        if a == '(' and b == ')':
            return True
        if a == '[' and b == ']':
            return True

        return False



    def isValid(self, expr):
        my_stack = []
        for i in expr:
            if i == '(' or i == '[' or i == '{':
                my_stack.append(i)
            elif i == '}' or i == ')' or i == ']':
                if len(my_stack) == 0:
                    return False
                a = my_stack.pop()
                if self.bracket_match(a,i):
                    continue
                else:
                    return False

        if len(my_stack) > 0:
            return False

        return True


if __name__ == '__main__':
    A = "{()[]{}}"

    testObj = Solution()
    print(testObj.isValid(A))