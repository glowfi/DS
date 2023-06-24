# https://www.codingninjas.com/codestudio/problems/ceiling-in-a-sorted-array_1825401,Medium


# Floor -> Largest number in the array such that number<=x
# Ceil  -> Smallest number in the array such that number>=x


# Optimal
# T.C. -> O(log(n))+O(log(n))
# S.C. -> O(1)


def ceilingInSortedArray(n, x, arr):
    arr.sort()

    def getFloor(n, x, arr):
        ans = -1
        st, en = 0, len(arr) - 1

        while st <= en:
            mid = (st + en) // 2

            if arr[mid] > x:
                en = mid - 1
            elif arr[mid] <= x:
                ans = mid
                st = mid + 1
        return ans

    def getCeil(n, x, arr):
        ans = -1
        st, en = 0, len(arr) - 1

        while st <= en:
            mid = (st + en) // 2

            if arr[mid] < x:
                st = mid + 1

            elif arr[mid] >= x:
                ans = mid
                en = mid - 1
        return ans

    floor = getFloor(n, x, arr)
    ceil = getCeil(n, x, arr)
    ans = [arr[floor], arr[ceil]]
    if floor == -1:
        ans[0] = -1
    elif ceil == -1:
        ans[-1] = -1

    return ans
