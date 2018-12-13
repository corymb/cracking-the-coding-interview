from hypothesis import given
from hypothesis import strategies as st


@given(st.text(), st.text())
def test_is_permutation(q2, text1, text2):
    expected = sorted(text1) == sorted(text2)
    assert q2(text1, text2) == expected
