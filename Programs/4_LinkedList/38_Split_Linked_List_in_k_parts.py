# https://leetcode.com/problems/split-linked-list-in-parts/ , Medium


# Optimal
# T.C. - O(n)+O(k*n)
# S.C  - O(1)


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        ans = [None] * k
        if head is None:
            return ans

        n = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            n += 1

        min_nodes_in_each_bucket = n // k
        extra_nodes = n % k

        prev = None
        currHead = head

        for i in range(0, k):
            nodes_to_fill = min_nodes_in_each_bucket
            if extra_nodes > 0:
                nodes_to_fill += 1
                extra_nodes -= 1

            ans[i] = currHead
            for _ in range(nodes_to_fill):
                prev = currHead
                currHead = currHead.next

            prev.next = None

        return ans
