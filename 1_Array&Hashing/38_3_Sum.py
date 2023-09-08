# https://leetcode.com/problems/3sum/description/ , Medium

# Brute
# T.C -> O(N^3)+O(nlog(n))
# S.C -> O(no of unique triplets)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    sm = nums[i] + nums[j] + nums[k]
                    if sm == 0 and (nums[i], nums[j], nums[k]) not in ans:
                        ans.add((nums[i], nums[j], nums[k]))

        return ans


# Better
# T.C -> O(N^2)+O(nlog(n))
# S.C -> O(N)+O(no of unique triplets)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            h = {}
            target = nums[i] * -1
            for j in range(i + 1, len(nums)):
                diff = target - nums[j]
                if diff in h:
                    ans.add((nums[h[diff]], nums[j], target * -1))
                h[nums[j]] = j
        return ans


# Optimal
# T.C -> O(N^2)+O(nlog(n))
# S.C -> O(no of unique triplets)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums) - 3 + 1):
            if nums[i] == nums[i - 1] and i != 0:
                continue

            target = nums[i] * -1
            j, k = i + 1, len(nums) - 1

            while j < k:
                sm = nums[i] + nums[j] + nums[k]

                if sm == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

                    while nums[k] == nums[k + 1] and k > j:
                        k -= 1

                elif sm > 0:
                    k -= 1

                elif sm < 0:
                    j += 1

        return ans
