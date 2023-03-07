#!/usr/bin/python3
def uppercase(str):
    list1 = list(str)
    for i in list1:
        j = ord(i) - 32
        print("{}".format(chr(j)), end="")
    print("")
