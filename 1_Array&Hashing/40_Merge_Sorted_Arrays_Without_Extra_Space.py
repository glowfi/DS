# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1 , Medium

# Brute
# T.C. -> O(m+n)+O(m+n)
# S.C. -> O(m+n)


class Solution:
    def merge(self, arr1, arr2, n, m):
        ans = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                ans.append(arr1[i])
                i += 1

            elif arr2[j] <= arr1[i]:
                ans.append(arr2[j])
                j += 1

        while i < len(arr1):
            ans.append(arr1[i])
            i += 1

        while j < len(arr2):
            ans.append(arr2[j])
            j += 1

        idx = 0
        for i in range(len(arr1)):
            arr1[i] = ans[idx]
            idx += 1

        for i in range(len(arr2)):
            arr2[i] = ans[idx]
            idx += 1


# Optimal
# T.C. -> O(min(n1,n2))+O(n1log(n1))+O(n2log(n2))
# S.C. -> O(1)


class Solution:
    def merge(self, arr1, arr2, n, m):
        i, j = len(arr1) - 1, 0

        while i >= 0 and j < len(arr2):
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
                i -= 1
                j += 1
            else:
                break

        arr1.sort()
        arr2.sort()
