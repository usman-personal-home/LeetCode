import re

def main():
    fh = open("simpsons_phone_book.txt")
    for line in fh:
        if re.search(r"J.*Neu",line):
            #print line.rstrip()
            pass
    fh.close()


    l = ["555-8396 Neu, Allison",
         "Burns, C. Montgomery",
         "555-5299 Putz, Lionel",
         "555-7334 Simpson, Homer Jay"]

    for i in l:
        res = re.search(r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)", i)
        print (res.group(3) + " " + res.group(2) + " " + res.group(1))


if __name__ == '__main__':
    main()