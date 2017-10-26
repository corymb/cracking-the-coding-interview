from chapter_1.e1_hash_table import HashTable


def test_empty_hash_table():
    hash_table = HashTable()
    assert len(hash_table) == 0


def test_insert():
    hash_table = HashTable()
    hash_table.insert('test', 5)
    assert len(hash_table) == 1
    assert 'test' in hash_table.__repr__()
    assert str(5) in hash_table.__repr__()
