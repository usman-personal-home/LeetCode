if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8]

    # includes first number, less than the last number
    print a
    # [1, 2, 3, 4, 5, 6, 7, 8]
    print a[:]
    # [1, 2, 3, 4, 5, 6, 7, 8]

    print a[1:4]
    # [2, 3, 4]

    print a[::-1]
    # [8, 7, 6, 5, 4, 3, 2, 1]

    print a[1:]
    # [2, 3, 4, 5, 6, 7, 8]

    print a[:len(a) - 1]
    # [1, 2, 3, 4, 5, 6, 7]

    print a[1:7]
    # [2, 3, 4, 5, 6, 7]