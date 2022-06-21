#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for element in my_list[0:x]:
            print(element, end="")
            num = num + 1

    except IndexError:
        print("")
    print()
    return num
