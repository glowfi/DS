# NA , Easy, Basic

# Question
# You are given an integer array nums containing n + 1 integers where each integer is in the
# range [1, n]. There is only one duplicate number in the array, but it could be repeated more than once.
# You must solve the problem without modifying the input array and using O(1) extra space.


# Input: nums = [3, 1, 4, 2]
# Output: [1, 2, 3, 4]

# Input: nums = [1, 3, 4, 2]
# Output: [1, 2, 3, 4]

# Input: nums = [2, 1, 3]
# Output: [1, 2, 3]


# Optimal
# T.C. - O(N-1+n) ~ O(N)
# S.C  - O(1)

# Intuition
# Check whether current number is at its correct index
# This algorithm works for small ranged numbers
# must be in range of 1 to N or 0 to N
# For one based indexing , correct index of number is val-1
# For one based indexing , element at index i should be at i+1
# For zero based indexing , correct index of number is val
# For zero based indexing , element at index i should be at i
# Always remember -> ignore numbers greater than size of array for zero based indexing
# Always remember -> cyclic sort will make the duplicate numbers go at wrong place
# Always remember -> duplicate numbers will not be at its correct place say i , then nums[i] is the duplicate and i+1 is missing

from typing import List


def cyclic_sort(nums: List[int]) -> None:
    i = 0
    while i < len(nums):
        actualPos = nums[i] - 1
        if nums[actualPos] != nums[i]:
            nums[i], nums[actualPos] = nums[actualPos], nums[i]
        else:
            i += 1


if __name__ == "__main__":
    # Test cases
    nums1 = [3, 1, 4, 2]
    cyclic_sort(nums1)
    assert nums1 == [1, 2, 3, 4], f"Test case 1 failed: expected [1, 2, 3], got {nums1}"

    nums2 = [1, 3, 4, 2]
    cyclic_sort(nums2)
    assert nums2 == [1, 2, 3, 4], f"Test case 2 failed: expected [1, 2, 3], got {nums2}"

    nums3 = [2, 1, 3]
    cyclic_sort(nums3)
    assert nums3 == [1, 2, 3], f"Test case 3 failed: expected [1, 2, 3], got {nums3}"

    nums4 = [4, 3, 2, 1]
    cyclic_sort(nums4)
    assert nums4 == [
        1,
        2,
        3,
        4,
    ], f"Test case 4 failed: expected [1, 2, 3, 4], got {nums4}"

    nums5 = [5, 4, 3, 2, 1]
    cyclic_sort(nums5)
    assert nums5 == [
        1,
        2,
        3,
        4,
        5,
    ], f"Test case 5 failed: expected [1, 2, 3, 4, 5], got {nums5}"

    print("All test cases passed!")
