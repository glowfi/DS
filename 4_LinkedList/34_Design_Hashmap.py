# https://leetcode.com/problems/design-hashmap/ ,Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(n)


class MyHashMap:
    def __init__(self):
        self.hmap = [-1] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.hmap[key] = value

    def get(self, key: int) -> int:
        return self.hmap[key]

    def remove(self, key: int) -> None:
        self.hmap[key] = -1


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Node:
    def __init__(self, prev=None, next=None, data=[-1, -1]) -> None:
        self.prev = prev
        self.next = next
        self.data = data


class MyHashMap:
    def __init__(self):
        # This will work for large ranges to as we are taking an arbitary sized array
        self.len = 100
        self.hmap = [Node()] * self.len

    def hashFunction(self, key):
        return key % self.len

    def put(self, key: int, value: int) -> None:
        # Get the index to insert a the key,value as DLL node
        idx = self.hashFunction(key)

        # If values are already present then update
        if self.get(key) != -1:
            ptr = self.hmap[idx]
            while ptr:
                if ptr.data[0] == key:
                    ptr.data[1] = value
                    break
                ptr = ptr.next

        # We are yet to insert any value
        # If not present insert key and value
        else:
            ptr = self.hmap[idx]

            if ptr.next is None:
                ptr.next = Node(ptr, None, [key, value])
            else:
                while True:
                    if ptr.next is None:
                        break
                    ptr = ptr.next
                ptr.next = Node(ptr, None, [key, value])

    def get(self, key: int) -> int:
        # Get the index to insert a the key,value as DLL node
        idx = self.hashFunction(key)
        ptr = self.hmap[idx]

        while ptr:
            if ptr.data[0] == key:
                return ptr.data[1]
            ptr = ptr.next
        return -1

    def remove(self, key: int) -> None:
        if self.get(key) != -1:
            # Get the index to insert a the key,value as DLL node
            idx = self.hashFunction(key)
            ptr = self.hmap[idx]

            while ptr:
                if ptr.data[0] == key:
                    # Tail Node
                    if ptr.next is None:
                        ptr.prev.next = None
                        ptr.prev = None
                        break
                    # Normal Node
                    else:
                        ptr.prev.next = ptr.next
                        ptr.next.prev = ptr.prev
                        break

                ptr = ptr.next
