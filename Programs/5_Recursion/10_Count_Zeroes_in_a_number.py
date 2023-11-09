# NA , Easy

# Optimal
# T.C. - O(n)
# S.C  - O(n)


def countZeroes(n: int) -> int:
    if n == 0:
        return 1

    if n > 0 and n <= 9:
        return 0

    d = n % 10
    num = (n - d) // 10
    if d == 0:
        return 1 + countZeroes(num)
    else:
        return countZeroes(num)


print(countZeroes(1))
print(countZeroes(0))
print(countZeroes(1020303))
