"""
Palindrome Permutation: Given a string, write a function to check if it is a
permutation of a palindrome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of letters. The
palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations:"taco cat'; "atco cta '; etc.)
"""

from collections import Counter
from string import ascii_letters


# A O(n)
# W O(n)
def base_case(xs):
    allowed = set(ascii_letters)
    letters = (x for x in xs if x in allowed)
    return sum(v for v in Counter(letters).values() if v % 2 == 1) < 2


# A O(n)
# W O(n)
def is_palindrome_permutation(xs):
    frequency = {}
    for x in xs:
        c = _get_char_code(x)
        if not c == -1:
            if c in frequency:
                frequency[c] += 1
            else:
                frequency[c] = 1

    found_odd = False
    for v in frequency.values():
        if v % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True


# A O(n)
# W O(n)
def is_palindrome_permutation_2(xs):
    """
    This isn't necessarily more performant because although it avoids the
    second loop, it's still O(n) on account of not being able to avoid
    looking through the whole string.

    TODO: Profile this and previous solution. This might even be slower
    because the optimiser won't be able to unroll the loops.
    """
    frequency = {}
    count_odd = 0
    for x in xs:
        c = _get_char_code(x)
        if not c == -1:
            if c in frequency:
                frequency[c] += 1
            else:
                frequency[c] = 1

            if frequency[c] % 2 == 1:
                count_odd += 1
            else:
                count_odd -= 1
    return count_odd <= 1


# A O(n)
# W O(n)
def is_palindrome_permutation_3(xs):
    """
    'Bit Array' implementation; Still O(n)
    """
    # 27 bit integer:
    count_odd = 1 << 26
    for x in xs:
        c = _get_char_code(x)
        if c > 0:
            count_odd = _flip_bit(count_odd, c)

    # bin(count_odd).count('1') is 1 at initialisation, so decrement popcount:
    return bin(count_odd).count('1') - 1 <= 2


# Helper functions:
def _get_char_code(c):
    """
    Takes character, converts to ascii code and returns integer if input falls
    between A-Z or a-z.

    This is basically Java's Character.getNumericValue() (which is case
    insensitive)

    A or a = 0
    Z or z = 25
    """
    code = ord(c)
    if 65 <= code <= 90:
        return code - ord('A')
    if 97 <= code <= 122:
        return code - ord('a')
    return -1


def _flip_bit(bitarray, index):
    mask = 1 << index
    return bitarray ^ mask
