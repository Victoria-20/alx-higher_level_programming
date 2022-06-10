#!/usr/bin/python3


def weight_average(my_list=[]):
    sum = 0
    weighted_sum = 0

    if my_list:
        for i in my_list:
            sum = sum + i[0] * i[1]
            weighted_sum = weighted_sum + i[1]
        return sum / weighted_sum
    else:
        return 0
