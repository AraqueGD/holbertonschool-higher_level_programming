#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return None
    bestKey = sorted(a_dictionary, reverse=True)
    return bestKey[0]
