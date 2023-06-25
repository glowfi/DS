# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/,Medium

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def search(self, nums, target):
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = (st + en) // 2

            if nums[mid] == target:
                return True

            if nums[mid] == nums[en] and nums[mid] == nums[st]:
                st += 1
                en -= 1
                continue

            # Find the sorted Part

            # If right Half is sorted
            if nums[mid] <= nums[en]:
                # if target lies in right part proceed
                if nums[mid] <= target and target <= nums[en]:
                    st = mid + 1
                else:
                    en = mid - 1

            # If left Half is sorted
            else:
                # if target lies in right part proceed
                if nums[st] <= target and target <= nums[mid]:
                    en = mid - 1
                else:
                    st = mid + 1

        return False
