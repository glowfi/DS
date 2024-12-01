# https://leetcode.com/problems/letter-case-permutation/ , Medium

# Brute
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, idx, tmp, st: str, mp, ans):
        if idx == len(st):
            ans.append(tmp[:])
            return

        # check numbers
        if st[idx] in mp:
            self.solve(idx + 1, tmp + st[idx], st, mp, ans)

        elif st[idx].isalpha():
            self.solve(idx + 1, tmp + st[idx].lower(), st, mp, ans)
            self.solve(idx + 1, tmp + st[idx].upper(), st, mp, ans)

    def letterCasePermutation(self, s: str) -> list[str]:
        mp = {str(i): True for i in range(10)}
        ans = []
        self.solve(0, "", s, mp, ans)
        return ans


obj = Solution()
s = "a1b2"
print(obj.letterCasePermutation(s))
