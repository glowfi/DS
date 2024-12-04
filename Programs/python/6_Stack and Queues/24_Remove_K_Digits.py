# https://leetcode.com/problems/remove-k-digits/ , Medium

# Brute
# T.C. - O(2^n)
# S.C  - O(n)+O(n)


class Solution:
    def sanitizeNumber(self, num: str):
        if len(num) == 0:
            return "0"

        if len(num) == 1:
            return num

        idx = 0
        while idx < len(num) and num[idx] == "0":
            idx += 1

        if not num[idx:]:
            return "0"
        return num[idx:]

    def strToInt(self, num: str):
        mp = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        newNum = 0

        for i in range(len(num)):
            newNum = (newNum * 10) + mp[num[i]]

        return newNum

    def solve(self, num: str, k: int):
        if k == 0:
            return float("inf")
        mn = float("inf")
        for i in range(len(num)):
            newNum = num[:i] + num[i + 1 :]
            newNum = self.sanitizeNumber(newNum)
            res = self.solve(newNum, k - 1)
            mn = min(self.strToInt(newNum), res, mn)

        return mn

    def removeKdigits(self, num: str, k: int) -> str:
        k = self.solve(num, k)
        return str(k)


# Optimal
# T.C. - O(2*n)
# S.C  - O(n)


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = [num[0]]
        mp = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        for i in range(1, len(num)):
            while k and stk and mp[stk[-1]] > mp[num[i]]:
                stk.pop(-1)
                k -= 1
            stk.append(num[i])

        # Empty stack
        if not stk:
            return "0"

        # Pop remaining
        while k:
            stk.pop(-1)
            k -= 1

        # Trailing zeroes
        idx = 0
        while idx < len(stk) and stk[idx] == "0":
            idx += 1

        res = "".join(stk[idx:])

        if not res:
            return "0"
        return res
