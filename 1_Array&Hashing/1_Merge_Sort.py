# https://practice.geeksforgeeks.org/problems/merge-sort/1,Medium

# T.C. -> O(nlog(n))
# S.C. -> O(n)


class Solution:
    def merge(self, arr, l, m, r):
        i, j = l, m + 1
        s1 = m
        s2 = r
        tmp = []

        while i <= s1 and j <= s2:
            if arr[i] <= arr[j]:
                tmp.append(arr[i])
                i += 1
            elif arr[j] <= arr[i]:
                tmp.append(arr[j])
                j += 1

        while i <= s1:
            tmp.append(arr[i])
            i += 1

        while j <= s2:
            tmp.append(arr[j])
            j += 1

        k = 0
        for i in range(l, r + 1):
            arr[i] = tmp[k]
            k += 1

    def mergeSort(self, arr, l, r):
        if l >= r:
            return

        mid = (l + r) // 2

        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)
        self.merge(arr, l, mid, r)
