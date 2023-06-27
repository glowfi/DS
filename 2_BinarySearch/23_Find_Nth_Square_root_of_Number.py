# https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1 , Medium

# Brute
# T.C. -> O(n*m)
# S.C. -> O(1)


class Solution:
    def NthRoot(self, n, m):
        ans = -1
        for i in range(1, m + 1):
            if i**n == m:
                ans = i
            elif i**n < m:
                ans = -1
            elif i**n > m:
                break
        return ans


# Optimal
# T.C. -> O(log(n)*n)
# S.C. -> O(1)


class Solution:
    def NthRoot(self, n, m):
        ans = -1
        st, en = 1, m

        while st <= en:
            mid = (st + en) // 2

            if mid**n == m:
                return mid

            elif mid**n < m:
                st = mid + 1
                ans = -1

            elif mid**n > m:
                en = mid - 1

        return ans
