# https://practice.geeksforgeeks.org/problems/square-root/0 , Medium

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def floorSqrt(self, x):
        ans = 1

        for i in range(1, x + 1):
            if i**2 <= x:
                ans = i
            elif i**2 > x:
                break

        return ans


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def floorSqrt(self, x):
        st, en = 0, x
        ans = 1

        while st <= en:
            mid = (st + en) // 2

            if mid * mid <= x:
                ans = mid
                st = mid + 1

            elif mid * mid > x:
                en = mid - 1
        return ans
