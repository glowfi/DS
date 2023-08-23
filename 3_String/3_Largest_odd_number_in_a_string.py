# https://leetcode.com/problems/largest-odd-number-in-string/ , Easy

# Brute
# T.C. -> O(n^2)
# S.C. -> O(1)


class Solution:
    def largestOddNumber(self, num: str) -> str:
        largest = 1
        flag = 0
        for i in range(len(num)):
            for j in range(i, len(num)):
                if int(num[i : j + 1]) % 2 != 0:
                    flag = 1
                    largest = max(largest, int(num[i : j + 1]))

        if flag == 0 and largest == 1:
            return ""

        return str(largest)


# Optimal
# T.C. -> O(n)
# S.C. -> O(5)


class Solution:
    def largestOddNumber(self, num: str) -> str:
        st = {"1", "3", "5", "7", "9"}
        idx = len(num) - 1

        while idx >= 0:
            if num[idx] in st:
                return num[: idx + 1]
            idx -= 1
        return ""
