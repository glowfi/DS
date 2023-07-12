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


class Solution(object):
    def search(self, nums, target):
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = st + ((en - st) // 2)

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                en = mid - 1

            else:
                st = mid + 1

        return -1


# Optimal (Recursive)
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def search(self, nums, target):
        def bs(st, en):
            if st > en:
                return -1

            mid = st + ((en - st) // 2)

            if nums[mid] == target:
                return mid

            # Go Left
            elif nums[mid] > target:
                return bs(st, mid - 1)

            # Go Right
            else:
                return bs(mid + 1, en)

        return bs(0, len(nums) - 1)
