# NA , Easy

# Optimal [ans in body]
# T.C. - O(n)
# S.C  - O(n)


def sumofdigits(n):
    if n == 0:
        return 0
    d = n % 10
    num = (n - d) // 10
    return d + sumofdigits(num)
