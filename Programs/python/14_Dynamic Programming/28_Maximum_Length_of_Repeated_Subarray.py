# https://leetcode.com/problems/maximum-length-of-repeated-subarray/ , Medium


# Tabulation
# T.C. - O(ind1*ind2)
# S.C  - O(ind1*ind2)


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]

        ans = 0

        for ind1 in range(len(nums1) + 1):
            for ind2 in range(len(nums2) + 1):
                if ind1 == 0 or ind2 == 0:
                    dp[ind1][ind2] = 0
                else:
                    match = 0
                    notMatch = 0
                    if nums1[ind1 - 1] == nums2[ind2 - 1]:
                        match = 1 + dp[ind1 - 1][ind2 - 1]
                    else:
                        notMatch = 0

                    dp[ind1][ind2] = max(match, notMatch)
                    ans = max(match, notMatch, ans)

        return ans


# Space Optimized
# T.C. - O(ind1*ind2)
# S.C  - O(ind2)


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0 for _ in range(len(nums2) + 1)]
        ans = 0

        ans = 0

        for ind1 in range(len(nums1) + 1):
            tmp = [0 for _ in range(len(nums2) + 1)]
            for ind2 in range(len(nums2) + 1):
                if ind1 == 0 or ind2 == 0:
                    tmp[ind2] = 0
                else:
                    match = 0
                    notMatch = 0
                    if nums1[ind1 - 1] == nums2[ind2 - 1]:
                        match = 1 + dp[ind2 - 1]
                    else:
                        notMatch = 0

                    tmp[ind2] = max(match, notMatch)
                    ans = max(match, notMatch, ans)
            dp = tmp

        return ans
