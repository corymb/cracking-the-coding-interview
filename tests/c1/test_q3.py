from hypothesis import given
from hypothesis import strategies as st


# Ascii only
@given(st.text(st.characters(max_codepoint=127)))
def test_urlify(q3, text):
    expected = text.replace(' ', '%20')
    assert q3(text, len(text)) == expected
