#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    max_key = None
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > score:
                score = a_dictionary[key]
                max_key = key
    return max_key
