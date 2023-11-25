# https://practice.geeksforgeeks.org/problems/print-n-bit-binary-numbers-having-more-1s-than-0s0252/1 , Medium

# Brute
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, idx, tmp, ans, N, c0, c1):
        if idx == N:
            ans.append(tmp[:])
            return

        if c0 == c1:
            self.solve(idx + 1, tmp + "1", ans, N, c0, c1 + 1)

        elif c0 < c1:
            self.solve(idx + 1, tmp + "0", ans, N, c0 + 1, c1)
            self.solve(idx + 1, tmp + "1", ans, N, c0, c1 + 1)

    def NBitBinary(self, N):
        ans = []
        self.solve(0, "", ans, N, 0, 0)
        ans.sort(reverse=True)
        return ans


obj = Solution()
print(obj.NBitBinary(3))
