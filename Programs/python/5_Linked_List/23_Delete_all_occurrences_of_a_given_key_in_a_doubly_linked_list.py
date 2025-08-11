# https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1, Medium, Task

# Question
# You are given the head_ref of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key if it is present and return the new DLL.

# Example1:

# Input:
# 2<->2<->10<->8<->4<->2<->5<->2
# 2
# Output:
# 10<->8<->4<->5
# Explanation:
# All Occurences of 2 have been deleted.

# Example2:

# Input:
# 9<->1<->3<->4<->5<->1<->8<->4
# 9
# Output:
# 1<->3<->4<->5<->1<->8<->4
# Explanation:
# All Occurences of 9 have been deleted.
# Your Task:

# Complete the function void deleteAllOccurOfX(struct Node** head_ref, int key), which takes the reference of the head pointer and an integer value key. Delete all occurrences of the key from the given DLL.

# Expected Time Complexity: O(N).

# Expected Auxiliary Space: O(1).

# Constraints:

# 1<=Number of Nodes<=10^5

# 0<=Node Value <=10^9


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# First delete all starting nodes if have they have x
# then keep deleting the nodes with x


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def deleteAllOccurOfX(self, head: Node, x: int) -> Node:
        # Handle edge case where list is empty
        if not head:
            return head

        # Traverse the list
        ptr = head
        while ptr.data == x:
            ptr = ptr.next
            head = ptr

        while ptr:
            savedNxt = ptr.next

            # If the current node's data matches x
            if ptr.data == x:
                if ptr and ptr.prev:
                    ptr.prev.next = ptr.next

                if ptr and ptr.next:
                    ptr.next.prev = ptr.prev

            ptr = savedNxt

        return head
