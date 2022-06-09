#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        key = ""
        max_score = 0

        for k in a_dictionary.keys():
            if a_dictionary[k] > max_score:
                key = k
                max_score = a_dictionary[k]
        return(key)
    else:
        return(None)
