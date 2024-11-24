# https://leetcode.com/problems/count-number-of-nice-subarrays/ , Medium


# Optimal
# T.C. - O(2n)
# S.C  - O(1)


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        sm = 0
        c = 0
        count_zeroes = 0

        while r < len(nums):
            sm += 0 if nums[r] % 2 == 0 else 1

            while l < r and (sm > k or nums[l] % 2 == 0):
                if nums[l] % 2 == 0:
                    count_zeroes += 1
                else:
                    count_zeroes = 0
                sm -= 0 if nums[l] % 2 == 0 else 1
                l += 1

            if sm == k:
                c += 1 + count_zeroes

            r += 1

        return c
