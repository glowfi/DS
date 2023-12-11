# https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1 , Medium


# Brute
# T.C. - O(log(n))+O(n)
# S.C  - O(log(n))+O(n)


class Solution:
    def ceil(self, arr, x):
        st, en = 0, len(arr) - 1
        ans = -1
        while st <= en:
            mid = st + (en - st) // 2
            if arr[mid] >= x:
                ans = arr[mid]
                en = mid - 1
            else:
                st = mid + 1
        return ans

    def findCeil(self, root, inp):
        ls = []

        def helper(root):
            if root is None:
                return

            helper(root.left)
            ls.append(root.key)
            helper(root.right)

        helper(root)

        return self.ceil(ls, inp)


# Better
# T.C. - O(log(n))
# S.C  - O(log(n))


class Solution:
    def findCeil(self, root, inp):
        ans = [float("inf")]

        def helper(root):
            if root is None:
                return

            if root.key >= inp:
                ans[0] = min(ans[0], root.key)

            if inp < root.key:
                helper(root.left)

            if inp > root.key:
                helper(root.right)

        helper(root)
        if ans[0] == float("inf"):
            return -1
        return ans[0]
