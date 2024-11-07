# https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1 , Medium

# Brute
# T.C. - O(N^2)
# S.C  - O(n)


class Solution:

    def longestKSubstr(self, s, k):
        mx_len = -1
        for i in range(len(s)):
            hmap = {}
            for j in range(i, len(s)):
                if s[j] not in hmap:
                    hmap[s[j]] = 1
                else:
                    hmap[s[j]] += 1

                if len(hmap) > k:
                    break

                if len(hmap) == k:
                    mx_len = max(mx_len, j - i + 1)

        return mx_len


# Better
# T.C. - O(2n)
# S.C  - O(n)


class Solution:

    def longestKSubstr(self, s, k):
        hmap = {}
        l, r = 0, 0
        n = len(s)
        mx_len = -1

        while r < n:
            currChar = s[r]
            if currChar not in hmap:
                hmap[currChar] = 1
            else:
                hmap[currChar] += 1

            while len(hmap) > k:
                if hmap[s[l]] - 1 == 0:
                    del hmap[s[l]]
                else:
                    hmap[s[l]] -= 1
                l += 1

            if len(hmap) == k:
                mx_len = max(mx_len, r - l + 1)

            r += 1

        return mx_len


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:

    def longestKSubstr(self, s, k):
        hmap = {}
        l, r = 0, 0
        n = len(s)
        mx_len = -1

        while r < n:
            currChar = s[r]
            if currChar not in hmap:
                hmap[currChar] = 1
            else:
                hmap[currChar] += 1

            if len(hmap) > k:
                if hmap[s[l]] - 1 == 0:
                    del hmap[s[l]]
                else:
                    hmap[s[l]] -= 1
                l += 1

            if len(hmap) == k:
                mx_len = max(mx_len, r - l + 1)

            r += 1

        return mx_len
