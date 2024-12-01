# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/ , Hard

# Brute [bfs]
# T.C. - O(n)+O(n)
# S.C  - O(n)+O(n)+O(n)+O(n)

from collections import deque


class Codec:
    def serialize(self, root):
        if not root:
            return ""

        q = deque([[root, 0]])
        val, ind = [], []

        while q:
            for i in range(len(q)):
                node, idx = q.popleft()
                val.append(str(node.val))
                ind.append(str(idx))

                if node.left:
                    q.append([node.left, 2 * idx + 1])

                if node.right:
                    q.append([node.right, 2 * idx + 2])

        return ",".join(val) + ";" + ",".join(ind)

    def deserialize(self, data):
        if not data:
            return None

        data = data.split(";")
        val = data[0].split(",")
        ind = data[1].split(",")

        level_val_map = {}
        level_node_map = {}

        rootfound = False
        root = None

        for i, indx in enumerate(ind):
            node = TreeNode(int(val[int(i)]))
            if not rootfound:
                root = node
                rootfound = True
            level_val_map[int(indx)] = int(val[int(i)])
            level_node_map[int(indx)] = node

        for i, indx in enumerate(ind):
            lcidx, rcidx = 2 * int(indx) + 1, 2 * int(indx) + 2
            if str(lcidx) in ind:
                level_node_map[int(indx)].left = level_node_map[lcidx]
            if str(rcidx) in ind:
                level_node_map[int(indx)].right = level_node_map[rcidx]

        return root


# Optimal [dfs]
# T.C. - O(n)+O(n)
# S.C  - O(n)+O(n)


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(root):
            if root is None:
                return ["N"]

            ans = []

            ans.append(str(root.val))

            l = dfs(root.left)
            for i in l:
                ans.append(i)

            r = dfs(root.right)
            for i in r:
                ans.append(i)

            return ans

        if not root:
            return ""

        return ",".join(dfs(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(",")

        def helper(idx, data):
            if data[idx[0]] == "N":
                return

            currRoot = TreeNode(int(data[idx[0]]))

            idx[0] += 1
            currRoot.left = helper(idx, data)

            idx[0] += 1
            currRoot.right = helper(idx, data)

            return currRoot

        index = [0]
        return helper(index, data)
