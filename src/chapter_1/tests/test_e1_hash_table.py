from chapter_1.e1_hash_table import HashTable

def test_hash_table():
    assert HashTable()

def test_empty_hash_table():
    hash_table = HashTable()
    assert len(hash_table) == 0
