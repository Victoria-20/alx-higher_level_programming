#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    list_cop = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return list_cop
    else:
        list_cop[idx] = element
    return (list_cop)
