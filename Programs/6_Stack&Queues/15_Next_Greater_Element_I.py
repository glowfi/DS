#  https://leetcode.com/problems/next-greater-element-i/ , Easy


# Optimal
# T.C. - O(n1)+O(n2)
# S.C  - O(n1)+O(n2)


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        mp = {}

        for i in range(len(nums2) - 1, -1, -1):
            while stk and nums2[stk[-1]] <= nums2[i]:
                stk.pop(-1)

            if stk:
                mp[nums2[i]] = nums2[stk[-1]]
            else:
                mp[nums2[i]] = -1

            stk.append(i)

        out = []
        for i in range(len(nums1)):
            out.append(mp[nums1[i]])

        return out
