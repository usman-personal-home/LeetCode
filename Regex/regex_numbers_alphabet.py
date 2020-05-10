import re
import sys



if __name__ == "__main__":
    strs = ["abc cdedede hijkl h3456.678 bbbb"]

    #re1 = re.compile(r"\d+\.\d+") #1234.345
    #re1 = re.compile(r"([a-z0-9]+)")
    #re1 = re.compile(r"\b\w{8}\b")
    re1 = re.compile(r"^(?:\S+\s){2}(\S+)") # third word in a sentence
    re1 = re.compile(r"^\S+\s\S+\s(\S+)")   # third word in a sentence

    for line in strs:
        match = re1.search(line)
        if match:
            print match
            print(match.group())
            print(match.group(1))

    str1 = "Thu Jun 21 13:06:06 PDT 2018"
    re2 = re.compile(r"^(?:\w+\s){1}(\w+)") # month from unix date command
    re2 = re.compile(r"^\w+\s(\w+)")        # month from unix date command
    match = re2.search(str1)
    if match:
        pass
        print(match.group())
        print(match.group(1))

    text = "Clearly, he has no excuse for such behavior dearly."
    re3 = re.compile(r"\w+ly")  # Find Adverbs
    match = re3.findall(text)
    if match:
        pass
        print(match)

