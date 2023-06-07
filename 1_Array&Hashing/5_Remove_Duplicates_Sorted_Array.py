# https://leetcode.com/problems/remove-duplicates-from-sorted-array/,Easy

# Brute
# T.C. -> O(n)+O(nlog(n))+O(n)
# S.C. -> O(n)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = list(set(nums))
        st.sort()

        for i in range(len(st)):
            nums[i] = st[i]

        return len(st)


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
