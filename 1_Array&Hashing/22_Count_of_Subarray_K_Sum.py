# https://leetcode.com/problems/subarray-sum-equals-k/description/,Medium

# Brute
# T.C. -> O(n^2)
# S.C. -> O(n)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    c += 1

        return c


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        count = {0: 1}
        pref = 0

        for i in range(len(nums)):
            pref += nums[i]
            remaining = pref - k

            if remaining in count:
                c += count[remaining]

            if pref not in count:
                count[pref] = 1
            else:
                count[pref] += 1

        return c
