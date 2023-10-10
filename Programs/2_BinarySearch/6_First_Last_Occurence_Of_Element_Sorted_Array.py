# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/,Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def searchRange(self, nums, target):
        first, last = -1, -1
        c = 0

        for i in range(len(nums)):
            if nums[i] == target:
                last = i
                c += 1
            if nums[i] > target and nums[i] != target:
                break

        if c == 0:
            return [-1, -1]

        first = last - c + 1
        return [first, last]


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def search(self, arr, X, _type):
        st, en = 0, len(arr) - 1
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2

            if arr[mid] == X:
                ans = mid
                if _type == "first":
                    en = mid - 1
                else:
                    st = mid + 1

            elif arr[mid] < X:
                st = mid + 1

            elif arr[mid] > X:
                en = mid - 1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = self.search(nums, target, "first"), self.search(
            nums, target, "last"
        )

        return [first, last]
