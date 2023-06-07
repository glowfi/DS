# https://practice.geeksforgeeks.org/problems/longest-subarray-with-sum-divisible-by-k1259/1,Medium

# Brute
# T.C. -> O(n^2)
# S.C. -> O(n)


class Solution:
    def longSubarrWthSumDivByK(self, arr, n, K):
        mx = 0
        for i in range(len(arr)):
            sum = 0
            for j in range(i, len(arr)):
                sum += arr[j]
                if sum % K == 0:
                    mx = max(mx, j - i + 1)
        return mx


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def longSubarrWthSumDivByK(self, arr, n, K):
        mx = 0
        r = {0: -1}
        pref = 0

        for i in range(len(arr)):
            pref += arr[i]
            rem = pref % K

            if rem < 0:
                rem += K

            if rem in r:
                mx = max(mx, i - r[rem])

            if rem not in r:
                r[rem] = i

        return mx
