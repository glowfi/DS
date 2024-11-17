# https://leetcode.com/problems/contiguous-array/ , Medium

# Cant Apply sliding window

# Better
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hmap = {0: -1}
        pref = 0
        mx_len = 0
        k = 0

        for i in range(len(nums)):
            pref += 1 if nums[i] else -1

            want_sum = pref - k
            if want_sum in hmap:
                mx_len = max(mx_len, i - hmap[want_sum])

            if want_sum not in hmap:
                hmap[want_sum] = i

        return mx_len


# Optimal
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sm = 0
        mx_len = 0
        k = 0
        l, r = 0, 0
        n = len(nums)

        while r < n:
            sm += nums[r]

            while sm > k:
                sm -= nums[l]
                l += 1

            if sm == k:
                mx_len = max(mx_len, r - l + 1)

            r += 1

        return mx_len
