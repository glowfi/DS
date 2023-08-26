# https://leetcode.com/problems/copy-list-with-random-pointer/description/, Medium


# Better
# T.C. -> O(n)+O(n)
# S.C. -> O(n)


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        newList = cp = Node(-1)
        copy = {None: None}

        ptr = head
        while ptr:
            copy[ptr] = Node(ptr.val, None, None)
            ptr = ptr.next

        ptr = head
        while ptr:
            copy[ptr].random = copy[ptr.random]
            copy[ptr].next = copy[ptr.next]
            cp.next = copy[ptr]
            cp = cp.next
            ptr = ptr.next

        return newList.next


# Optimal
# T.C. -> O()
# S.C. -> O()


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        pass
