#!/usr/bin/python3


def roman_to_int(roman_string):
    base_rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 100}
    int_string = ''

    for i in roman_string:
        int_string += str(base_rom_dict[i])
    return int(int_string)
