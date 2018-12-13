from collections import Counter
from string import ascii_letters

from hypothesis import example, given
from hypothesis import strategies as st


# Limit to ASCII:
@given((st.characters(max_codepoint=127)))
@example('racecar')
@example('not palindrome permutation')  # TODO: wtf hypothesis?
@example('non%$#@^%$pali')
@example('55rfsjdoig0^%$#WYH-pali')
@example('')
def test_is_palindrome_permutation(q4, text):
    allowed = set(ascii_letters)
    letters = (c for c in text if c in allowed)
    expected = sum(v for v in Counter(letters).values() if v % 2 == 1) < 2
    assert q4(text) == expected
