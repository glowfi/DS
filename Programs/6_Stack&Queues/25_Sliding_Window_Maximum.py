# https://leetcode.com/problems/sliding-window-maximum/ , Hard

# Brute
# T.C. - O(N-k)*k
# S.C  - O(N-k)

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        for i in range(len(nums) - k + 1):
            mx = float("-inf")
            for j in range(i, i + k):
                mx = max(mx, nums[j])
            ans.append(mx)

        return ans


# Optimal
# T.C. -
# S.C  -
