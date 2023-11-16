# https://leetcode.com/problems/letter-combinations-of-a-phone-number/ , Medium

# Recursive Tree
# https://0x0.st/HtkD.068.png

# Optimal [ans in argument]
# T.C. - O(4^n)
# S.C  - O(m)


class Solution:
    def helper(self, idx: int, proc: str, s: str, mp: dict[str], res: list[str]):
        if idx == len(s):
            res.append(proc)
            return

        combiString = mp[s[idx]]

        for char in combiString:
            newString = proc + char
            self.helper(idx + 1, newString, s, mp, res)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []

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

        self.helper(0, "", digits, mp, res)

        return res


# Optimal [ans in body]
# T.C. - O(4^n)
# S.C  - O(m)


class Solution:
    def helper(self, idx: int, proc: str, s: str, mp: dict[str]):
        if idx == len(s):
            return [proc]

        combiString = mp[s[idx]]
        tmp = []

        for char in combiString:
            newString = proc + char
            val = self.helper(idx + 1, newString, s, mp)
            for i in val:
                tmp.append(i)

        return tmp

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

        return self.helper(0, "", digits, mp)
