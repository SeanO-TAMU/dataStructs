class HashMap:
    #if you implement in C you need to keep track of size of list/bucket size and potentially resize
    def __init__(self, capacity):

        self.capacity = capacity # of buckets
        self.size = 0 # of elements in hashMap
        self.buckets = [[] for _ in range(capacity)]

    # O(1) - constant time
    def __len__(self):
        return self.size

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def __contains__(self, key):
        index = self._hash_function(key)

        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True
        
        return False

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def put(self, key, value):
        index = self._hash_function(key)

        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1
        
    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def get(self, key):
        index = self._hash_function(key)

        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError("Key not found")

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def remove(self, key):
        index = self._hash_function(key)

        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return

        raise KeyError("Key not found")

    # O(n) - linear time
    def keys(self):
        #return all keys in map
        keys = []
        for i in self.buckets:
            for k, v in i:
                keys.append(k)
        
        return keys
    
    # O(n) - linear time
    def values(self):
        #return all values in map
        values = []
        for i in self.buckets:
            for k, v in i:
                values.append(v)
        
        return values

    # O(n) - linear time
    def items(self):
        #return all (key, value) pairs in map
        keyVal = []
        for i in self.buckets:
            for k, v in i:
                keyVal.append((k, v))
        
        return keyVal

    # O(k) - linear in key length/dependent on key length (practically O(1))
    def _hash_function(self, key): #underscore in front signifies it as private to the developer
        
        key_string = str(key)
        hash_result = 0

        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity

        return hash_result

if __name__ == '__main__':

    hash_map = HashMap(10)

    print("---- TEST: put() and get() ----")
    hash_map.put("apple", 1)
    hash_map.put("banana", 2)
    hash_map.put("cat", 3)

    print(hash_map.get("apple"))   # EXPECT 1
    print(hash_map.get("banana"))  # EXPECT 2
    print(hash_map.get("cat"))     # EXPECT 3

    print("\n---- TEST: override existing key ----")
    hash_map.put("apple", 99)
    print(hash_map.get("apple"))   # EXPECT 99

    print("\n---- TEST: __contains__ ----")
    print("apple" in hash_map)     # EXPECT True
    print("dog" in hash_map)       # EXPECT False

    print("\n---- TEST: remove() ----")
    hash_map.remove("banana")
    print("banana" in hash_map)    # EXPECT False

    try:
        hash_map.remove("banana")  # EXPECT KeyError
    except KeyError:
        print("KeyError caught correctly for remove()")

    print("\n---- TEST: keys() ----")
    print(hash_map.keys())         # EXPECT something like ["apple", "cat"]

    print("\n---- TEST: values() ----")
    print(hash_map.values())       # EXPECT [99, 3]

    print("\n---- TEST: items() ----")
    print(hash_map.items())        # EXPECT [("apple", 99), ("cat", 3)]

    print("\n---- TEST: Multiple collisions ----")
    # Force collisions by giving all keys the same hash bucket
    collision_map = HashMap(2)
    collision_map.put("x", 10)
    collision_map.put("y", 20)
    collision_map.put("z", 30)
    

    print(collision_map.items())   # EXPECT all pairs stored in the same bucket

    print("\n---- ALL TESTS COMPLETED ----")

