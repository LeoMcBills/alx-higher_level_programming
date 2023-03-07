#!/usr/bin/python3
def print_last_digit(number):
    list1 = list(str(number))
    num = int(list1[-1])
    print("{}".format(num), end="")
    return num
