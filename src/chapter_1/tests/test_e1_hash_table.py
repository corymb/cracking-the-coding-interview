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
