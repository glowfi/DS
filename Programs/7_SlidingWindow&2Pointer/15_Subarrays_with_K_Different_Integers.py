# https://leetcode.com/problems/subarrays-with-k-different-integers , Hard

# Brute
# T.C. - O(n^2)
# S.C  - O(n)


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        c = 0
        for i in range(len(nums)):
            mp = {}
            for j in range(i, len(nums)):
                if nums[j] in mp:
                    mp[nums[j]] += 1
                else:
                    mp[nums[j]] = 1

                if len(mp) > k:
                    break

                if len(mp) == k:
                    c += 1

        return c


# Optimal
# T.C. - O(2n)
# S.C  - O(n)

from collections import defaultdict


class Solution:
    def solve(self, nums, k):
        l, r = 0, 0
        mp = defaultdict(int)
        c = 0

        while r < len(nums):
            mp[nums[r]] += 1

            while len(mp) > k:
                if mp[nums[l]] - 1 == 0:
                    del mp[nums[l]]
                else:
                    mp[nums[l]] -= 1
                l += 1

            c += r - l + 1

            r += 1

        return c

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.solve(nums, k) - self.solve(nums, k - 1)
