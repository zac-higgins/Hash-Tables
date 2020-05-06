class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, storage):
        self.storage = [None] * storage
        self.capacity = len(self.storage)
        self.total_items = 0
        self.load_factor = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        bytes_representation = key.encode()
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        FNV_size = 2**64
        for byte in bytes_representation:
            hval = (FNV_offset_basis * FNV_prime) % FNV_size
            hval = hval ^ byte
        return hval

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value, manual=False):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        if node is None:
            self.storage[index] = HashTableEntry(key, value)
            self.total_items += 1
        elif node is not None:
            if node.key != key:
                while node.next is not None:
                    if node.key != key:
                        node = node.next
                    else:
                        node.value = value
                if node.key == key:
                    node.value = value
                else:
                    node.next = HashTableEntry(key, value)
                    self.total_items += 1
            else:
                node.value = value
        if manual == False:
            self.auto_resize()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if self.get(key) is not None:
            index = self.hash_index(key)
            node = self.storage[index]
            while node.next is not None:
                if node.key == key:
                    node.key = node.next.key
                    node.value = node.next.value
                    node.next = node.next.next
                    self.total_items -= 1
                    return
                else:
                    node = node.next
            if node.key == key:
                node.key = None
                node.value = None
                node.next = None
                self.total_items -= 1
            else:
                return None
        else:
            return None
        self.auto_resize()

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        if node is not None:
            while node.next is not None:
                if node.key == key:
                    return node.value
                else:
                    node = node.next
            if node.key == key:
                    return node.value
            else:
                return None
        else:
            return None

    def resize(self, new_capacity, manual):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        temp_storage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * new_capacity
        for item in temp_storage:
            if item is not None:
                if item.next is not None:
                    while item.next is not None:
                        # print(item.key, item.value, "-->", item.next.key, item.next.value)
                        self.put(item.key, item.value, manual)
                        item = item.next
                    self.put(item.key, item.value, manual)
                elif item.next is None:
                    # print(item.key, item.value, "-->", item.next)
                    self.put(item.key, item.value, manual)

    def auto_resize(self):
        self.load_factor = self.total_items / self.capacity
        # print("load factor on put: ", self.load_factor)
        if self.load_factor > 0.7:
            self.resize(self.capacity * 2, False)
            # print("bigger resize happened! ", self.capacity)
        elif self.load_factor < 0.2:
            new_size = self.capacity // 2
            if new_size > 8:
                self.resize(new_size, False)
                # print("smaller resize happened! ", self.capacity)
            elif new_size <= 8:
                self.resize(8, False)
                # print("smaller resize happened! ", self.capacity)

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test overwriting
    # print("")
    # ht.put("line_3", "this is the new value!")
    # print("is it the new value? ", ht.get("line_3"))

    # # Test resizing
    print("-----")
    old_capacity = len(ht.storage)
    ht.resize(4)
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # print("----")
    # # ht.delete("line_3")
    # print("delete")
    # print("----")

    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    print("")
