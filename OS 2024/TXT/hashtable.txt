class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return ord(key[0]) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value
        print(f"Inserted {value} at position {index}")

    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]

    def delete(self, key):
        index = self.hash_function(key)
        self.table[index] = None
        print(f"Deleted value at position {index}")

hash_table = HashTable(10)

hash_table.insert("apple", 10)
hash_table.insert("banana", 20)

print("Get 'apple':", hash_table.get("apple"))
print("Get 'banana':", hash_table.get("banana"))

hash_table.delete("apple")
print("Get 'apple' after deletion:", hash_table.get("apple"))
