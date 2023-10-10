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
            mid = st + ((en - st) // 2)

            # If element is Found
            if nums[mid] == target:
                return True

            # Remove Duplicate elements cases
            if nums[st] == nums[mid] and nums[mid] == nums[en]:
                st += 1
                en -= 1
                continue

            ### Idenify the part that is sorted and check the target is present in sorted part or not

            ## Right Half is sorted
            elif nums[mid] <= nums[en]:
                # Check if target is present
                if nums[mid] <= target and target <= nums[en]:
                    st = mid + 1
                else:
                    en = mid - 1

            ## Left Half is sorted
            else:
                # Check if target is present
                if nums[st] <= target and target <= nums[mid]:
                    en = mid - 1
                else:
                    st = mid + 1

        return False
