# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/ , Easy


# Brute
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 2 == 0:
            return 1 + self.numberOfSteps(num // 2)
        else:
            return 1 + self.numberOfSteps(num - 1)
