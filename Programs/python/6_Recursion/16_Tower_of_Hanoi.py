# https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1, Medium, IBH

# Question
# You are given n disks placed on a starting rod (from), with the smallest disk on top and the largest at the bottom. There are three rods:
# the starting rod(from), the target rod (to), and an auxiliary rod (aux).
# You have to calculate the total number of moves required to transfer all n disks from the starting rod to the target rod, following these rules:
#       1. Only one disk can be moved at a time.
#       2. A disk can only be placed on top of a larger disk or on an empty rod.
# Return the number of moves needed to complete the task.

# Examples:

# Input: n = 2
# Output: 3
# Explanation: For n =2 , steps will be as follows in the example and total 3 steps will be taken.
# move disk 1 from rod 1 to rod 2
# move disk 2 from rod 1 to rod 3
# move disk 1 from rod 2 to rod 3

# Input: n = 3
# Output: 7
# Explanation: For N=3 , steps will be as follows in the example and total 7 steps will be taken.
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
# T.C. - O(2^N) [two possibilities for every disk]
# S.C  - O(N) [recursion stack space]

# Intuition
# We can use the concept of IBH in this case very easily
# We develop a hypo that given n,fromm,to,aux the function
# will move all n plates from  src to destination.
# Now lets solve the problem for smaller input, now lets
# put the n-1 disk from rod1 to rod2 leaving the last plate
# then our problem becomes easy right, in the induction step
# we just have to move the leftover disk from rod1 to rod3
# and all the plates at rod2 to rod3 obeying all the conditions
# given to us


class Solution:
    def towerOfHanoi(self, n: int, fromm: int, to: int, aux: int) -> int:
        # Base
        if n == 1:
            # print(
            #     "move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to)
            # )
            return 1

        c = 0
        # Hypo
        # Move all the plates (n-1) rod leaving the last plate to rod 2
        c += self.towerOfHanoi(n - 1, fromm, aux, to)

        # Induction
        # Move the leftover plate in rod1 to rod3
        # print(
        #         "move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to)
        #     )
        c += 1

        # Now move all the plates at rod2 to rod3
        c += self.towerOfHanoi(n - 1, aux, to, fromm)

        return c
