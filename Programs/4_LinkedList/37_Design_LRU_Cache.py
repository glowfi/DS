# https://leetcode.com/problems/lru-cache/ ,Medium


# Optimal
# T.C. -> O()
# S.C. -> O()


class Node:
    def __init__(self, prev=None, next=None, data=[-1, -1]):
        self.prev = prev
        self.next = next
        self.data = data


class LRUCache:
    def __init__(self, capacity: int):
        self.mp = {}
        self.currcap = 0
        self.cap = 0
        self.head = Node()

    def get(self, key: int) -> int:
        ptr = self.head
        while ptr:
            if ptr.data[0] == key:
                # Tail node
                if ptr.next is None:
                    ptr.prev.next = None
                    ptr.next = self.head
                    ptr.prev = None
                    self.head = ptr
                    return self.mp[ptr.data[0]]

                # Normal node
                else:
                    ptr.prev.next = ptr.next
                    ptr.next.prev = ptr.prev
                    ptr.prev = None
                    ptr.next = self.head
                    self.head = ptr
                    return self.mp[ptr.data[0]]
            ptr = ptr.next

        return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.mp[key] = value
            return

        if self.currcap > self.cap:
            ptr = self.head
            while True:
                if ptr.next is None:
                    del self.mp[ptr.data[0]]
                    ptr.prev.next = None
                    self.currcap -= 1
                    break
                ptr = ptr.next

        ptr = self.head

        if ptr.next is None:
            ptr.next = Node(ptr, None, [key, value])
        else:
            while True:
                if ptr.next is None:
                    ptr.next = Node(ptr, None, [key, value])
                    self.mp[key] = value
                    break
                ptr = ptr.next
