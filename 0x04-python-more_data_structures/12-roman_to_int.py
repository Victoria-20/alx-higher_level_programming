#!/usr/bin/python3


def roman_to_int(roman_string):
    roman_string = roman_string.upper()
    rom_dict = {'M': 1000, 'D': 500, 'C': 100,
                'L': 50, 'X': 10, 'V': 5, 'I': 1}
    int_sum = 0

    if roman_string is None or type(roman_string) != str:
        return 0
    else:
        for i in range(len(roman_string)):
            if i > 0 and rom_dict[roman_string[i]] > rom_dict[roman_string[i - 1]]:
                int_sum += rom_dict[roman_string[i]] - 2 * rom_dict[roman_string[i - 1]]
            else:
                int_sum += rom_dict[roman_string[i]]
        return int_sum
