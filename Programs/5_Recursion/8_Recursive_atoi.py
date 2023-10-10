# https://leetcode.com/problems/string-to-integer-atoi/,Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(n) [Recursion stack space]


class Solution:
    def helper(self, st, parsed, idx):
        if idx == len(st):
            return parsed

        if not st[idx].isnumeric():
            return parsed

        parsed = parsed * 10 + (ord(st[idx]) - ord("0"))
        return self.helper(st, parsed, idx + 1)

    def myAtoi(self, s: str) -> int:
        # Constants
        idx = 0
        intmin = -1 * (2**31)
        intmax = (2**31) - 1

        # Trim leading spaces
        s = s.strip(" ")

        if not s:
            return 0

        # Determine sign
        sign = 1
        if s[0] == "-":
            sign = -1
            idx += 1
        elif s[0] == "+":
            sign = 1
            idx += 1

        getNum = self.helper(s, 0, idx)

        # Assign sign
        if sign == -1:
            getNum *= sign

        # Check inbounds
        if getNum >= intmax:
            return intmax

        elif getNum <= intmin:
            return intmin

        return getNum


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def myAtoi(self, s: str) -> int:
        # Constants
        idx = 0
        intmin = -1 * (2**31)
        intmax = (2**31) - 1

        # Trim leading spaces
        s = s.strip(" ")

        if not s:
            return 0

        # Determine sign
        sign = 1
        if s[0] == "-":
            sign = -1
            idx += 1
        elif s[0] == "+":
            sign = 1
            idx += 1

        parsed = 0
        while idx < len(s):
            if s[idx].isnumeric():
                parsed = parsed * 10 + (ord(s[idx]) - ord("0"))
                idx += 1
            else:
                break

        # Assign sign
        if sign == -1:
            parsed *= sign

        # Check inbounds
        if parsed >= intmax:
            return intmax

        elif parsed <= intmin:
            return intmin

        return parsed
