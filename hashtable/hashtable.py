class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.keys_count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.keys_count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        pass

        # Your code here
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037
        hash = offset_basis
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for char in key:
            hash = (hash * 33) + ord(char)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value, changing_size=False):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Day 1
        # index = self.hash_index(key)
        # self.bucket[index] = value

        # Day 2

        index = self.hash_index(key)

        current = self.storage[index]
        if current == None:
            self.storage[index] = HashTableEntry(key, value)
            if not changing_size:
                self.keys_count += 1
        else:
            while current is not None:
                if current.key == key:
                    current.value = value
                    break
                if current.next == None:
                    current.next = HashTableEntry(key, value)
                    if not changing_size:
                        self.keys_count += 1
                    break
                current = current.next
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # Day 1
        # index = self.hash_index(key)
        # self.bucket[index] = None

        #  Day 2

        index = self.hash_index(key)

        if self.storage[index].key == key:
            self.storage[index] = self.storage[index].next
            self.keys_count -= 1
        else:

            current = self.storage[index]
            while True:
                if current.next.key == key:
                    current.next = current.next.next
                    self.keys_count -= 1
                    break
                elif current.next:
                    current = current.next
                else:
                    print("Not found")
                    break

        if self.get_load_factor() < 0.2:
            new_capacity = max(self.capacity // 2, 8)
            self.resize(new_capacity)

        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # Day 1
        # index = self.hash_index(key)
        # return self.bucket[index]

        #  Day 2

        index = self.hash_index(key)

        current = self.storage[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return current

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        #  Day 2

        old_storage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        for current in old_storage:
            while current:
                self.put(current.key, current.value, True)
                current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
