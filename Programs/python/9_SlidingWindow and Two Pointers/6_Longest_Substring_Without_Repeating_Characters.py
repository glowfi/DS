# https://leetcode.com/problems/longest-substring-without-repeating-characters/ , Medium

# Brute
# T.C. - O(N^2)
# S.C  - O(N)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx_len = 0

        for i in range(len(s)):
            st = set()
            for j in range(i, len(s)):
                if s[j] in st:
                    break
                else:
                    st.add(s[j])
                    mx_len = max(mx_len, j - i + 1)

        return mx_len


# Optimal
# T.C. - O(N)
# S.C  - O(N)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hmap = {}
        mx_len = 0

        while r < len(s):
            currChar = s[r]

            if currChar in hmap:
                if hmap[currChar] >= l:
                    l = hmap[currChar] + 1

            hmap[currChar] = r
            mx_len = max(mx_len, r - l + 1)
            r += 1

        return mx_len
