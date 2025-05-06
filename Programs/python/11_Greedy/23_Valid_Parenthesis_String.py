# https://leetcode.com/problems/valid-parenthesis-string , Medium


# Recursion
# T.C. - O(4^n)
# S.C  - O(n)


class Solution:
    def solve(self, idx, count, s: str) -> bool:
        if idx == len(s):
            return count == 0

        if count < 0:
            return False

        if s[idx] == "*":
            return (
                self.solve(idx + 1, count, s)
                or self.solve(idx + 1, count + 1, s)
                or self.solve(idx + 1, count - 1, s)
            )

        if s[idx] == "(":
            return self.solve(idx + 1, count + 1, s)

        return self.solve(idx + 1, count - 1, s)

    def checkValidString(self, s: str) -> bool:
        return self.solve(0, 0, s)


# Memoization
# T.C. - O(N^2)
# S.C  - O(N)+O(N)


class Solution:
    def solve(self, idx, count, s: str, memo: dict) -> bool:
        if idx == len(s):
            return count == 0

        if count < 0:
            return False

        if (idx, count) in memo:
            return memo[(idx, count)]

        if s[idx] == "*":
            memo[(idx, count)] = (
                self.solve(idx + 1, count, s, memo)
                or self.solve(idx + 1, count + 1, s, memo)
                or self.solve(idx + 1, count - 1, s, memo)
            )
            return memo[(idx, count)]

        if s[idx] == "(":
            memo[(idx, count)] = self.solve(idx + 1, count + 1, s, memo)
            return memo[(idx, count)]

        memo[(idx, count)] = self.solve(idx + 1, count - 1, s, memo)
        return memo[(idx, count)]

    def checkValidString(self, s: str) -> bool:
        return self.solve(0, 0, s, {})


# Tabulation
# T.C. - O(N^2)
# S.C  - O(N*N)


class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = [[False for _ in range((len(s) * 2)+1] for _ in range(len(s))]

        return dp[len(s) - 1][0]


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# carry over a range possible values
# if at the end min is possible value is 0 return True


class Solution:
    def checkValidString(self, s: str) -> bool:
        min_val = 0
        max_val = 0

        for i in range(len(s)):
            if s[i] == "(":
                min_val += 1
                max_val += 1
            elif s[i] == ")":
                min_val -= 1
                max_val -= 1
            else:
                min_val -= 1
                max_val += 1

            if min_val < 0:
                min_val = 0

            if max_val < 0:
                return False
        return min_val == 0
