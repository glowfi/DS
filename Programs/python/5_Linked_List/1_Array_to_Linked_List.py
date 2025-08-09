# https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1 , Easy, Basic

# Question
# Given an array of integer arr. Your task is to construct the linked list from arr & return the head of the linked list.

# Examples:

# Input: arr = [1, 2, 3, 4, 5]
# Output: LinkedList: 1->2->3->4->5
# Explanation: Linked list for the given array will be

# Input: arr = [2, 4, 6, 7, 5, 1, 0]
# Output: LinkedList: 2->4->6->7->5->1->0
# Explanation: Linked list for the given array will be

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)

# Constraints:
# 1 <= arr.size() <= 10^6
# 1 <= arr[i] <= 10^6


# Optimal
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# initialize two vars head and curr
# head will be returned as head of final linked list
# create a copy of the head in a curr var which will be used
# to assign the next node as we iterate over the array
# Traverse through the array and keep making the curr as next node
# to curr


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class Solution:
    def constructLL(self, arr: list[int]) -> Node:
        head: Node = Node(-1)
        curr: Node = head

        for num in arr:
            curr.next = Node(num)
            curr = curr.next

        return head.next
