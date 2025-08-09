# https://www.geeksforgeeks.org/problems/aggressive-cows/1 , Medium, BS-on-Ans

# Question
# You are given an array with unique elements of stalls[], which denote the position of a stall. You are also given an integer k
# which denotes the number of aggressive cows. Your task is to assign stalls to k cows such that
# the minimum distance between any two of them is the maximum possible.

# Examples :

# Input: stalls[] = [1, 2, 4, 8, 9], k = 3
# Output: 3
# Explanation: The first cow can be placed at stalls[0],
# the second cow can be placed at stalls[2] and
# the third cow can be placed at stalls[3].
# The minimum distance between cows, in this case, is 3, which also is the largest among all possible ways.

# Input: stalls[] = [10, 1, 2, 7, 5], k = 3
# Output: 4
# Explanation: The first cow can be placed at stalls[0],
# the second cow can be placed at stalls[1] and
# the third cow can be placed at stalls[4].
# The minimum distance between cows, in this case, is 4, which also is the largest among all possible ways.

# Input: stalls[] = [2, 12, 11, 3, 26, 7], k = 5
# Output: 1
# Explanation: Each cow can be placed in any of the stalls, as the no. of stalls are exactly equal to the number of cows.
# The minimum distance between cows, in this case, is 1, which also is the largest among all possible ways.

# Constraints:
# 2 <= stalls.size() <= 10^6
# 0 <= stalls[i] <= 10^8
# 2 <= k <= stalls.size()

# Brute
# T.C. - O(N*max(stalls))+O(Nlog(N))
# S.C  - O(1)

# Intuition
# First sort the give array as sorting will make our placements deterministic
# otherwise we might place cows too close or too far, we may miss out on optimal placemnts
# Sorting gives a predictable structure — so we can place cows in a left-to-right greedy manner
# These are like points on a number line. If the stalls aren't sorted, there's no structure
# Placing the first cow at the first stall gives maximum room for future cows to be placed at a distance of at least minDistance
# Do a linear search and keep track of whether we can place the cows in an ans variable, as we
# want the max distance all the possiblities where we can place cows


class Solution:
    def canPlaceCows(self, stalls: list[int], minDistance: int, cows: int) -> bool:
        placedCows = 1
        prevIdx = 0

        for i in range(1, len(stalls)):
            if stalls[i] - stalls[prevIdx] >= minDistance:
                prevIdx = i
                placedCows += 1

            if placedCows >= cows:
                return True

        return False

    def aggressiveCows(self, stalls: list[int], k: int) -> int:
        stalls.sort()
        st, en = 1, stalls[-1] - stalls[0] + 1
        ans = -1

        for i in range(st, en):
            if self.canPlaceCows(stalls, i, k):
                ans = max(ans, i)
        return ans


# Optimal
# T.C. - O(N*log(max(stalls)))+O(Nlog(N))
# S.C  - O(1)

# Intuition
# First sort the give array as sorting will make our placements deterministic
# otherwise we might place cows too close or too far, we may miss out on optimal placemnts
# Sorting gives a predictable structure — so we can place cows in a left-to-right greedy manner
# These are like points on a number line. If the stalls aren't sorted, there's no structure
# Placing the first cow at the first stall gives maximum room for future cows to be placed at a distance of at least minDistance
# Do a binary search and keep going right as we want the max possible distance possible if we are able to place all cows
# otherwise go to left


class Solution:
    def canPlaceCows(self, stalls: list[int], minDistance: int, cows: int) -> bool:
        placedCows = 1
        prevIdx = 0

        for i in range(1, len(stalls)):
            if stalls[i] - stalls[prevIdx] >= minDistance:
                prevIdx = i
                placedCows += 1

            if placedCows >= cows:
                return True

        return False

    def aggressiveCows(self, stalls: list[int], k: int) -> int:
        stalls.sort()
        st, en = 1, stalls[-1] - stalls[0]
        ans = 0

        while st <= en:
            mid = st + (en - st) // 2

            if self.canPlaceCows(stalls, mid, k):
                ans = mid
                st = mid + 1
            else:
                en = mid - 1

        return ans
