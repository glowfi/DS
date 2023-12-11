# https://practice.geeksforgeeks.org/problems/floor-in-bst/1 , Medium


# Brute
# T.C. - O(n)+O(log(n))
# S.C  - O(log(n))+O(n)


class Solution:
    def getFloor(self, arr, x):
        st, en = 0, len(arr) - 1
        ans = -1
        while st <= en:
            mid = st + (en - st) // 2
            if arr[mid] <= x:
                ans = arr[mid]
                st = mid + 1
            else:
                en = mid - 1
        return ans

    def floor(self, root, x):
        ls = []

        def helper(root):
            if root is None:
                return

            helper(root.left)
            ls.append(root.data)
            helper(root.right)

        helper(root)
        return self.getFloor(ls, x)


# Optimal
# T.C. - O(log(n))
# S.C  - O(log(n))


class Solution:
    ans = [float("-inf")]

    def floor(self, root, x):
        ans = [float("-inf")]

        def helper(root):
            if root is None:
                return

            if root.data <= x:
                ans[0] = max(ans[0], root.data)

            if x < root.data:
                helper(root.left)

            if x > root.data:
                helper(root.right)

        helper(root)
        if ans[0] == float("-inf"):
            return -1
        return ans[0]
