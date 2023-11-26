# https://leetcode.com/problems/palindrome-partitioning/ , Medium

# Brute
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

    def solve(self, ips, tmp, ans):
        if len(ips) == 0:
            ans.append(tmp[:])
            return

        for idx in range(len(ips)):
            ops = ips[: idx + 1]

            if self.isPalindrome(ops):
                leftOver = ips[idx + 1 :]
                tmp.append(ops)
                self.solve(leftOver, tmp, ans)
                tmp.pop(-1)

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.solve(s, [], ans)
        return ans
