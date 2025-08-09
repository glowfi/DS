# https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1 , Hard, BS-on-Ans

# Question
# Ram wants to paint his dog's home that has n boards with different lengths. The length of ith board is given
# by arr[i] where arr[] is an array of n integers. He hired k painters for this work and each painter takes 1 unit time to paint 1 unit of the board.

# Return the minimum time to get this job done if all painters start together with the constraint that any painter
# will only paint continuous boards, say boards numbered [2,3,4] or only board [1] or nothing but not boards [2,4,5].

# Examples:

# Input: arr[] = [5, 10, 30, 20, 15], k = 3
# Output: 35
# Explanation: The most optimal way will be: Painter 1 allocation : [5,10],
# Painter 2 allocation : [30], Painter 3 allocation : [20,15], Job will be done when all painters finish i.e. at time = max(5+10, 30, 20+15) = 35

# Input: arr[] = [10, 20, 30, 40], k = 2
# Output: 60
# Explanation: The most optimal way to paint: Painter 1 allocation : [10,20,30], Painter 2 allocation : [40], Job will be complete at time = 60

# Input: arr[] = [100, 200, 300, 400], k = 1
# Output: 1000
# Explanation: There is only one painter, so the painter must paint all boards sequentially. The total time taken will be the sum of all board lengths, i.e., 100 + 200 + 300 + 400 = 1000.

# Constraints:
# 1 ≤ arr.size() ≤ 10^5
# 1 ≤ arr[i] ≤ 10^5
# 1 ≤ k ≤ 10^5

# Brute
# T.C. - O(N*sum(books))
# S.C  - O(1)

# Intuition
# Do a linear search and the first time you
# see that we are able to allocate books to
# fewer than k a painters we return the current min
# page value


class Solution:
    def isPossible(self, maxTime: int, arr: list[int], k: int) -> bool:
        paintersAllocated = 0
        currBoardLength = maxTime

        for val in arr:
            if val <= currBoardLength:
                currBoardLength -= val
            else:
                paintersAllocated += 1
                currBoardLength = maxTime
                currBoardLength -= val

        if currBoardLength >= 0:
            paintersAllocated += 1

        return paintersAllocated <= k

    def minTime(self, arr: list[int], k: int) -> int:
        st, en = max(arr), sum(arr) + 1

        for i in range(st, en):
            if self.isPossible(i, arr, k):
                return i
        return -1


# Optimal
# T.C. - O(N*log(sum(books)))
# S.C  - O(1)

# Intuition
# Do a binary search if painter allocation is possible
# go as left as possible to get min page otherwise
# go right


class Solution:
    def isPossible(self, maxTime: int, arr: list[int], k: int) -> bool:
        paintersAllocated = 0
        currBoardLength = maxTime

        for val in arr:
            if val <= currBoardLength:
                currBoardLength -= val
            else:
                paintersAllocated += 1
                currBoardLength = maxTime
                currBoardLength -= val

        if currBoardLength >= 0:
            paintersAllocated += 1

        return paintersAllocated <= k

    def minTime(self, arr: list[int], k: int) -> int:
        st, en = max(arr), sum(arr)
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2

            if self.isPossible(mid, arr, k):
                ans = mid
                en = mid - 1
            else:
                st = mid + 1

        return ans
