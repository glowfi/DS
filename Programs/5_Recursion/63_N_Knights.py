# https://practice.geeksforgeeks.org/problems/save-knights2718/1 , Medium

# Brute
# T.C. - O(n^n)
# S.C  - O(n)


def display(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()
    print("")


def canPlace(ro, co, mat):
    dirs = [(), (), (), ()]


def solve(ro, co, mat, placed):
    if placed == 0:
        display(mat)
        return

    # Logic for going to next row
    if co == len(mat):
        solve(ro + 1, 0, mat, placed)
        return

    # if at last row and last index
    if ro == len(mat) - 1 and co == len(mat):
        return

    if canPlace(ro, co, mat):
        mat[ro][co] = "K"
        solve(ro, co + 1, mat, placed + 1)
        mat[ro][co] = "."

    # Logic for going to next row
    solve(ro, co + 1, mat, placed + 1)


def NKnights(n):
    mat = [["." for _ in range(n)] for _ in range(n)]
    ans = []
    solve(0, 0, mat, n)


NKnights(4)
