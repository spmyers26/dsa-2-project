# hashtable.py

class HashTable:
    def __init__(self, initial_capacity=10):
        # create a list of lists
        self.num_nodes = 0
        self.OPTIMAL_LOAD_FACTOR = 1
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        # get bucket
        bucket = self.simple_hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update item if key is already in the bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # append item to bucket list if key not already in bucket
        key_value = [key, item]
        bucket_list.append(key_value)

        # resize if load factor exceeds 1
        self.num_nodes = self.num_nodes + 1
        if self.num_nodes / len(self.table) > self.OPTIMAL_LOAD_FACTOR:
            self.resize()

        return True

    def search(self, key):
        # gets appropriate bucket
        bucket = self.simple_hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for key in bucket
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]

    def remove(self, key):
        # get appropriate bucket
        bucket = self.simple_hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove key-value pair
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    def resize(self):
        # create new table with twice the current capacity
        new_table = []
        current_capacity = len(self.table)
        for i in range(current_capacity * 2):
            new_table.append([])

        # copy key-value pairs into newly hashed buckets
        for bucket_list in self.table:
            for kv in bucket_list:
                bucket = self.simple_hash(kv[0]) % len(new_table)
                new_table[bucket].append([kv[0], kv[1]])

        # replace current table with new table, delete new table
        self.table = new_table
        del new_table

    def simple_hash(self, key):
        return key % len(self.table)
