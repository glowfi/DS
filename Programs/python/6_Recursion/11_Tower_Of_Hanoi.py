# https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1, Medium, IBH

# Question
# You are given n disks placed on a starting rod (from), with the smallest disk on top and the largest at the bottom. There are
# three rods: the starting rod(from), the target rod (to), and an auxiliary rod (aux).
# You have to calculate the minimum number of moves required to transfer all n disks from the starting rod to the target rod, following these rules:
#       1. Only one disk can be moved at a time.
#       2. A disk can only be placed on top of a larger disk or on an empty rod.
# Return the minimum number of moves needed to complete the task.

# Examples:

# Input: n = 2
# Output: 3
# Explanation: For n = 2, total 3 steps will be taken. Steps are as follows -
# move disk 1 from rod 1 to rod 2
# move disk 2 from rod 1 to rod 3
# move disk 1 from rod 2 to rod 3

# Input: n = 3
# Output: 7
# Explanation: For n = 3, total 7 steps will be taken.Steps are as follows -
# move disk 1 from rod 1 to rod 3
# move disk 2 from rod 1 to rod 2
# move disk 1 from rod 3 to rod 2
# move disk 3 from rod 1 to rod 3
# move disk 1 from rod 2 to rod 1
# move disk 2 from rod 2 to rod 3
# move disk 1 from rod 1 to rod 3

# Input: n = 0
# Output: 0
# Explanation: Total 0 steps will be taken.

# Constraints:
#   0 ≤ n ≤ 20

# Optimal
# T.C. - O(2^n)
# S.C  - O(n)

# Intuition
# Use the IBH method
# Define hypothesis to that given towerOfHanoi function it will move all the n rods to desitnation
# we will move n-1 rods to the auxiliary rods and atlast move the biggest rod in source to desitnation
# and all the rods in auxiliary to desitnation using source


class Solution:
    def towerOfHanoi(self, n: int, fromm: int, to: int, aux: int):
        # Base
        if n == 1:
            # print(f"move disk {n} from rod {fromm} to rod {to}")
            return 1

        # Hypothesis
        a = self.towerOfHanoi(n - 1, fromm, aux, to)  # Move all n-1 rods to auxiliary
        # print(f"move disk {n} from rod {fromm} to rod {to}")
        b = self.towerOfHanoi(n - 1, aux, to, fromm)  # Move the n-1 rods to desitnation

        # Induction
        return 1 + a + b


obj = Solution()
print(obj.towerOfHanoi(3, 1, 2, 3))
