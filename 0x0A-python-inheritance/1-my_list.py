#!/usr/bin/python3


class MyList(list):
    def print_sorted(self):
        list.sort(reverse = False)
        print(list)
