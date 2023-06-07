# https://leetcode.com/problems/longest-consecutive-sequence/,Medium

# Brute
# T.C. -> O(nlog(n))+O(n)
# S.C. -> O(n)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()

        streak = 1
        maxStreak = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                streak += 1
            elif nums[i - 1] - nums[i] == 0:
                continue
            else:
                streak = 1
            maxStreak = max(maxStreak, streak)

        return maxStreak


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        mx = 0

        for i in range(len(nums)):
            # If start point
            if not nums[i] - 1 in st:
                streak = 0
                curr = nums[i]
                while curr in st:
                    streak += 1
                    curr += 1
                mx = max(streak, mx)
        return mx
