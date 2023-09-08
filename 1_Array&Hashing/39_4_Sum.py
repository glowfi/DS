# https://leetcode.com/problems/4sum/ , Medium

# Brute
# T.C -> O(N^4)+O(nlog(n))
# S.C -> O(no of unique triplets)


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        sm = nums[i] + nums[j] + nums[k] + nums[l]

                        if sm == target:
                            ans.add((nums[i], nums[j], nums[k], nums[l]))

        return ans


# Better
# T.C -> O(N^3)+O(nlog(n))
# S.C -> O(N)+O(no of unique triplets)


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                h = {}
                tar = target - nums[i] - nums[j]
                for k in range(j + 1, len(nums)):
                    diff = tar - nums[k]

                    if diff in h:
                        ans.add((nums[i], nums[j], nums[h[diff]], nums[k]))

                    h[nums[k]] = k

        return ans


# Optimal
# T.C -> O(N^2)+O(nlog(n))
# S.C -> O(no of unique triplets)


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums) - 4 + 1):
            if nums[i] == nums[i - 1] and i != 0:
                continue
            for j in range(i + 1, len(nums) - 3 + 1):
                if nums[j] == nums[j - 1] and j > i + 1:
                    continue
                k, l = j + 1, len(nums) - 1
                while k < l:
                    sm = nums[i] + nums[j] + nums[k] + nums[l]

                    if sm == target:
                        ans.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1

                        while nums[k] == nums[k - 1] and l > k:
                            k += 1

                        while nums[l] == nums[l + 1] and l > k:
                            l -= 1

                    elif sm > target:
                        l -= 1

                    elif sm < target:
                        k += 1

        return ans
