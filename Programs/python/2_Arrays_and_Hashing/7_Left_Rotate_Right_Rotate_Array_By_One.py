# NA , Easy, Rotation

# Question
# You are given an integer array arr of size n. You need to implement two functions to perform rotations on this array:

# Left Rotate: Implement a function left_rotate(arr: List[int]) -> List[int] that rotates the array to the left by one position. The first
# element of the array should move to the end.

# Right Rotate: Implement a function right_rotate(arr: List[int]) -> List[int] that rotates the array to the right by one position.
# The last element of the array should move to the front.

# Left Rotate Test Cases:

# Example 1:

# Input:
# arr = [1, 2, 3, 4, 5]

# Output:
# [2, 3, 4, 5, 1]

# Example 2:

# Input:
# arr = [10, 20, 30, 40, 50]

# Output:
# [20, 30, 40, 50, 10]

# --------------------------------

# Right Rotate Test Cases:

# Example 1:

# Input:
# arr = [1, 2, 3, 4, 5]

# Output:
# [5, 1, 2, 3, 4]

# Example 2:

# Input:
# arr = [10, 20, 30, 40, 50]

# Output:
# [50, 10, 20, 30, 40]

# Constraints:

# The input array will contain at least one integer.
# The array can contain both positive and negative integers.


# Intuition

# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# For left rotation move the first element to the last index by continous swapping
# For right rotation move the last element to the first index by continous swapping

from typing import List


def left_rotate(arr: List[int]) -> List[int]:
    for i in range(len(arr) - 1):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def right_rotate(arr: List[int]) -> List[int]:
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr


# Example usage with assertions
if __name__ == "__main__":
    # Test left rotation
    assert left_rotate([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 1], "Test Case 1 Failed"
    assert left_rotate([10, 20, 30, 40, 50]) == [
        20,
        30,
        40,
        50,
        10,
    ], "Test Case 2 Failed"
    assert left_rotate([]) == [], "Test Case 3 Failed"  # Edge case: empty array

    # Test right rotation
    assert right_rotate([1, 2, 3, 4, 5]) == [5, 1, 2, 3, 4], "Test Case 1 Failed"
    assert right_rotate([10, 20, 30, 40, 50]) == [
        50,
        10,
        20,
        30,
        40,
    ], "Test Case 2 Failed"
    assert right_rotate([]) == [], "Test Case 3 Failed"  # Edge case: empty array

    print("All test cases passed!")
