import pytest

from chapter_1.e1_hash_table import (
    DynamicHashTable, SimpleHashTable,
    INITIAL_BUCKET_COUNT, LOAD_FACTOR_THRESHOLD
)


def test_empty_hash_table():
    hash_table = SimpleHashTable()
    assert len(hash_table) == 0


def test_insert(single_key_value_pair):
    hash_table = SimpleHashTable()
    k, v = single_key_value_pair
    hash_table.insert(k, v)
    assert len(hash_table) == 1
    assert k in hash_table.__repr__()
    assert v in hash_table.__repr__()


def test_retrieve(hash_table, single_key_value_pair):
    k, v = single_key_value_pair
    assert hash_table.retrieve(k) == v


def test_object_model_set(single_key_value_pair):
    hash_table = SimpleHashTable()
    key, value = single_key_value_pair
    hash_table[key] = value


def test_object_model_get(hash_table, single_key_value_pair):
    key, value = single_key_value_pair
    assert hash_table[key] == value


def test_key_error(hash_table):
    with pytest.raises(KeyError):
        hash_table['non_existent_key']


def test_initial_bucket_count():
    hash_table = SimpleHashTable()
    assert len(hash_table._buckets) == INITIAL_BUCKET_COUNT


def test_len(hash_table):
    assert len(hash_table) == 5
    for i in range(20):
        hash_table['test_insert_{}'.format(i)] = i
    assert len(hash_table) == 25


def test_iteration(hash_table, keys, values):
    for k, v in hash_table:
        assert k in keys
        assert v in values


def test_raises_stop_iteration():
    with pytest.raises(StopIteration):
        next(_ for _ in SimpleHashTable())


def test_load_factor_starts_at_zero():
    hash_table = DynamicHashTable()
    assert hash_table._load_factor == 0


def test_load_factor_threshold_initialisation():
    hash_table = DynamicHashTable()
    hash_table._load_factor_threshold == LOAD_FACTOR_THRESHOLD


def test_get_load_factor():
    value_count = 5
    hash_table = DynamicHashTable()
    expected_value = round(value_count / INITIAL_BUCKET_COUNT, 2)  # 0.45
    assert hash_table._get_load_factor() == 0.0
    for i in range(value_count):
        hash_table['test_insert_{}'.format(i)] = i
    assert hash_table._get_load_factor() == expected_value


def test_bucket_generation():
    hash_table = DynamicHashTable()
    expected_count = 10
    buckets = hash_table._generate_buckets(expected_count)
    assert len(buckets) == expected_count


def test_rehash_increases_bucket_count(dynamic_hash_table, first_table_primes):
    for i in first_table_primes:
        dynamic_hash_table._rehash()
        assert i == len(dynamic_hash_table._buckets)


def test_length_retained_after_rehash(dynamic_hash_table):
    assert len(dynamic_hash_table) == 5
    dynamic_hash_table._rehash()
    assert len(dynamic_hash_table) == 5


def test_items_retained_after_rehash(dynamic_hash_table, native_dict):
    for k, v in native_dict.items():
        assert dynamic_hash_table[k] == v
    dynamic_hash_table._rehash()
    for k, v in native_dict.items():
        assert dynamic_hash_table[k] == v


# def test_rehash_method_called_after_threshold_breached():
#     pass


def test_prime_list(dynamic_hash_table, first_table_primes):
    primes = list(dynamic_hash_table._primes)
    assert len(primes) == 1225  # number of primes between 11-10,000
    assert primes[:15] == first_table_primes
