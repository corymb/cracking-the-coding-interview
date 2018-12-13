"""
Check Permutation: Given two strings, write a method to decide if one is a
permutation of the other.

Notes:

Check with interviewer regarding:
  - case sensitivity
  - ASCII or Unicode?
"""

from collections import Counter


# A: O(n)
# W: O(n)
def base_case(a, b):
    return len(a) == len(b) and set(a) == set(b)


# A: O(n log n)
# W: O(n)
def is_permutation(a, b):
    return len(a) == len(b) and sorted(a) == sorted(b)


# A: O(n)
# W: O(n)
def is_permutation_2(a, b):
    return len(a) == len(b) and Counter(a) == Counter(b)
