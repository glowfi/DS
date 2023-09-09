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
    def getnumofElements(self, n1, n2):
        return (n1 + n2 + 1) // 2

    def getMedian(self, a, b):
        n1, n2 = len(a), len(b)

        st, en = 0, len(a)

        while st <= en:
            totalElements = self.getnumofElements(n1, n2)

            partA = st + (en - st) // 2
            partB = totalElements - partA

            l1 = float("-inf") if partA == 0 else a[partA - 1]
            r1 = float("inf") if partA == n1 else a[partA]

            l2 = float("-inf") if partB == 0 else b[partB - 1]
            r2 = float("inf") if partB == n2 else b[partB]

            if l1 > r2:
                en = partA - 1
            elif l2 > r1:
                st = partA + 1
            elif l1 <= r2 and l2 <= r1:
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
        return 0

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)

        # Means nums 2 is smaller
        if n1 > n2:
            return self.getMedian(nums2, nums1)

        # Means nums 1 is smaller
        else:
            return self.getMedian(nums1, nums2)
