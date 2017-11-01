import pytest

from chapter_1.e1_hash_table import HashTable


def test_empty_hash_table():
    hash_table = HashTable()
    assert len(hash_table) == 0


def test_insert(single_key_value_pair):
    hash_table = HashTable()
    k, v = single_key_value_pair
    hash_table.insert(k, v)
    assert len(hash_table) == 1
    assert k in hash_table.__repr__()
    assert v in hash_table.__repr__()


def test_retrieve(hash_table, single_key_value_pair):
    k, v = single_key_value_pair
    assert hash_table.retrieve(k) == v


def test_object_model_set(single_key_value_pair):
    hash_table = HashTable()
    key, value = single_key_value_pair
    hash_table[key] = value


def test_object_model_get(hash_table, single_key_value_pair):
    key, value = single_key_value_pair
    assert hash_table[key] == value


def test_key_error(hash_table):
    with pytest.raises(KeyError):
        hash_table['non_existent_key']
