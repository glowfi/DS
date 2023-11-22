# https://leetcode.com/problems/letter-combinations-of-a-phone-number/ , Medium

# Recursive Tree
# https://0x0.st/HtkD.068.png

# Optimal [ans in argument]
# T.C. - O(4^n)
# S.C  - O(m)


class Solution:
    def getAllCombi(self, idx, tmp, digits, ans, mp):
        if idx == len(digits):
            ans.append(tmp)
            return

        getCharCombi = mp[digits[idx]]

        for char in getCharCombi:
            self.getAllCombi(idx + 1, tmp + char, digits, ans, mp)

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
        ans = []

        self.getAllCombi(0, "", digits, ans, mp)

        return ans


# Optimal [ans in body]
# T.C. - O(4^n)
# S.C  - O(m)


class Solution:
    def getAllCombi(self, idx, tmp, digits, mp):
        if idx == len(digits):
            return [tmp]

        getCharCombi = mp[digits[idx]]

        ans = []

        for char in getCharCombi:
            vals = self.getAllCombi(idx + 1, tmp + char, digits, mp)
            for val in vals:
                ans.append(val)

        return ans

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

        return self.getAllCombi(0, "", digits, mp)
