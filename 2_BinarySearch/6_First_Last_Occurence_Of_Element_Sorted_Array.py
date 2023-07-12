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


class Solution(object):
    def getPosition(self, nums, target, type):
        st, en = 0, len(nums) - 1
        ans = -1

        while st <= en:
            mid = st + ((en - st) // 2)

            if nums[mid] == target:
                ans = mid

                if type == "first":
                    en = mid - 1
                elif type == "last":
                    st = mid + 1

            elif nums[mid] > target:
                en = mid - 1

            else:
                st = mid + 1
        return ans

    def searchRange(self, nums, target):
        first = self.getPosition(nums, target, "first")
        if first == -1:
            return [-1, -1]
        last = self.getPosition(nums, target, "last")
        return [first, last]
