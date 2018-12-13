from hypothesis import given
from hypothesis import strategies as st

from src.c1.q2 import base_case


@given(st.text(), st.text())
def test_is_permutation(q2, text1, text2):
    expected = base_case(text1, text2)
    assert q2(text1, text2) == expected
