# NA , Medium

# Brute [Iterative]
# T.C. - getMin:O(1) insert:O(log(n)) removeMin:O(log(n))
# S.C  - O(n)


class MinHeap:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.storage = [0] * capacity
        self.size = 0

    def getParentIndex(self, index) -> int:
        return (index - 1) // 2

    def getLeftChildIndex(self, index) -> int:
        return (2 * index) + 1

    def getRightChildIndex(self, index) -> int:
        return (2 * index) + 2

    def hasParent(self, index) -> bool:
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index) -> bool:
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index) -> bool:
        return self.getRightChildIndex(index) < self.size

    def parent(self, index) -> int:
        return self.storage[self.getParentIndex(index)]

    def leftChild(self, index) -> int:
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self, index) -> int:
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self) -> bool:
        return self.size == self.capacity

    def isEmpty(self) -> bool:
        return self.size == 0

    def swap(self, index1, index2) -> None:
        self.storage[index1], self.storage[index2] = (
            self.storage[index2],
            self.storage[index1],
        )

    def heapifyUp(self, lastInsertedIdx) -> None:
        lastInsertedVal = self.storage[lastInsertedIdx]
        while True:
            parentIdx = self.getParentIndex(lastInsertedIdx)
            if (
                self.hasParent(lastInsertedIdx)
                and self.storage[parentIdx] > lastInsertedVal
            ):
                self.swap(lastInsertedIdx, parentIdx)
                lastInsertedIdx = parentIdx
            else:
                break

    def heapifyUpRecursive(self, lastInsertedIdx) -> None:
        if not self.hasParent(lastInsertedIdx):
            return

        parentIdx = self.getParentIndex(lastInsertedIdx)
        if self.storage[parentIdx] < self.storage[lastInsertedIdx]:
            return

        self.swap(lastInsertedIdx, parentIdx)
        self.heapifyUpRecursive(parentIdx)

    def insert(self, data: int) -> None:
        if self.isFull():
            return

        self.storage[self.size] = data
        self.heapifyUp(self.size)
        self.size += 1

    def getMin(self) -> int:
        if self.isEmpty():
            return -1
        return self.storage[0]

    def heapifyDown(self, idx):
        while idx < self.size:
            left_child = self.getLeftChildIndex(idx)
            right_child = self.getRightChildIndex(idx)
            smallest = idx

            if (
                self.hasLeftChild(idx)
                and self.storage[left_child] < self.storage[smallest]
            ):
                smallest = left_child

            if (
                self.hasRightChild(idx)
                and self.storage[right_child] < self.storage[smallest]
            ):
                smallest = right_child

            if smallest != idx:
                self.swap(smallest, idx)
                idx = smallest
            else:
                break

    def heapifyDownRecursive(self, idx):
        left_child = self.getLeftChildIndex(idx)
        right_child = self.getRightChildIndex(idx)
        smallest = idx

        if self.hasLeftChild(idx) and self.storage[left_child] < self.storage[smallest]:
            smallest = left_child

        if (
            self.hasRightChild(idx)
            and self.storage[right_child] < self.storage[smallest]
        ):
            smallest = right_child

        if smallest != idx:
            self.swap(smallest, idx)
            self.heapifyDownRecursive(smallest)
        else:
            return

    def removeMin(self) -> None:
        if self.isEmpty():
            return

        # swap first and last inserted
        self.swap(0, self.size - 1)
        self.size -= 1
        self.heapifyDown(0)

    def remove(self, idx):
        self.swap(idx, self.size - 1)
        self.size -= 1
        self.heapifyUp(idx)
        self.heapifyDown(idx)
