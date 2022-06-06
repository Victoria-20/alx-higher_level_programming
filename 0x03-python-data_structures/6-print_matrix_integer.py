#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    len_f_element = len(matrix[0])
    if len_f_element != 0:
        for items in matrix:
            for i in range(len_f_element - 1):
                print("{:d}".format(items[i]), end=" ")
            print("{:d}".format(items[len_f_element - 1]))
    else:
        print("")
