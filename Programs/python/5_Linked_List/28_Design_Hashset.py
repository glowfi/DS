# https://leetcode.com/problems/design-hashset, Easy, Design

# Question
# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


# Example 1:

# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)


# Constraints:

# 0 <= key <= 10^6
# At most 10^4 calls will be made to add, remove, and contains.

# Brute
# T.C. - O(1)
# S.C  - O(10**6)

# Intuition
# Just use a list of size 10**6 and mark everything to false
# if aksed to add just mark the index as True
# if aksed to remove mark the index as False
# if aksed to check if it contains a value check at that index is True or not


class MyHashSet:

    def __init__(self):
        self.set = [False] * ((10**6) + 1)

    def add(self, key: int) -> None:
        self.set[key] = True

    def remove(self, key: int) -> None:
        if self.set[key]:
            self.set[key] = False

    def contains(self, key: int) -> bool:
        return self.set[key] == True


# Optimal
# T.C. - O(N)
# S.C  - O(Dynamic_Size)

# Intuition
# Use the concept of chaining on collision
# Resize on increase in load factor


class Node:
    def __init__(self, x: int) -> None:
        self.data: int = x
        self.next: Node = None


class MyHashSet:

    def __init__(self):
        self.set: list[Node] = [None] * 5
        self.num_items = 0
        self.load_factor = 0.75

    def has_function(self, key: int, size: int) -> int:
        return key % size

    def _resize(self, set: list[Node]) -> list[Node]:
        new_size = len(set) * 2
        new_set: list[Node] = [None] * new_size

        for node in set:
            if node:
                ptr = node
                while ptr:
                    new_set = self._add(ptr.data, new_set)
                    ptr = ptr.next

        return new_set

    def _add(self, key: int, set: list[Node]) -> list[Node]:
        idx = self.has_function(key, len(set))
        head = set[idx]

        if head is None:
            set[idx] = Node(key)
            return set

        ptr = head
        while ptr and ptr.next:
            ptr = ptr.next

        new_entry = Node(key)
        ptr.next = new_entry

        return set

    def add(self, key: int) -> None:
        curr_load_factor = self.num_items // len(self.set)

        if curr_load_factor > self.load_factor:
            self.set = self._resize(self.set)

        if self.contains(key):
            return

        self.set = self._add(key, self.set)
        self.num_items += 1

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return

        idx = self.has_function(key, len(self.set))
        head = self.set[idx]

        if head.data == key:
            self.set[idx] = head.next
            self.num_items -= 1
            return

        ptr = head
        while ptr:
            if ptr.next.data == key:
                ptr.next = ptr.next.next
                self.num_items -= 1
                return
            ptr = ptr.next

    def contains(self, key: int) -> bool:
        idx = self.has_function(key, len(self.set))
        head = self.set[idx]

        if not head:
            return False

        ptr = head
        while ptr:
            if ptr.data == key:
                return True
            ptr = ptr.next

        return False
