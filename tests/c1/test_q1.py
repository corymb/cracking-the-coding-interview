from hypothesis import given
from hypothesis import strategies as st


@given(st.text())
def test_unique(q1, text):
    expected = len(set(text)) == len(text)
    assert q1(text) == expected
