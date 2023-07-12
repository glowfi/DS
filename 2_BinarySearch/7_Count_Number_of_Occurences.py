# https://www.codingninjas.com/codestudio/problems/occurrence-of-x-in-a-sorted-array_630456 , Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


def count(arr: [int], n: int, x: int) -> int:
    count = 0

    for i in range(len(arr)):
        if arr[i] == x:
            count += 1

    return count


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


def getPosition(nums, target, type):
    st, en = 0, len(nums) - 1
    ans = -1

    while st <= en:
        mid = st + ((en - st) // 2)

        if nums[mid] == target:
            ans = mid

            if type == "first":
                en = mid - 1
            elif type == "last":
                st = mid + 1

        elif nums[mid] > target:
            en = mid - 1

        else:
            st = mid + 1
    return ans


def count(arr: [int], n: int, x: int) -> int:
    first = getPosition(arr, x, "first")
    if first == -1:
        return 0
    last = getPosition(arr, x, "last")
    return last - first + 1
