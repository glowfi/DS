# https://leetcode.com/problems/search-in-rotated-sorted-array/ , Medium


# Better
# T.C. -> O(log(n))
# S.C. -> O(n)


class Solution:
    def helper(self, st, en, arr, tar):
        # Not Found
        if st > en:
            return -1

        mid = (st + en) // 2

        # Found
        if arr[mid] == tar:
            return mid

        # Identify which portion of array is sorted
        if arr[st] <= arr[mid]:
            if arr[st] <= tar and tar <= arr[mid]:
                return self.helper(st, mid - 1, arr, tar)
            else:
                return self.helper(mid + 1, en, arr, tar)
        else:
            if arr[mid] <= tar and tar <= arr[en]:
                return self.helper(mid + 1, en, arr, tar)
            else:
                return self.helper(st, mid - 1, arr, tar)

    def search(self, nums: List[int], target: int) -> int:
        return self.helper(0, len(nums) - 1, nums, target)
