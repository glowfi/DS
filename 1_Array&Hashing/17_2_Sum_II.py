# https://www.codingninjas.com/codestudio/problems/reading_6845742,Easy

# Brute
# T.C. -> O(n^2)
# S.C. -> O(1)


def read(n: int, book: [int], target: int) -> str:
    for i in range(len(book)):
        for j in range(i + 1, len(book)):
            if book[i] + book[j] == target:
                return "YES"
    return "NO"


# Better
# T.C. -> O(n)
# S.C. -> O(n)


def read(n: int, book: [int], target: int) -> str:
    h = {}

    for i in range(len(book)):
        diff = target - book[i]

        if diff in h:
            return "YES"
        else:
            h[book[i]] = i
    return "NO"


# Better
# T.C. -> O(nlog(n))+O(n)
# S.C. -> O(1)


def read(n: int, book: [int], target: int) -> str:
    book.sort()

    i, j = 0, len(book) - 1

    while i < j:
        if book[i] + book[j] == target:
            return "YES"
        elif book[i] + book[j] < target:
            i += 1
        else:
            j -= 1
    return "NO"
