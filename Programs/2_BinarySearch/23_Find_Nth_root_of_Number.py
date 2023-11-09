# https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1 , Medium

# Brute
# T.C. -> O(n*m)
# S.C. -> O(1)


class Solution:
    def nthroot(self, num, power):
        return num**power

    def NthRoot(self, n, m):
        for i in range(1, m + 1):
            if self.nthroot(i, n) == m:
                return i
            elif self.nthroot(i, n) > m:
                break
        return -1


# Optimal
# T.C. -> O(log(n)*n)
# S.C. -> O(1)


class Solution:
    def nthroot(self, num, power):
        return num**power

    def NthRoot(self, n, m):
        st, en = 1, m + 1
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2
            if self.nthroot(mid, n) == m:
                return mid
            elif self.nthroot(mid, n) < m:
                st = mid + 1
            else:
                en = mid - 1
        return ans
