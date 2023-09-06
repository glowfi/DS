# https://leetcode.com/problems/binary-search/,Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


# Optimal (Iterative)
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = (st) + (en - st) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                st = mid + 1

            elif nums[mid] > target:
                en = mid - 1

        return -1


# Optimal (Recursive)
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def bsRecursive(self, nums, st, en, target):
        if st > en:
            return -1

        mid = st + (en - st) // 2

        if nums[mid] < target:
            return self.bsRecursive(nums, mid + 1, en, target)

        elif nums[mid] > target:
            return self.bsRecursive(nums, st, mid - 1, target)

        else:
            return mid

    def search(self, nums: List[int], target: int) -> int:
        st, en = 0, len(nums) - 1

        return self.bsRecursive(nums, st, en, target)
