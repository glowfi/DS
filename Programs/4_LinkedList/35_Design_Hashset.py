# https://leetcode.com/problems/design-hashset/description/ , Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(n)


class MyHashSet:
    def __init__(self):
        self.len = (10**6) + 1
        self.hset = [-1] * self.len

    def add(self, key: int) -> None:
        self.hset[key] = key

    def remove(self, key: int) -> None:
        self.hset[key] = -1

    def contains(self, key: int) -> bool:
        if self.hset[key] != -1:
            return True
        return False


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Node:
    def __init__(self, prev=None, next=None, data=-1) -> None:
        self.data = data
        self.prev = prev
        self.next = next


class MyHashSet:
    def __init__(self):
        self.len = 100
        self.hset = [Node()] * self.len

    def hashFunction(self, key):
        return key % self.len

    def add(self, key: int) -> None:
        if not self.contains(key):
            idx = self.hashFunction(key)
            ptr = self.hset[idx]

            # No head node
            if ptr.next is None:
                ptr.next = Node(ptr, None, key)

            else:
                while ptr:
                    if ptr.next is None:
                        break
                    ptr = ptr.next

                ptr.next = Node(ptr, None, key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            idx = self.hashFunction(key)
            ptr = self.hset[idx]

            while ptr:
                if ptr.data == key:
                    # Tail Node
                    if ptr.next is None:
                        ptr.prev.next = None
                        break

                    # Normal Node
                    else:
                        ptr.prev.next = ptr.next
                        ptr.next.prev = ptr.prev
                        break

                ptr = ptr.next

    def contains(self, key: int) -> bool:
        idx = self.hashFunction(key)
        ptr = self.hset[idx]

        while ptr:
            if ptr.data == key:
                return True
            ptr = ptr.next
        return False
