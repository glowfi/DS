# https://leetcode.com/problems/longest-repeating-character-replacement/ , Medium

# Brute
# T.C. - O(n^2)
# S.C  - O(26)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_rep = 0
        for i in range(len(s)):
            hmap = {}
            max_freq = float("-inf")
            for j in range(i, len(s)):
                if s[j] not in hmap:
                    hmap[s[j]] = 1
                else:
                    hmap[s[j]] += 1
                max_freq = max(hmap[s[j]], max_freq)
                left_characters_that_can_be_replaced = (j - i + 1) - max_freq
                if left_characters_that_can_be_replaced <= k:
                    longest_rep = max(longest_rep, j - i + 1)

        return longest_rep


# Optimal
# T.C. - O(2n)
# S.C  - O(26)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hmap = {}
        max_freq = float("-inf")
        longest_rep = 0

        while r < len(s):
            if s[r] in hmap:
                hmap[s[r]] += 1
            else:
                hmap[s[r]] = 1

            max_freq = max(hmap[s[r]], max_freq)

            while (r - l + 1) - max_freq > k:
                if hmap[s[l]] - 1 == 0:
                    del hmap[s[l]]
                else:
                    hmap[s[l]] -= 1
                l += 1

            longest_rep = max(r - l + 1, longest_rep)

            r += 1

        return longest_rep
