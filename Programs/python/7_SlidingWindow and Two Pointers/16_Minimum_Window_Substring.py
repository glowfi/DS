# https://leetcode.com/problems/minimum-window-substring/ , Hard

# Brute
# T.C. - O(n^2)
# S.C  - O(256)


from collections import defaultdict


class Solution:
    def hasAllcharacters(self, mp_s, mp_t):
        c = 0
        for key in mp_t:
            if key in mp_s and mp_s[key] >= mp_t[key]:
                c += 1
        return c == len(mp_t)

    def minWindow(self, s: str, t: str) -> str:
        min_window = ""
        min_window_size = float("inf")

        mp_t = defaultdict(int)
        for i in range(len(t)):
            mp_t[t[i]] += 1

        for i in range(len(s)):
            mp = defaultdict(int)
            for j in range(i, len(s)):
                mp[s[j]] += 1
                if self.hasAllcharacters(mp, mp_t):
                    curr_window_size = j - i + 1
                    if curr_window_size < min_window_size:
                        min_window = s[i : j + 1]
                        min_window_size = curr_window_size

        return min_window


# Brute
# T.C. - O(n^2)
# S.C  - o(256)


from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window = ""
        min_window_size = float("inf")

        for i in range(len(s)):
            mp_t = defaultdict(int)
            for j in range(len(t)):
                mp_t[t[j]] += 1
            c = 0
            for k in range(i, len(s)):
                if mp_t[s[k]] > 0:
                    c += 1
                mp_t[s[k]] -= 1

                if c == len(t):
                    if k - i + 1 < min_window_size:
                        min_window = s[i : k + 1]
                        min_window_size = k - i + 1
                        break

        return min_window


# Optimal
# T.C. - O(m)+O(2n)
# S.C  - O(256)


from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window = ""
        min_window_size = float("inf")

        l, r = 0, 0
        mp_t = defaultdict(int)

        for i in range(len(t)):
            mp_t[t[i]] += 1

        c = 0

        while r < len(s):
            if mp_t[s[r]] > 0:
                c += 1

            mp_t[s[r]] -= 1

            while c == len(t):
                if r - l + 1 < min_window_size:
                    min_window_size = r - l + 1
                    min_window = s[l : r + 1]

                # while shrinking we are adding back elements
                mp_t[s[l]] += 1
                if mp_t[s[l]] > 0:
                    c -= 1

                l += 1

            r += 1

        return min_window
