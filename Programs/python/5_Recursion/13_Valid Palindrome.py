# https://leetcode.com/problems/valid-palindrome/ , Easy


# Better
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def helper(self, l, r, s, tmp):
        if l >= r:
            return True

        while l < r and s[l] not in tmp:
            l += 1

        while r > l and s[r] not in tmp:
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        return self.helper(l + 1, r - 1, s, tmp)

    def isPalindrome(self, s: str) -> bool:
        tmp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890"
        return self.helper(0, len(s) - 1, s, tmp)


# Optimal
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890"
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and s[l] not in tmp:
                l += 1

            while r > l and s[r] not in tmp:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
