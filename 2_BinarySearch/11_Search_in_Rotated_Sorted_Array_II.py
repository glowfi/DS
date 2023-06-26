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

            # If target found
            if nums[mid] == target:
                return True

            # Check if element at st,mid,en are equal or not
            if nums[st] == nums[mid] == nums[en]:
                st += 1
                en -= 1
                continue

            # Identify Sorted Part
            # Check if target exists in the sorted part and eliminate the part not conatining the target

            # If left half is sorted
            elif nums[st] <= nums[mid]:
                # Target is in left half
                if nums[st] <= target and target <= nums[mid]:
                    en = mid - 1
                else:
                    st = mid + 1

            # If right half is sorted
            else:
                # Target is in right half
                if nums[mid] <= target and target <= nums[en]:
                    st = mid + 1
                else:
                    en = mid - 1

        return False
