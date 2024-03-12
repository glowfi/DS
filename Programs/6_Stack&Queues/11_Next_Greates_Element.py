# https://www.geeksforgeeks.org/problems/greater-on-right-side4305/1 , Easy

# Optimal
# T.C. - O(N)
# S.C  - O(N)


class Solution:
    def nextLargerElement(self, arr, n):
        # Monotonically Decreasing Stack from bottom to top
        stk = []
        ans = [-1 for _ in range(len(arr))]

        for idx in range(len(arr) - 1, -1, -1):
            while stk and stk[-1] <= arr[idx]:
                stk.pop(-1)

            ans[idx] = stk[-1] if stk else -1
            stk.append(arr[idx])

        return ans


arr = [16, 17, 4, 3, 5, 2]
arr = [2, 3, 1, 9]
arr = [1, 3, 2, 4]
obj = Solution()
print(obj.nextGreatest(arr, len(arr)))
