# https://www.geeksforgeeks.org/problems/introduction-to-doubly-linked-list/1, Easy, Basic

# Question
# Geek is learning data structures and is familiar with linked lists, but he's curious about how to access the previous element in a linked list in the same way that we access the next element. His teacher explains doubly linked lists to him.

# Given an integer array arr of size n. Construct the doubly linked list from arr and return the head of it.

# Example 1:
# Input:
# n = 5
# arr = [1,2,3,4,5]
# Output:
# 1 2 3 4 5
# Explanation: Linked list for the given array will be 1<->2<->3<->4<->5.

# Example 2:
# Input:
# n = 1
# arr = [1]
# Output:
# 1
# Explanation: Linked list for the given array will be 1.

# Constraints:
# 1 <= n <= 10^5
# 1 <= arr[i] <= 100

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function constructDLL() which takes arr[] as input parameters and returns the head of the Linked List.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# initialize two vars head and curr
# head will be returned as head of final linked list
# create a copy of the head in a curr var which will be used
# to assign the next node,prev node as we iterate over the array
# Traverse through the array and keep making the curr as next node
# to curr


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def constructDLL(self, arr: list[int]) -> Node:
        if not arr:
            return None

        head = Node(arr[0])
        curr = head

        for num in arr[1:]:
            new_node = Node(num)
            new_node.prev = curr
            curr.next = new_node
            curr = curr.next

        return head
