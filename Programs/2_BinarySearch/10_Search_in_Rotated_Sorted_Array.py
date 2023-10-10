# https://leetcode.com/problems/search-in-rotated-sorted-array/,Medium

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


# Better
# T.C. -> O(log(n))+O(log(n))
# S.C. -> O(1)


class Solution(object):
    def bs(self, arr, X, st, en):
        while st <= en:
            mid = st + ((en - st) // 2)

            if arr[mid] == X:
                return mid

            elif arr[mid] > X:
                en = mid - 1

            else:
                st = mid + 1
        return -1

    def findMin(self, nums):
        n = len(nums)
        st, en = 1, n - 2

        while st <= en:
            mid = st + ((en - st) // 2)

            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return mid

            # Identify the unsorted part as the minimum elemeny will be present in the unsorted part (By Observation)

            # Right Half is sorted and left half is unsorted
            elif nums[mid] < nums[en]:
                en = mid - 1

            # Left Half is sorted and right half is unsorted
            else:
                st = mid + 1

        if nums[0] < nums[n - 1]:
            return 0
        return n - 1

    def search(self, nums, target):
        getMin = self.findMin(nums)
        print(getMin)

        first = self.bs(nums, target, 0, getMin - 1)
        if first != -1:
            return first
        return self.bs(nums, target, getMin, len(nums) - 1)


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def search(self, nums, target):
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = st + ((en - st) // 2)

            # Found the element
            if nums[mid] == target:
                return mid

            ### Identify the sorted part and check whether the element is present in the sorted part or not

            ## Right half is sorted
            elif nums[mid] <= nums[en]:
                # Target is in right half
                if nums[mid] <= target and target <= nums[en]:
                    st = mid + 1
                else:
                    en = mid - 1

            ## Left half is sorted
            else:
                # Target is in left half
                if nums[st] <= target and target <= nums[mid]:
                    en = mid - 1
                else:
                    st = mid + 1
        return -1
