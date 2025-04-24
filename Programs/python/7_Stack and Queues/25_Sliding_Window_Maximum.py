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
# T.C. - O(2n)
# S.C  - O(n)


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, -1
        dq = deque([])
        n = len(nums)
        ans = []

        for i in range(k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)
            r += 1

        ans.append(nums[dq[0]])

        while r < n - 1:
            l += 1
            while dq and dq[0] < l:
                dq.popleft()

            r += 1
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()

            dq.append(r)

            ans.append(nums[dq[0]])

        return ans
