INITIAL_BUCKET_COUNT = 11


class SimpleHashTable:
    def __init__(self):
        self._buckets = [[] for x in range(INITIAL_BUCKET_COUNT)]

    def __len__(self):
        return len([b for b in self._buckets if b])

    def __repr__(self):
        return '{}'.format([b for b in self._buckets if b])

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.retrieve(key)

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
