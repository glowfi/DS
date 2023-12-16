# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/ , Hard


# Optimal
# T.C. - O(n)+O(n)+O(nlog(n))
# S.C  - O(n)


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.q = [[root, 0]]
        self.tmp = {}
        self.row = 0

        def bfs():
            while self.q:
                for i in range(len(self.q)):
                    node, col = self.q.pop(0)
                    if col not in self.tmp:
                        self.tmp[col] = [[node.val, self.row]]
                    else:
                        self.tmp[col].append([node.val, self.row])

                    if node.left:
                        self.q.append([node.left, col - 1])

                    if node.right:
                        self.q.append([node.right, col + 1])
                self.row += 1

        bfs()
        ans = []

        # Sort by value adn then by depth
        for i in sorted(self.tmp.items()):
            i[1].sort(key=lambda x: x[0])
            i[1].sort(key=lambda x: x[1])
            tmp = []
            for j in i[1]:
                tmp.append(j[0])
            ans.append(tmp)

        return ans
