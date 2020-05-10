class Solution(object):

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Fib(0) = 0
        # Fib(1) = 1
        # Fib(2) = 0 + 1
        # Input to the fib function      = 0,1,2,3,4,5,6
        # Fib(N)                         = 0,1,1,2,3,5,8
        if N == 0:
            return 0
        if N == 1:
            return 1

        return self.fib(N - 1) + self.fib(N - 2)


    # Computes value of first
    # fibonacci numbers
    # Fib(0) = 0
    # Fib(1) = 1
    # Fib(2) = 0 + 1
    # N      = 0,1,2,3,4,5,6
    # Fib(N) = 0,1,1,2,3,5,8

    # Calculate the sum to fib(N)
    def calculateFibSum(self, n):

        if n <= 0:
            return 0

        fibo = [0] * (n + 1)
        fibo[1] = 1

        # Initialize result
        # sm = 0
        sm = fibo[0] + fibo[1]

        # Add remaining terms
        for i in range(2, n + 1):
            # Storing the last 2 sum values in fib[i] for next time
            fibo[i] = fibo[i - 1] + fibo[i - 2]
            sm = sm + fibo[i]
        print fibo

        return sm

    # print the nth term in the seq, not fib(N)
    # Fib(0) = 0
    # Fib(1) = 1
    # Fib(2) = 0 + 1
    # Input to the fib function      = 0,1,2,3,4,5,6
    # Fib(N)                         = 0,1,1,2,3,5,8
    def printnthfib(self, nth):
        n1,n2 = 0,1
        count = 0
        if nth == 1:
            print(0)
        elif nth == 2:
            print(1)
        else:
            while count < n:
                print n1
                #print n2
                nterm = n1 + n2
                #print nterm
                print

                # update values
                n1 = n2
                n2 = nterm
                count += 1

    def printFibSeq(self, nterms):
        # first two terms
        n1, n2 = 0, 1
        count = 0

        # check if the number of terms is valid
        if nterms <= 0:
            print("Please enter a positive integer")
        elif nterms == 1:
            print("Fibonacci sequence upto " +str(nterms) + " :")
            print(n1)
        else:
            print("Fibonacci sequence:")
            while count < nterms:
                # start from 0
                print(n1)

                # fib(n)
                nth = n1 + n2

                # update values increment n1 to n2
                n1 = n2

                # incremnt n2 to fib(n)
                n2 = nth

                count += 1


if __name__ == '__main__':
    testObj = Solution()
    sum = 0
    for i in range(5):
        sum += testObj.fib(i)

    print sum
    # above function
    n = 4
    #print("Sum of Fibonacci numbers is : ",
    #      testObj.calculateFibSum(n))

    #
    #testObj.printnthfib(n)