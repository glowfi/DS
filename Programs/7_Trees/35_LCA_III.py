# NA , Medium

# Nodes have parent now

# Better
# T.C. - O(2n)
# S.C  - O(n)


class Solution:
    def lca(self, p, q):
        seen = set()

        while p:
            seen.add(p.val)
            p = p.parent

        while q:
            if q.val in seen:
                return q
            q = q.parent


# Optimal
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def lca(self, p, q):
        p_copy = p
        q_copy = q

        while p_copy != q_copy:
            if not p_copy:
                p_copy = q
            else:
                p_copy = p_copy.parent

            if not q_copy:
                q_copy = p
            else:
                q_copy = q_copy.parent

        return p_copy
