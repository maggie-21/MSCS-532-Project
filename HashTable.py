# Hash Table class for the Product Catalog
class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        self.table[key] = value

    def search(self, key):
        # Retrieve the value associated with the key
        return self.table.get(key, None)

    def delete(self, key):
        # Delete a key-value pair from the hash table
        if key in self.table:
            del self.table[key]
