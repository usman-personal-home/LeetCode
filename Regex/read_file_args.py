"""
read raw input

"""

import sys
#sys.stdin.readlines()

def read_file(fp):
    with open(fp, 'r') as file:
        lines = file.readlines()

    for line in lines:
        print(line.strip())

def read_file2(fp):
    with open(fp, 'r') as file:
        for line in file:
            print(line.strip())

def read_file3(fp):
    with open(fp, 'r') as file:
        data = file.read()
        print(type(data))
        print data

def read_file4(fp):
        file = open(fp, 'r')
        data = file.read()
        print(type(data))
        lst =  data.split("\n")
        print(lst)

if __name__ == "__main__":
    fp = sys.argv[1]
    print(fp)
    read_file4(fp)