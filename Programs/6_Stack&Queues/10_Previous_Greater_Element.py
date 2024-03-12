# NA , Easy

# Optimal
# T.C. - O(N)
# S.C  - O(N)


class Solution:
    def previous_greater_element(self, ls, out):
        # Monotonically Decreasing Stack from bottom to top
        stk = []
        ans = [-1 for _ in range(len(ls))]

        for idx in range(len(ls)):
            while stk and stk[-1] <= ls[idx]:
                stk.pop(-1)

            ans[idx] = stk[-1] if stk else -1
            stk.append(ls[idx])

        return ans == out, ans


# ls = [10, 4, 2, 20, 40, 12, 30]
# out = [-1, 10, 4, -1, -1, 40, 40]

# ls = [10, 20, 30, 40]
# out = [-1, -1, -1, -1]

# ls = [40, 30, 20, 10]
# out = [-1, 40, 30, 20]

obj = Solution()
print(obj.previous_greater_element(ls, out))
