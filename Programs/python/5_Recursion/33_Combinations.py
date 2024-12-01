# https://leetcode.com/problems/combinations/ , Medium

# Brute [Ans in argument]
# T.C. - O(2^n)
# S.C  - O(k)


class Solution:
    def getCombinations(
        self, idx: int, tmp: list[int], ans: list[list[int]], k: int, n: int
    ):
        if len(tmp) == k:
            ans.append(tmp[:])
            return

        for i in range(idx, n + 1):
            tmp.append(i)
            self.getCombinations(i + 1, tmp, ans, k, n)
            tmp.pop(-1)

    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return []

        ans = []
        self.getCombinations(1, [], ans, k, n)
        return ans


# Brute [Ans in argument]
# T.C. - O(2^n)
# S.C  - O(k)


class Solution:
    def getCombinations(self, idx: int, tmp: list[int], k: int, n: int):
        if len(tmp) == k:
            return [tmp[:]]

        ans = []

        for i in range(idx, n + 1):
            tmp.append(i)
            vals = self.getCombinations(i + 1, tmp, k, n)
            for val in vals:
                ans.append(val[:])
            tmp.pop(-1)

        return ans

    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return []

        return self.getCombinations(1, [], k, n)
