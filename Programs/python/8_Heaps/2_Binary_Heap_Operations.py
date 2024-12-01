# https://www.geeksforgeeks.org/problems/operations-on-binary-min-heap/1 , Medium


# Optimal
# T.C. - getMin:O(1) insert:O(log(n)) removeMin:O(log(n))
# S.C  - O(n)

heap = []
curr_size = 0


def getParentIndex(index) -> int:
    return (index - 1) // 2


def getLeftChildIndex(index) -> int:
    return (2 * index) + 1


def getRightChildIndex(index) -> int:
    return (2 * index) + 2


def hasParent(index) -> bool:
    return getParentIndex(index) >= 0


def hasLeftChild(index) -> bool:
    return getLeftChildIndex(index) < curr_size


def hasRightChild(index) -> bool:
    return getRightChildIndex(index) < curr_size


def parent(index) -> int:
    return heap[getParentIndex(index)]


def leftChild(index) -> int:
    return heap[getLeftChildIndex(index)]


def rightChild(index) -> int:
    return heap[getRightChildIndex(index)]


def swap(index1, index2) -> None:
    heap[index1], heap[index2] = (
        heap[index2],
        heap[index1],
    )


def heapifyUp(lastInsertedIdx):
    if not hasParent(lastInsertedIdx):
        return

    parentIdx = getParentIndex(lastInsertedIdx)
    if heap[parentIdx] < heap[lastInsertedIdx]:
        return

    swap(lastInsertedIdx, parentIdx)
    heapifyUp(parentIdx)


# Function to insert a value in Heap.
def insertKey(x):
    global curr_size

    heap[curr_size] = x
    heapifyUp(curr_size)
    curr_size += 1


def heapifyDown(index):
    left_child = getLeftChildIndex(index)
    right_child = getRightChildIndex(index)
    smallest = index

    if hasLeftChild(index) and heap[left_child] < heap[smallest]:
        smallest = left_child

    if hasRightChild(index) and heap[right_child] < heap[smallest]:
        smallest = right_child

    if smallest != index:
        swap(smallest, index)
        heapifyDown(smallest)
    else:
        return


# Function to delete a key at ith index.
def deleteKey(i):
    global curr_size

    if i >= curr_size:
        return -1

    swap(i, curr_size - 1)
    curr_size -= 1
    heapifyUp(i)
    heapifyDown(i)


# Function to extract minimum value in heap and then to store
# next minimum value at first index.
def extractMin():
    if curr_size == 0:
        return -1

    min_num = heap[0]
    deleteKey(0)
    return min_num
