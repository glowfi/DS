# https://leetcode.com/problems/sort-characters-by-frequency/ , Medium

# Optimal
# T.C. -> O(nlog(n))+O(n)+O(log(n))
# S.C. -> O(log(n))+O(n)


class Solution:
    def mergeSort(self, lo, hi, arr, freq):
        if lo >= hi:
            return

        mid = (lo + hi) // 2
        self.mergeSort(lo, mid, arr, freq)
        self.mergeSort(mid + 1, hi, arr, freq)
        self.merge(lo, mid, hi, arr, freq)

    def merge(self, lo, mid, hi, arr, freq):
        i, j = lo, mid + 1
        tmp = []

        while i <= mid and j <= hi:
            if freq[arr[i]] >= freq[arr[j]]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                j += 1

        while i <= mid:
            tmp.append(arr[i])
            i += 1

        while j <= hi:
            tmp.append(arr[j])
            j += 1

        k = 0
        for i in range(lo, hi + 1):
            arr[i] = tmp[k]
            k += 1

    def frequencySort(self, s: str) -> str:
        freq = {}

        for i in s:
            freq[i] = freq.get(i, 0) + 1

        ls = list(freq.keys())
        lo = 0
        hi = len(ls) - 1

        self.mergeSort(lo, hi, ls, freq)

        ans = ""

        for i in ls:
            ans += f"{i}" * freq[i]

        return ans
