import pytest

from chapter_1.e1_hash_table import SimpleHashTable


@pytest.fixture()
def keys():
    return 'key_1 key_2 key_3 key_4 key_5'.split()


@pytest.fixture()
def values():
    return 'value_1 value_2 value_3 value_4 value_5'.split()


@pytest.fixture()
def native_dict(keys, values):
    return dict(zip(keys, values))


@pytest.fixture()
def hash_table(native_dict):
    hash_table = SimpleHashTable()
    for k, v in native_dict.items():
        hash_table[k] = v
    return hash_table


@pytest.fixture()
def single_key_value_pair(keys, values):
    return keys[0], values[0]
