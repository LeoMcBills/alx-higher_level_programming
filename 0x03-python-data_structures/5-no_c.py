#!/usr/bin/python3
def no_c(my_string):
    new = [i for i in my_string if i != 'c' and i != 'C']
    str = "".join(new)
    return str
