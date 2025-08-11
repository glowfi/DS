# https://leetcode.com/problems/lru-cache, Medium, Design

# Question
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.


# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4


# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 105 calls will be made to get and put.

# Brute
# T.C. - O(N^2)
# S.C  - O(N)

# Intuition
# Maintain a list to store the LRU cache
# Store the recently used in front
# When getting,push the element to get to the
# front and when pushing,push the element to
# the front,if max capacity reached delete the
# end node,if key already exists replace the
# existing value


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.max_cap = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            k, v = self.cache[i][0], self.cache[i][1]
            if k == key:
                self.cache = self.cache[:i] + self.cache[i + 1 :]
                self.cache.insert(0, [k, v])
                return v
        return -1

    def put(self, key: int, value: int) -> None:
        # if key already exits
        for i in range(len(self.cache)):
            k = self.cache[i][0]
            if k == key:
                self.cache = self.cache[:i] + self.cache[i + 1 :]
                break

        # Evict if max cap reached
        if len(self.cache) >= self.max_cap:
            self.cache.pop()

        self.cache.insert(0, [key, value])


# Optimal
# T.C. - O(1)
# S.C  - O(N)

# Intuition
# We will use a combination of a doubly linked list (DLL) and a hash map (dictionary) to implement the LRU Cache.
# The DLL will allow us to maintain the order of usage, while the hash map will provide O(1) access to the nodes.
# We will have a head and a tail node to facilitate easy insertion and deletion of nodes.


class Node:
    def __init__(self, k: int, v: int) -> None:
        self.key = k  # The key of the node
        self.val = v  # The value of the node
        self.prev: Node | None = None  # Pointer to the previous node
        self.next: Node | None = None  # Pointer to the next node


class DLL:
    def __init__(self) -> None:
        # Initialize the doubly linked list with a head and a tail node
        self.head: Node = Node(-1, -1)  # Dummy head node
        self.tail: Node = Node(-1, -1)  # Dummy tail node
        self.head.next = self.tail  # Head points to tail
        self.tail.prev = self.head  # Tail points back to head

    def insert_after_head(self, node: "Node|None") -> None:
        # Insert a node right after the head
        if not node:
            return

        head_next = self.head.next  # Get the current first node after head

        # Adjust pointers to insert the new node
        head_next.prev = node
        node.next = head_next
        self.head.next = node
        node.prev = self.head

    def delete_node(self, node: "Node|None") -> None:
        # Remove a node from the DLL
        if not node:
            return

        next_node = node.next  # Get the next node
        prev_node = node.prev  # Get the previous node

        # Adjust pointers to bypass the node being deleted
        next_node.prev = prev_node
        prev_node.next = next_node

        # Clear the pointers of the deleted node
        node.next = None
        node.prev = None

    def get_tail(self) -> Node | None:
        # Return the last node before the tail
        return self.tail.prev

    def get_head(self) -> Node | None:
        # Return the first node after the head
        return self.head.next


class LRUCache:
    def __init__(self, capacity: int):
        self.max_cap = capacity  # Maximum capacity of the cache
        self.curr_cap = 0  # Current capacity of the cache
        self.cache: dict[int, Node] = {}  # Hash map to store key-node pairs
        self.dll = DLL()  # Initialize the doubly linked list

    def make_recently_use(self, key: int):
        # Move the accessed node to the front (after head) to mark it as recently used
        node = self.cache[key]  # Get the node from the cache
        self.dll.delete_node(node)  # Remove it from its current position
        self.dll.insert_after_head(node)  # Insert it after the head

    def get(self, key: int) -> int:
        # Retrieve the value for the given key
        if key not in self.cache:
            return -1  # Return -1 if the key is not found

        self.make_recently_use(key)  # Mark the node as recently used
        return self.cache[key].val  # Return the value of the node

    def put(self, key: int, value: int) -> None:
        # Insert or update the value for the given key
        if key in self.cache:
            self.cache[key].val = value  # Update the value
            self.make_recently_use(key)  # Mark it as recently used
            return

        if self.curr_cap >= self.max_cap:
            # Evict the least recently used node if the cache is full
            node = self.dll.get_tail()  # Get the last node before the tail
            self.dll.delete_node(node)  # Remove it from the DLL
            del self.cache[node.key]  # Remove it from the cache
            self.curr_cap -= 1  # Decrement the current capacity

        # Insert the new node
        new_node = Node(key, value)  # Create a new node
        self.cache[key] = new_node  # Add it to the cache
        self.dll.insert_after_head(new_node)  # Insert it after the head
        self.curr_cap += 1  # Increment the current capacity
