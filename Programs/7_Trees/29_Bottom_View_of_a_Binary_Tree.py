# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1 , Medium


# Optimal
# T.C. - O(n)+O(nlog(n))+O(n)
# S.C  - O(n)


class Solution:
    def bottomView(self, root):
        self.q = [[root, 0]]
        self.tmp = {}
        self.row = 0

        def bfs():
            while self.q:
                for i in range(len(self.q)):
                    node, col = self.q.pop(0)
                    if col not in self.tmp:
                        self.tmp[col] = [[self.row, node.data]]
                    else:
                        self.tmp[col] = [[self.row, node.data]]

                    if node.left:
                        self.q.append([node.left, col - 1])

                    if node.right:
                        self.q.append([node.right, col + 1])
                self.row += 1

        bfs()
        ans = []

        for i in sorted(self.tmp.items()):
            ans.append(i[1][0][1])

        return ans
