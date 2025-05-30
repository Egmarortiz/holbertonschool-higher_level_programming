#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for ch in reversed(roman_string):
        value = roman_map.get(ch)
        if value is None:
            # Invalid character → abort
            return 0
        # If a smaller value precedes a larger one, subtract it
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value

    return total
