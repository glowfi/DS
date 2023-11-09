# NA , Easy


# Optimal
# T.C. - O(n)
# S.C  - O(n)


def reverse(n, rev):
    if n >= 0 and n <= 9:
        return rev * 10 + n

    d = n % 10
    rev = rev * 10 + d
    num = (n - d) // 10
    k = reverse(num, rev)
    return k


def checkPali(num):
    return num == reverse(num, 0)


print(checkPali(1234))
print(checkPali(333))
