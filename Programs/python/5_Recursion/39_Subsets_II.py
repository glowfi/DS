# https://leetcode.com/problems/subsets-ii/ , Medium

# Brute
# T.C. - O(2^n) + O(nlog(n))
# S.C  - O(n)


class Solution:
    def getSubsets(self, idx, tmp, arr, ans):
        if idx == len(arr):
            ans.append(tmp[:])
            return

        ans.append(tmp[:])

        for i in range(idx, len(arr)):
            if i > idx and arr[i] == arr[i - 1]:
                continue
            tmp.append(arr[i])
            self.getSubsets(i + 1, tmp, arr, ans)
            tmp.pop(-1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.getSubsets(0, [], nums, ans)
        return ans
