# NA , Medium

# Optimal
# T.C. - heapify_from_array O(n), percolate_up O(log(n)), percolate_down O(log(n)),
# increase_key O(log(n)), decrease_key O(log(n)), insert_key O(log(n)), extract_max O(log(n))
# delete_key O(log(n) + log(n)) = O(2log(n)) = O(log(n))
# S.C  - O(n)

import math


class MinHeap:
    """
    MinHeap Implementation
    """

    def __init__(self, height):
        """
        Initialize the MinHeap with a given height.

        Args:
            height (int): The height of the MinHeap.
        """
        self.max_heap_size = (2 ** (height + 1)) - 1
        self.curr_size = 0
        self.heap_arr = [None] * self.max_heap_size

    def heapify_from_array(self, arr):
        """
        Heapify the array and return the heapified array.

        Args:
            arr (list): The input array to be heapified.

        Returns:
            list: The heapified array.
        """
        if len(arr) > self.max_heap_size:
            raise Exception("Array size exceeds the maximum heap size")

        self.heap_arr[: len(arr)] = arr
        self.curr_size = len(arr)
        last_internal_node_idx = math.floor(self.curr_size / 2) - 1

        for i in range(last_internal_node_idx, -1, -1):
            self.percolate_down_recursive(i)

        return self.heap_arr[: self.curr_size]

    def percolate_up(self, idx):
        """
        Percolate up the element at the given index.

        Args:
            idx (int): The index of the element to be percolated up.
        """
        if idx < 0 or idx >= self.curr_size:
            raise Exception("Index out of range")
        self.percolate_up_recursive(idx)

    def percolate_up_recursive(self, idx):
        """
        Recursively percolate up the element at the given index.

        Args:
            idx (int): The index of the element to be percolated up.
        """
        if idx > 0:
            parent_idx = math.floor((idx - 1) / 2)
            if self.heap_arr[parent_idx] > self.heap_arr[idx]:
                self.heap_arr[parent_idx], self.heap_arr[idx] = (
                    self.heap_arr[idx],
                    self.heap_arr[parent_idx],
                )
                self.percolate_up_recursive(parent_idx)

    def percolate_down(self, idx):
        """
        Percolate down the element at the given index.

        Args:
            idx (int): The index of the element to be percolated down.
        """
        if idx < 0 or idx >= self.curr_size:
            raise Exception("Index out of range")
        self.percolate_down_recursive(idx)

    def percolate_down_recursive(self, idx):
        """
        Recursively percolate down the element at the given index.

        Args:
            idx (int): The index of the element to be percolated down.
        """
        lc_idx = 2 * idx + 1
        rc_idx = 2 * idx + 2

        smallest_idx = idx

        if lc_idx < self.curr_size and self.heap_arr[lc_idx] < self.heap_arr[idx]:
            smallest_idx = lc_idx

        if (
            rc_idx < self.curr_size
            and self.heap_arr[rc_idx] < self.heap_arr[smallest_idx]
        ):
            smallest_idx = rc_idx

        if smallest_idx != idx:
            self.heap_arr[idx], self.heap_arr[smallest_idx] = (
                self.heap_arr[smallest_idx],
                self.heap_arr[idx],
            )
            self.percolate_down_recursive(smallest_idx)

    def insert_key(self, key):
        """
        Insert a new key into the MinHeap.

        Args:
            key (int): The key to be inserted.
        """
        if self.curr_size == self.max_heap_size:
            raise Exception("Heap is full")
        self.heap_arr[self.curr_size] = key
        self.percolate_up_recursive(self.curr_size)
        self.curr_size += 1

    def increase_key(self, idx, key):
        """
        Increase the key at the given index.

        Args:
            idx (int): The index of the key to be increased.
            key (int): The new key value.
        """
        if idx < 0 or idx >= self.curr_size:
            raise Exception("Index out of range")
        if key < self.heap_arr[idx]:
            raise Exception("New key is smaller than the current key")
        self.heap_arr[idx] = key
        self.percolate_up_recursive(idx)

    def decrease_key(self, idx, key):
        """
        Decrease the key at the given index.

        Args:
            idx (int): The index of the key to be decreased.
            key (int): The new key value.
        """
        if idx < 0 or idx >= self.curr_size:
            raise Exception("Index out of range")
        if key > self.heap_arr[idx]:
            raise Exception("New key is larger than the current key")
        self.heap_arr[idx] = key
        self.percolate_down_recursive(idx)

    def extract_min(self):
        """
        Extract the minimum element from the MinHeap.

        Returns:
            int: The minimum element.
        """
        if self.curr_size == 0:
            raise Exception("Heap is empty")
        min_elem = self.heap_arr[0]
        self.heap_arr[0] = self.heap_arr[self.curr_size - 1]
        self.curr_size -= 1
        self.percolate_down_recursive(0)
        return min_elem

    def delete_key(self, idx):
        """
        Delete the key at the given index.

        Args:
            idx (int): The index of the key to be deleted.
        """
        if idx < 0 or idx >= self.curr_size:
            raise Exception("Index out of range")
        self.heap_arr[idx] = float("-inf")
        self.percolate_up_recursive(idx)
        self.extract_min()


# Create a MinHeap with a height of 3
min_heap = MinHeap(3)

# Insert keys into the MinHeap
min_heap.insert_key(20)
min_heap.insert_key(10)
min_heap.insert_key(15)
min_heap.insert_key(30)
min_heap.insert_key(25)

# Print the MinHeap array
print("MinHeap array:", min_heap.heap_arr[: min_heap.curr_size])

# Extract the minimum element from the MinHeap
min_elem = min_heap.extract_min()
print("Extracted minimum element:", min_elem)

# Print the MinHeap array after extraction
print("MinHeap array after extraction:", min_heap.heap_arr[: min_heap.curr_size])

# Decrease a key in the MinHeap
min_heap.decrease_key(2, 5)
print("MinHeap array after decreasing key:", min_heap.heap_arr[: min_heap.curr_size])

# Increase a key in the MinHeap
min_heap.increase_key(2, 35)
print("MinHeap array after increasing key:", min_heap.heap_arr[: min_heap.curr_size])

# Delete a key from the MinHeap
min_heap.delete_key(2)
print("MinHeap array after deleting key:", min_heap.heap_arr[: min_heap.curr_size])

# Heapify an array
arr = [10, 20, 15, 30, 25]
min_heap.heapify_from_array(arr)
print("Heapified array:", min_heap.heap_arr[: min_heap.curr_size])
