import pytest

from src.c1.q1 import is_unique, is_unique_2, is_unique_3
from src.c1.q2 import is_permutation, is_permutation2, is_permutation3
from src.c1.q3 import urlify, urlify2
from src.c1.q4 import (
    is_palindrome_permutation,
    is_palindrome_permutation2,
    is_palindrome_permutation3,
    is_palindrome_permutation4
)


@pytest.fixture(params=(is_unique, is_unique_2, is_unique_3))
def q1(request):
    return request.param


@pytest.fixture(params=(is_permutation, is_permutation2, is_permutation3))
def q2(request):
    return request.param


@pytest.fixture(params=(urlify, urlify2))
def q3(request):
    return request.param


@pytest.fixture(params=(is_palindrome_permutation,
                is_palindrome_permutation2,
                is_palindrome_permutation3,
                is_palindrome_permutation4))
def q4(request):
    return request.param
