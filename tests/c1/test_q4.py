from hypothesis import example, given
from hypothesis import strategies as st

from src.c1.q4 import base_case


# Limit to ASCII:
@given((st.characters(max_codepoint=127)))
@example('racecar')
@example('not palindrome permutation')  # TODO: wtf hypothesis?
@example('non%$#@^%$pali')
@example('55rfsjdoig0^%$#WYH-pali')
@example('')
def test_is_palindrome_permutation(q4, text):
    expected = base_case(text)
    assert q4(text) == expected
