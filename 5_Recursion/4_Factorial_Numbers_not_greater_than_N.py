# https://www.codingninjas.com/studio/problems/factorial-numbers-not-greater-than-n_8365435,Easy

# Brute
# T.C. -> k*O(k)
# S.C. -> O(k) [Recursion stack space]


def getFac(n):
    if n <= 1:
        return n

    return n * getFac(n - 1)


def factorialNumbers(n: int) -> List[int]:
    num = 1
    ans = []

    while True:
        fac = getFac(num)
        if fac > n:
            return ans
        ans.append(fac)
        num += 1
