# https://leetcode.com/problems/merge-k-sorted-lists/ , Hard


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Better
# T.C. -  O(N*(k(k+1))/2)
# S.C  - O(1)


class Solution:
    def merge2sortedLinkedList(self, a: ListNode, b: ListNode) -> ListNode:
        i, j = a, b
        final_head = final = ListNode(-1)

        while i and j:
            if i.val <= j.val:
                final.next = i
                final = final.next
                i = i.next
            else:
                final.next = j
                final = final.next
                j = j.next

        if i:
            final.next = i

        if j:
            final.next = j

        return final_head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        merged_list_head = lists[0]

        for idx in range(1, len(lists)):
            merged_list_head = self.merge2sortedLinkedList(merged_list_head, lists[idx])

        return merged_list_head


# Optimal
# T.C. - O(k*log(k)+(k*n)*3*log(n))
# S.C  - O(k)

# Analysis -> Nodes gets replaced so reuse old nodes,All the nodes first elemnts will hold the first min value

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, list in enumerate(lists):
            if list:
                heappush(heap, (list.val, i, list))

        dummy = curr = ListNode(-1)
        while heap:
            _, i, smallest_node = heapq.heappop(heap)
            if smallest_node.next:
                heapq.heappush(heap, (smallest_node.next.val, i, smallest_node.next))
            curr.next = smallest_node
            curr = curr.next

        return dummy.next
