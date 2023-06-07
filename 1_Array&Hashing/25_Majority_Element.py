# https://leetcode.com/problems/majority-element/description/,Easy

# Brute
# T.C. -> O(n^2)
# S.C. -> O(1)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mx = -1
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1
            if cnt > (len(nums) // 2):
                mx = nums[i]
        return mx


# Better
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mx = -1
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = 1 + h.get(nums[i], 0)

        for i in h:
            if h[i] > (len(nums) // 2):
                mx = i

        return mx


# Optimal
# T.C. -> O(n)+O(n)
# S.C. -> O(1)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el, c = 0, 0

        for i in range(len(nums)):
            if c == 0:
                c = 1
                el = nums[i]

            elif nums[i] != el:
                c -= 1
            else:
                c += 1

        c1 = 0
        for i in nums:
            if i == el:
                c1 += 1

        if c1 > len(nums) // 2:
            return el
        return -1
