import pytest

from src.c1.q1 import is_unique, is_unique_2
from src.c1.q2 import is_permutation, is_permutation_2
from src.c1.q3 import urlify
from src.c1.q4 import (
    is_palindrome_permutation,
    is_palindrome_permutation_2,
    is_palindrome_permutation_3,
)


@pytest.fixture(params=(is_unique, is_unique_2))
def q1(request):
    return request.param


@pytest.fixture(params=(is_permutation, is_permutation_2))
def q2(request):
    return request.param


@pytest.fixture(params=(urlify,))
def q3(request):
    return request.param


@pytest.fixture(params=(is_palindrome_permutation,
                is_palindrome_permutation_2,
                is_palindrome_permutation_3))
def q4(request):
    return request.param
