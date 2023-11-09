# NA , Easy


# Optimal [ans in body]
# T.C. - O(n)
# S.C  - O(n)


def prodofdigits(n):
    if n == 1:
        return 1

    d = n % 10
    num = (n - d) // 10
    return d * prodofdigits(num)
