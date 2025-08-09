# https://leetcode.com/problems/design-hashmap , Easy, Design

# Question
# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]


# Constraints:

# 0 <= key, value <= 10^6
# At most 10^4 calls will be made to put, get, and remove.

# Brute
# T.C. - O(1)
# S.C  - O(10**6)

# Intuition
# Just use a list of size 10**6 and mark everything to -1
# if aksed to add just at that index assign the value
# if aksed to remove at that index mark the value as -1
# if aksed to check if at that index we have value or -1 (-1 signifies absence of value)


class MyHashMap:

    def __init__(self):
        self.map = [-1] * 10**6

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1


# Optimal
# T.C. - O(N)
# S.C  - O(Dynamic_Size)

# Intuition
# Use the concept of chaining on collision
# Resize on increase in load factor


class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key: int = key
        self.val: int = val
        self.next: Node = None


class MyHashMap:

    def __init__(self):
        self.map: list[Node] = [None] * 5
        self.num_items = 0
        self.load_factor = 0.75

    def has_function(self, key: int, size: int) -> int:
        return key % size

    def _resize(self, map: list[Node]) -> list[Node]:
        new_size = len(map) * 2
        new_map: list[Node] = [None] * new_size

        for node in map:
            if node:
                ptr = node
                while ptr:
                    new_map = self._put(ptr.key, ptr.val, new_map)
                    ptr = ptr.next

        return new_map

    def _put(self, key: int, val: int, map: list[Node]) -> list[Node]:
        idx = self.has_function(key, len(map))
        head = map[idx]

        if head is None:
            map[idx] = Node(key, val)
            return map

        ptr = head
        while ptr and ptr.next:
            ptr = ptr.next

        new_entry = Node(key, val)
        ptr.next = new_entry

        return map

    def put(self, key: int, value: int) -> None:
        curr_load_factor = self.num_items // len(self.map)

        if curr_load_factor > self.load_factor:
            self.map = self._resize(self.map)

        contains, found_node = self._contains(key)
        if contains and found_node:
            found_node.val = value
            return

        self.map = self._put(key, value, self.map)

    def get(self, key: int) -> int:
        _, found_node = self._contains(key)
        if found_node:
            return found_node.val
        return -1

    def remove(self, key: int) -> None:
        found, _ = self._contains(key)
        if not found:
            return

        idx = self.has_function(key, len(self.map))
        head = self.map[idx]

        if head.key == key:
            self.map[idx] = head.next
            self.num_items -= 1
            return

        ptr = head
        while ptr:
            if ptr.next.key == key:
                ptr.next = ptr.next.next
                self.num_items -= 1
                return
            ptr = ptr.next

    def _contains(self, key: int) -> tuple[bool, Node | None]:
        idx = self.has_function(key, len(self.map))
        head = self.map[idx]

        if not head:
            return False, None

        ptr = head
        while ptr:
            if ptr.key == key:
                return True, ptr
            ptr = ptr.next

        return False, None
