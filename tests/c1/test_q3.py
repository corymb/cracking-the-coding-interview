from hypothesis import given
from hypothesis import strategies as st

from src.c1.q3 import base_case


# Ascii only
@given(st.text(st.characters(max_codepoint=127)))
def test_urlify(q3, text):
    expected = base_case(text, len(text))
    assert q3(text, len(text)) == expected
