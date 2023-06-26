# NA, Easy


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


# Smallest among all the numbers greater than x
def ceil(x, nums):
    st, en = 0, len(nums) - 1
    ans = -1

    while st <= en:
        mid = (st + en) // 2

        if ord(nums[mid]) > ord(x):
            ans = nums[mid]
            en = mid - 1

        else:
            st = mid + 1

    return ans


nums = ["a", "c", "f", "h", "l", "q"]
x = "l"

print(ceil(x, nums))
