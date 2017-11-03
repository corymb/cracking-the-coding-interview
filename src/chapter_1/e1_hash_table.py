import math
from itertools import dropwhile


INITIAL_BUCKET_COUNT = 11
LOAD_FACTOR_THRESHOLD = 0.75


class SimpleHashTable:
    def __init__(self):
        self._buckets = [[] for x in range(INITIAL_BUCKET_COUNT)]

    def __len__(self):
        return len([i for b in self._buckets for i in b if i])

    def __repr__(self):
        return '{}'.format([i for b in self._buckets for i in b if i])

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.retrieve(key)

    def __iter__(self):
        return (i.split(':')[1:] for b in self._buckets for i in b if i)

    def insert(self, key, value):
        bucket = hash(key) % len(self._buckets)
        self._buckets[bucket].append('{0}:{1}:{2}'.format(
            hash(key), key, value))

    def retrieve(self, key):
        bucket = hash(key) % len(self._buckets)
        for item in self._buckets[bucket]:
            if item.startswith(str(hash(key))):
                __, __, v = item.split(':')
                return v
        raise KeyError

class DynamicHashTable(SimpleHashTable):
    """
    Dynamically resizing Hash Table

    - Recalculates buckets and redistributes once load factor is too high
    - Leverages prime numbers to improve hash distribution
    - Constant time look up (average case)
    - Linear time look up (worst case) on rebalance
    """
    def __init__(self):
        super().__init__()
        self._load_factor = 0
        self._load_factor_threshold = LOAD_FACTOR_THRESHOLD
        # Get prime after INITIAL_BUCKET_COUNT:
        self._primes = (i for i in range(INITIAL_BUCKET_COUNT, 10000)
            if all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)))

    def _get_load_factor(self):
        return round(len(self) / len(self._buckets), 2)

    def _generate_buckets(self, count):
        return [[] for _ in range(count)]

    def _rehash(self):
        items = (i for i in self)
        self._buckets = self._generate_buckets(next(self._primes))
        for k, v in items:
            self.insert(k, v)
