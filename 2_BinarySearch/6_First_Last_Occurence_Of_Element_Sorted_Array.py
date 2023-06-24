# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/,Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def findOccurence(self, nums, target):
        first, last = -1, -1
        c = 0

        for i in range(len(nums)):
            if nums[i] == target:
                last = i
                c += 1
            elif nums[i] > target:
                break

        if last == -1:
            return [-1, -1]
        else:
            return [last - c + 1, last]

    def searchRange(self, nums, target):
        return self.findOccurence(nums, target)


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def findOccurence(self, nums, target, type):
        st, en = 0, len(nums) - 1
        ans = -1

        while st <= en:
            mid = (st + en) // 2

            if nums[mid] > target:
                en = mid - 1

            elif nums[mid] < target:
                st = mid + 1

            else:
                ans = mid

                if type == "first":
                    en = mid - 1
                else:
                    st = mid + 1
        return ans

    def searchRange(self, nums, target):
        first = self.findOccurence(nums, target, "first")
        last = self.findOccurence(nums, target, "last")
        return [first, last]
