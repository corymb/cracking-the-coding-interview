"""
URLify: Write a method to replace all spaces in a string with '%20: You may
assume that the string has sufficient space at the end to hold the
additional characters, and that you are given the "true" length of the string.

(Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)

EXAMPLE
Input: "Mr John Smith", 13
Output: "Mr%20John%20Smith"
"""


# A O(n)
# W O(n)
def urlify(text, true_length):
    return text.replace(' ', '%20')


########################################################
# No Character Arrays in Python, so using bytearray(): #
########################################################


# A O(n)
# W O(n)
def urlify2(text, true_length):
    # First pass:
    space_count = sum(1 for c in text if c == ' ') * 2
    # Initialise bytearray with headroom for substitutions:
    substituted_string = bytearray(true_length+space_count)
    # Start at the end:
    i = len(substituted_string) - 1
    for c in text[::-1]:
        if c == ' ':
            substituted_string[i] = ord('0')
            substituted_string[i-1] = ord('2')
            substituted_string[i-2] = ord('%')
            i -= 3
        else:
            substituted_string[i] = ord(c)
            i -= 1
    return substituted_string.decode()
