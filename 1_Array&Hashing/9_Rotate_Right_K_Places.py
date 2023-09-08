# https://leetcode.com/problems/rotate-array/,Easy

# Brute
# T.C. -> O(k*n)
# S.C. -> O(1)


def right(ls, k):
    k = k % len(ls)

    for i in range(k):
        for i in range(len(ls) - 1, 0, -1):
            ls[i], ls[i - 1] = ls[i - 1], ls[i]
    return ls


print(right([1, 2, 3, 4, 5], 3))

# Optimal
# T.C. -> O(n)+O(k)+O(n-k)
# S.C. -> O(1)


# Right
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        def rev(i, j, arr):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        rev(0, len(nums) - 1, nums)
        rev(0, k - 1, nums)
        rev(k, len(nums) - 1, nums)
