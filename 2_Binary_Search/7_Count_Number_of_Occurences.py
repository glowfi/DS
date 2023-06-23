# https://www.codingninjas.com/codestudio/problems/occurrence-of-x-in-a-sorted-array_630456 , Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


def findOccurence(nums, target):
    first, last = -1, -1
    c = 0

    for i in range(len(nums)):
        if nums[i] == target:
            last = i
            c += 1
        elif nums[i] > target:
            break

    if last == -1:
        return 0
    else:
        first = last - c + 1
        return last - first + 1


def count(arr: [int], n: int, x: int) -> int:
    return findOccurence(arr, x)


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


def findOccurence(nums, target, type):
    st, en = 0, len(nums) - 1
    ans = -1

    while st <= en:
        mid = (st + en) // 2

        if nums[mid] > target:
            en = mid - 1

        elif nums[mid] < target:
            st = mid + 1

        else:
            ans = mid

            if type == "first":
                en = mid - 1
            else:
                st = mid + 1
    return ans


def count(arr: [int], n: int, x: int) -> int:
    first = findOccurence(arr, x, "first")

    if first == -1:
        return 0
    last = findOccurence(arr, x, "last")

    return last - first + 1
