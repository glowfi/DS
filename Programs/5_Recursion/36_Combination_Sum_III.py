# https://leetcode.com/problems/combination-sum-iii/ , Medium

# Brute
# T.C. - O(2^n * k), where n is the size of vector v, k is the average length
# S.C  - O(k * x), where x is the total number of possible combinations


class Solution:
    def getCombinations(
        self,
        idx: int,
        tmp: list[int],
        target: int,
        k,
        ans: list[list[int]],
    ):
        if k == 0:
            if target == 0:
                ans.append(tmp[:])
            return

        for i in range(idx, 10):
            tmp.append(i)
            self.getCombinations(i + 1, tmp, target - i, k - 1, ans)
            tmp.pop(-1)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.getCombinations(1, [], n, k, ans)
        return ans
