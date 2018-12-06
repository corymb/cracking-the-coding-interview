import pytest

from src.c1.q1 import is_unique, is_unique_2, is_unique_3


@pytest.fixture(params=(is_unique, is_unique_2, is_unique_3))
def q1(request):
    return request.param
