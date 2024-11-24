# https://leetcode.com/problems/binary-subarrays-with-sum/ , Medium


# Better
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hmap = {0: 1}
        c = 0
        pref = 0

        for i in range(len(nums)):
            pref += nums[i]
            rem = pref - goal

            if rem in hmap:
                c += hmap[rem]

            if pref not in hmap:
                hmap[pref] = 1
            else:
                hmap[pref] += 1

        return c


# Optimal
# T.C. - O(2n)
# S.C  - o(1)


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l, r = 0, 0
        sm = 0
        c = 0
        count_zeroes = 0

        while r < len(nums):
            sm += nums[r]

            while l < r and (sm > goal or nums[l] == 0):
                if nums[l] == 0:
                    count_zeroes += 1
                else:
                    count_zeroes = 0
                sm -= nums[l]
                l += 1

            if sm == goal:
                c += 1 + count_zeroes

            r += 1

        return c
