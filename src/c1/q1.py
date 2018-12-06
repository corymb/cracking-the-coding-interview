"""
Is Unique: Implement an algorithm to determine if a string has all
unique characters. What if you cannot use additional data structures?
"""

from itertools import tee


# A O(n)
def is_unique(xs):
    return True if len(set(xs)) == len(xs) else False


############################
# Without Data Structures: #
############################


# A O(n²)
def is_unique_2(xs):
    for i, c in enumerate(xs):
        if c in xs[:i] or c in xs[i+1:]:
            return False
    return True


# A: O(n log n) for sort, O(n) for check
# W: O(n log n) for sort, O(n) for check
def is_unique_3(xs):
    for x, y in _pairwise(sorted(xs)):
        if x == y:
            return False
    return True


# Helper function:
def _pairwise(xs):
    a, b = tee(xs)
    next(b, None)
    return zip(a, b)
