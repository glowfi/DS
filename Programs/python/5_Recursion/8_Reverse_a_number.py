# NA , Easy

# Optimal
# T.C. - O(n)
# S.C  - O(n)


def helper(n, rev):
    if n >= 0 and n <= 9:
        return rev * 10 + n

    d = n % 10
    num = (n - d) // 10
    rev = rev * 10 + d

    k = helper(num, rev)
    return k


def revNumber(n: int) -> int:
    return helper(n, 0)


print(revNumber(1234))
