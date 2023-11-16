# https://leetcode.com/problems/permutations/ , Easy

# Recursive Tree
# https://0x0.st/HtUm.763.png

# Brute [Ans in argument]
# T.C. - O(n!)
# S.C  - O(n)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(idx: int, proc: list[int], res: list[str]) -> None:
            if idx == len(nums):
                res.append(proc)
                return

            for i in range(len(proc) + 1):
                newArrangement = [*proc[:i], nums[idx], *proc[i:]]
                helper(idx + 1, newArrangement, res)

        helper(0, [], res)

        return res


# Brute [Ans in body]
# T.C. - O(n!)
# S.C  - O(n)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(idx: int, proc: list[int]) -> list[list[int]]:
            if idx == len(nums):
                return [proc]

            tmp = []

            for i in range(len(proc) + 1):
                newArrangement = [*proc[:i], nums[idx], *proc[i:]]
                val = helper(idx + 1, newArrangement)
                for i in val:
                    tmp.append(i)

            return tmp

        return helper(0, [])
