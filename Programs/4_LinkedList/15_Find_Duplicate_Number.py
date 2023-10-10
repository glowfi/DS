# https://leetcode.com/problems/find-the-duplicate-number/description/ , Medium

# Brute
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = {}

        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = 1
            else:
                return nums[i]


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # Cycle Exist
            if slow == fast:
                slow = 0

                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]

                return slow
