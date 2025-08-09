# https://leetcode.com/problems/longest-common-prefix , Easy, LCP

# Question
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.


# Optimal
# T.C. - O(S)
# S.C  - O(1)

# Intuition
# Take a comparison string suppose the first word in strs
# Keep checking each character of the comparison_str , whether its
# present in all words in the strs or not, if any time the char is
# not common or the character index is greater than length of the
# word we return as from that moment onwards we dont have longest
# prefix substring


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        comparison_str = strs[0]
        lcp = ""

        for i, char in enumerate(comparison_str):
            is_char_common = True
            for st in strs:
                if i + 1 > len(st) or st[i] != char:
                    is_char_common = False
                    return lcp
            if is_char_common:
                lcp += char

        return lcp
