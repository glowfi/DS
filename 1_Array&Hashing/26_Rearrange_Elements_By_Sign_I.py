# https://leetcode.com/problems/rearrange-array-elements-by-sign/,Medium

# Brute
# T.C. -> O(n)+O(n)
# S.C. -> O(n/2)+O(n/2) = O(n)


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])

        p, n = 0, 0

        for i in range(len(nums)):
            # Place Positive at even index
            if i % 2 == 0:
                nums[i] = pos[p]
                p += 1
            # Place Negative at odd index
            else:
                nums[i] = neg[n]
                n += 1
        return nums


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        pos = 0
        neg = 1

        for i in range(len(nums)):
            if nums[i] > 0:
                ans[pos] = nums[i]
                pos += 2
            else:
                ans[neg] = nums[i]
                neg += 2

        return ans
