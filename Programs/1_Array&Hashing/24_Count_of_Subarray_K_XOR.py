# https://www.codingninjas.com/codestudio/problems/count-subarrays-with-given-xor_1115652,Medium

# Brute
# T.C. -> O(n^2)
# S.C. -> O(n)


class Solution:
    def subarrayXor(self, arr, m):
        c = 0

        for i in range(len(arr)):
            xor = 0
            for j in range(i, len(arr)):
                xor ^= arr[j]
                if xor == m:
                    c += 1

        return c


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def subarrayXor(self, arr, m):
        hmap = {0: 1}
        c = 0

        pref_xor = 0

        for i in range(len(arr)):
            pref_xor ^= arr[i]
            want_xor = pref_xor ^ m
            if want_xor in hmap:
                c += hmap[want_xor]

            if pref_xor in hmap:
                hmap[pref_xor] += 1
            else:
                hmap[pref_xor] = 1

        return c
