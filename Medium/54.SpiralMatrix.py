class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        res = []
        r = 0
        r1 = len(matrix) - 1    # 3
        c = 0
        c1 = len(matrix[0]) - 1  # 3
        while r <= r1 and c <= c1:

            # going from c to c1:  1 2 3  -> top row
            for i in range(c, c1 + 1):
                print("Appending : " + str(matrix[r][i]) + "    Row : " + str(r) + " Col :" + str(i))
                res.append(matrix[r][i])
            print

            # going from r+1 to r1: 6 9  -> right column
            for j in range(r + 1, r1 + 1):
                print("Appending : " + str(matrix[j][c1]) + "     Row : " + str(j) + " Col :" + str(c1))
                res.append(matrix[j][c1])
            print

            if r < r1 and c < c1:
                # going from c1 -1  to c+1 -> bottom row
                for j in range(c1 - 1, c, -1):
                    print("Appending : " + str(matrix[r1][j]) + "     Row : " + str(r1) + " Col :" + str(j))
                    res.append(matrix[r1][j])
                print

                # going from r1 to r+1 -> left column
                for j in range(r1, r, -1):
                    print("Appending : " + str(matrix[j][c]) + "     Row : " + str(j) + " Col :" + str(c))
                    res.append(matrix[j][c])
                print

            r += 1
            r1 -= 1
            c += 1
            c1 -= 1

        return res
        

if __name__ == '__main__':

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    matrix = [[3],
              [2]]

    testObj = Solution()
    print(testObj.spiralOrder(matrix))

    for i in range(0,1):
        print "hello"
