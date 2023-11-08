#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    max_key = None
    for key, value in a_dictionary.items():
        if value > score:
            score = value
            max_key = key
    if max_key is not None:
        return max_key
    else:
        return None
            