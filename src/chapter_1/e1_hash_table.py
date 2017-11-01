
class HashTable:
    def __init__(self):
        self.buckets = [[] for x in range(11)]

    def __len__(self):
        return len([b for b in self.buckets if b])

    def __repr__(self):
        return '{}'.format([b for b in self.buckets if b])

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.retrieve(key)

    def insert(self, key, value):
        bucket = hash(key) % len(self.buckets)
        self.buckets[bucket].append('{0}:{1}:{2}'.format(
            hash(key), key, value))

    def retrieve(self, key):
        bucket = hash(key) % len(self.buckets)
        for item in self.buckets[bucket]:
            if item.startswith(str(hash(key))):
                __, __, v = item.split(':')
                return v
        raise KeyError
