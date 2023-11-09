# https://leetcode.com/problems/letter-combinations-of-a-phone-number/ , Medium


# Brute
# T.C. - O(4^n)
# S.C  - O(m)


class Solution:
    def helper(self, idx: int, processed: str, mp: dict, digits: str, res: list[str]):
        if idx == len(digits):
            res.append(processed)
            return

        currChar = digits[idx]
        allCombi = mp[currChar]

        for i in range(len(allCombi)):
            tmp = allCombi[i]
            self.helper(idx + 1, processed + tmp, mp, digits, res)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        self.helper(0, "", mp, digits, res)
        return res
