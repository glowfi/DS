# NA,Easy

# Optimal (Iterative)
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] < target:
                hi = mid - 1

            elif nums[mid] > target:
                lo = mid + 1

            else:
                return mid

        return -1


# Optimal (Recursive)
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def bs(self, st, en, nums, target):
        if st > en:
            return -1

        mid = (st + en) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            return self.bs(mid + 1, en, nums, target)

        else:
            return self.bs(st, mid - 1, nums, target)

    def search(self, nums, target):
        return self.bs(0, len(nums) - 1, nums, target)
