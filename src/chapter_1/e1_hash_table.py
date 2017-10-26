
class HashTable:
    def __init__(self):
        self.buckets = [[] for x in range(11)]

    def __len__(self):
        return len([b for b in self.buckets if b])

    def __repr__(self):
        return '{}'.format([b for b in self.buckets if b])

    def insert(self, key, value):
        bucket = hash(key) % len(self.buckets)
        self.buckets[bucket].append('{0}:{1}:{2}'.format(
            hash(key), key, value))
