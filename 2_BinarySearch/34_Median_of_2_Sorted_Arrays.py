# https://leetcode.com/problems/median-of-two-sorted-arrays/ , Hard


# Brute
# T.C. -> O(n+m)
# S.C. -> O(n+m)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        tmp = []

        if len(nums1) == 0 and len(nums2) == 0:
            return 0

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1

        while i < n1:
            tmp.append(nums1[i])
            i += 1

        while j < n2:
            tmp.append(nums2[j])
            j += 1

        n = len(tmp)
        mid = n // 2

        # Odd Length
        if n % 2 != 0:
            return tmp[mid]

        # Even Length
        sm = tmp[mid] + tmp[mid - 1]
        return sm / 2


# Better
# T.C. -> O(n+m)
# S.C. -> O(1)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        mid = n // 2

        ind1, ind2 = mid - 1, mid
        mid1, mid2 = -1, -1

        idx = 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                if idx == ind1:
                    mid1 = nums1[i]
                elif idx == ind2:
                    mid2 = nums1[i]
                idx += 1
                i += 1
            else:
                if idx == ind1:
                    mid1 = nums2[j]
                elif idx == ind2:
                    mid2 = nums2[j]
                idx += 1
                j += 1

        while i < n1:
            if idx == ind1:
                mid1 = nums1[i]
            elif idx == ind2:
                mid2 = nums1[i]
            idx += 1
            i += 1

        while j < n2:
            if idx == ind1:
                mid1 = nums2[j]
            elif idx == ind2:
                mid2 = nums2[j]
            idx += 1
            j += 1

        # Odd Length
        if n % 2 != 0:
            return mid2

        # Even Length
        sm = (mid1 + mid2) / 2
        return sm


# Optimal
# T.C. -> O(log(min(n,m)))
# S.C. -> O(1)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass
