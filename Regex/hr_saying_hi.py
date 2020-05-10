import re
import sys
"""
5
Hi Alex how are you doing - match
hI dave how are you doing
Good by Alex
hidden agenda
Alex greeted Martha
"""

def print_matches(fp):
    regex = re.compile(r"[hH][Ii]\s[^dD]")
    with open(fp, 'r') as file:
        for line in file:
            match = regex.search(line)
            if match:
                #print(line.strip())
                print(match.group())
            else:
                pass


if __name__ == "__main__":

    fp = sys.argv[1]
    print_matches(fp)



