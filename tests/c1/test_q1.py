from hypothesis import given
from hypothesis import strategies as st

from src.c1.q1 import base_case


@given(st.text())
def test_unique(q1, text):
    expected = base_case(text)
    assert q1(text) == expected
