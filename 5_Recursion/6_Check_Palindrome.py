# https://www.codingninjas.com/studio/problems/check-palindrome-recursive_624386,Easy

# Brute
# T.C. -> O(log(n))
# S.C. -> O(log(n)) [Recursion stack space]


def helper(i, st, n):
    if i == len(st) // 2:
        return True

    if st[i] != st[n - i - 1]:
        return False

    return helper(i + 1, st, n)


def isPalindrome(string: str) -> bool:
    return helper(0, string, len(string))
