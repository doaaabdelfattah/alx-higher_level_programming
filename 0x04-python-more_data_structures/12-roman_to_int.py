#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    result = 0
    if isinstance(roman_string, str) and roman_string is not None:
        for i in range(len(roman_string)):
            value = roman_num[roman_string[i]]
            if i < len(roman_string) - 1 and \
                    roman_num[roman_string[i + 1]] > value:
                result -= value
            else:
                result += value

        return result
    else:
        return 0
