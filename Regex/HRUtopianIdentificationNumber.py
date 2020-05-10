import re
import sys
"""
2
abc012333ABCDEEEE
0123AB
"""

def print_matches(fp):
    regex = re.compile(r"[a-z]{,3}[0-9]{2,8}[A-Z]{3,}")
    with open(fp, 'r') as file:
        for line in file:
            match = regex.search(line)
            if match:
                #print(line.strip())
                print(match.group())
                print ("valid")
            else:
                print ("invalid")
                pass


if __name__ == "__main__":

    fp = sys.argv[1]
    print_matches(fp)



