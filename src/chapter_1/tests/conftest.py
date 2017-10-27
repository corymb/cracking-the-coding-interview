import pytest


@pytest.fixture()
def keys():
    return 'key_1 key_2 key_3 key_4 key_5'.split()

@pytest.fixture()
def values():
    return 'value_1 value_2 value_3 value_4 value_5'.split()

@pytest.fixture()
def test_dict(keys, values):
    return dict(zip(keys, values))

@pytest.fixture()
def single_key_value_pair(keys, values):
    return keys[0], values[0]


