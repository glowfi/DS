# https://leetcode.com/problems/powx-n/ , Medium

# Brute
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def helper(self, x, n):
        ans = 1
        for i in range(n):
            ans *= x
        return ans

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            val = self.helper(x, n * -1)
            return 1 / (val)
        val = self.helper(x, n)
        return val


# Optimal [Recursion]
# T.C. - O(log(n))
# S.C  - O(log(n))

# Recursive Tree
# https://0x0.st/Ht3W.347.png


class Solution:
    def getval(self, x, n):
        if n == 0:
            return 1

        val = self.getval(x, n // 2)

        if n % 2 == 0:
            return val * val

        return val * val * x

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            val = self.getval(x, n * -1)
            return 1 / val

        return self.getval(x, n)


# Optimal [Iterative]
# T.C. - O(log(n))
# S.C  - O(log(n))

# Algorithm
# + Square the base half the expoenent
# + Store the x if expoenent is odd


class Solution:
    def getval(self, x, n):
        res = 1
        while n > 0:
            if n % 2 != 0:
                res *= x
            x *= x
            n //= 2
        return res

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            val = self.getval(x, n * -1)
            return 1 / val

        return self.getval(x, n)
