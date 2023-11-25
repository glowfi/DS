# https://practice.geeksforgeeks.org/problems/permutation-with-spaces3627/1 , Medium

# Brute
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, idx, st, tmp, ans):
        if idx == len(st):
            ans.append(tmp[:])
            return

        if idx == 0:
            # Take first character only
            self.solve(idx + 1, st, tmp + st[idx], ans)
        else:
            # Take first character with space
            self.solve(idx + 1, st, tmp + " " + st[idx], ans)
            # Take first character only
            self.solve(idx + 1, st, tmp + st[idx], ans)

    def permutation(self, S):
        ans = []
        self.solve(0, S, "", ans)
        return ans
