# https://leetcode.com/problems/maximum-product-subarray/ , Medium

# i<j and arr[i]>2*arr[j]

# Brute
# T.C. -> O(n^2)
# S.C. -> O(1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mxp = float("-inf")

        for i in range(len(nums)):
            p = 1
            for j in range(i, len(nums)):
                p *= nums[j]
                mxp = max(mxp, p)
        return mxp


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref = 1
        suff = 1
        mxp = float("-inf")
        n = len(nums)

        for i in range(len(nums)):
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1

            pref *= nums[i]
            suff *= nums[n - i - 1]

            mxp = max(mxp, suff, pref)

        return mxp
