# NA , Medium

# Question
# Given an array of integers sorted in ascending order, and a target value, find the element
# in the array that has minimum difference with the target value.

# Example 1:

# Input: a[] = [2, 5, 10, 12, 15], target = 6
# Output: 5
# Explanation: The difference between the target value '6' and '5' is the minimum.
# Example 2:

# Input: a[] = [2, 5, 10, 12, 15], target = 5
# Output: 5
# Example 3:

# Input: a[] = [2, 5, 10, 12, 15], target = 8
# Output: 10
# Example 4:

# Input: a[] = [2, 5, 10, 12, 15], target = 11
# Output: 10
# Example 5:

# Input: a[] = [2, 5, 10, 12, 15], target = 20
# Output: 15

# Optimal
# T.C. - O(log(N))+O(log(N))
# S.C  - O(1)

# Intuition
# Find the ceil and floor of the given target as the,
# min diff will always be with them,also check if
# target is less than first element in array return the
# first element or if target is greater than last element
# in array return the last element


class Solution:
    def floor(self, x: int, arr: list[int]):
        st, en = 0, len(arr) - 1
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2

            if arr[mid] <= x:
                ans = arr[mid]
                st = mid + 1
            elif arr[mid] > x:
                en = mid - 1

        return ans

    def ceil(self, x: int, arr: list[int]):
        st, en = 0, len(arr) - 1
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2

            if arr[mid] >= x:
                ans = arr[mid]
                en = mid - 1
            else:
                st = mid + 1

        return ans

    def find_min_diff(self, arr: list[int], target: int) -> int:
        if target < arr[0]:
            return arr[0]

        if target > arr[-1]:
            return arr[-1]

        ceil = self.ceil(target, arr)
        floor = self.floor(target, arr)

        diff_ceil = abs(ceil - target)
        diff_floor = abs(floor - target)

        if diff_ceil < diff_floor:
            return ceil
        return floor


if __name__ == "__main__":
    # Test cases
    solution = Solution()
    arr1 = [2, 5, 10, 12, 15]
    target1 = 6
    expected1 = 5
    assert (
        solution.find_min_diff(arr1, target1) == expected1
    ), f"Test case 1 failed: expected {expected1}, got {solution.find_min_diff(arr1, target1)}"

    arr2 = [2, 5, 10, 12, 15]
    target2 = 5
    expected2 = 5
    assert (
        solution.find_min_diff(arr2, target2) == expected2
    ), f"Test case 2 failed: expected {expected2}, got {solution.find_min_diff(arr2, target2)}"

    arr3 = [2, 5, 10, 12, 15]
    target3 = 8
    expected3 = 10
    assert (
        solution.find_min_diff(arr3, target3) == expected3
    ), f"Test case 3 failed: expected {expected3}, got {solution.find_min_diff(arr3, target3)}"

    arr4 = [2, 5, 10, 12, 15]
    target4 = 11
    expected4 = 10
    assert (
        solution.find_min_diff(arr4, target4) == expected4
    ), f"Test case 4 failed: expected {expected4}, got {solution.find_min_diff(arr4, target4)}"

    arr5 = [2, 5, 10, 12, 15]
    target5 = 20
    expected5 = 15
    assert (
        solution.find_min_diff(arr5, target5) == expected5
    ), f"Test case 5 failed: expected {expected5}, got {solution.find_min_diff(arr5, target5)}"

    print("All test cases passed!")
