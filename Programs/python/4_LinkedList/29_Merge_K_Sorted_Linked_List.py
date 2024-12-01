# https://leetcode.com/problems/merge-k-sorted-lists/ , Hard


# Optimal
# T.C. -> O(nlog(k))
# S.C. -> O(total nodes present)


class Solution:
    def merge2sortedList(self, l1, l2):
        p1, p2 = l1, l2
        curr = dummy = ListNode(-1)
        # print(p1.val,p2.val)

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            else:
                curr.next = p2
                p2 = p2.next
                curr = curr.next

        if p1:
            curr.next = p1

        if p2:
            curr.next = p2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        while len(lists) != 1:
            tmp = self.merge2sortedList(lists[0], lists[1])
            lists.pop(0)
            lists.pop(0)
            lists.insert(0, tmp)

        ans = lists[0]
        return ans
