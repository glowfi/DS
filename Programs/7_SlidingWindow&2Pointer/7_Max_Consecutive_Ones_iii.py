# https://leetcode.com/problems/max-consecutive-ones-iii/ , Medium

# Brute
# T.C. - O(N^2)
# S.C  - O(1)


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        mx_len = 0

        for i in range(len(nums)):
            c = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    c += 1

                if c > k:
                    break
                mx_len = max(mx_len, j - i + 1)

        return mx_len


# Better
# T.C. - O(2n)
# S.C  - O(1)


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        n = len(nums)
        cnt_zeroes = 0
        mx_len = 0

        while r < n:
            if nums[r] == 0:
                cnt_zeroes += 1

            while cnt_zeroes > k:
                if nums[l] == 0:
                    cnt_zeroes -= 1
                l += 1

            if cnt_zeroes <= k:
                mx_len = max(mx_len, r - l + 1)

            r += 1

        return mx_len


# Optimal
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        n = len(nums)
        cnt_zeroes = 0
        mx_len = 0

        while r < n:
            if nums[r] == 0:
                cnt_zeroes += 1

            if cnt_zeroes > k:
                if nums[l] == 0:
                    cnt_zeroes -= 1
                l += 1

            if cnt_zeroes <= k:
                mx_len = max(mx_len, r - l + 1)

            r += 1

        return mx_len
