# https://leetcode.com/problems/majority-element-ii/description/ ,Medium


# Brute
# T.C. -> O(n^2)
# S.C. -> O(nums of majority element)


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = set()

        for i in range(len(nums)):
            if nums[i] in ans:
                continue
            cnt = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1
            if cnt > len(nums) // 3:
                ans.add(nums[i])

        return ans


# Better
# T.C. -> O(n)+O(n)
# S.C. -> O(n)+O(nums of majority element)


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        ans = []
        for i in count:
            if count[i] > len(nums) // 3:
                ans.append(i)

        return ans
