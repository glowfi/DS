# https://leetcode.com/problems/string-to-integer-atoi/ , Medium

# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        limit = 2**31
        upper = limit - 1
        lower = limit * -1

        # Handle Leading Space
        s = s.lstrip(" ")
        # print(s)

        # Handle empty string
        if not s:
            return 0

        # Check sign
        sign = 1
        if s[idx] == "-":
            sign = -1
            idx += 1
        elif s[idx] == "+":
            sign = 1
            idx += 1

        # Handle parsing of numbers
        parsed = 0
        while idx < len(s):
            if not s[idx].isnumeric():
                break
            else:
                parsed = parsed * 10 + (ord(s[idx]) - ord("0"))

            idx += 1

        # Assign Sign
        parsed *= sign

        # Check inbounds
        if parsed >= upper:
            return upper
        elif parsed <= lower:
            return lower

        return parsed
