# https://leetcode.com/problems/group-anagrams, Medium, HashMap / Sorting Key

# Question
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Optimal
# T.C. - O(n*k)
# S.C  -  O(n*k+m)

# Intuition
# Group all the words by their frequency count array

from collections import defaultdict
from typing import List


class Solution:
    def get_freq_string(self, s: str) -> str:
        counter_map = [0] * 26
        for ch in s:
            counter_map[ord(ch) - 97] += 1

        res = ""
        for i in range(len(counter_map)):
            if counter_map[i] > 0:
                res += f"{chr(i+97)}{counter_map[i]}"

        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - 97] += 1
            groups[tuple(count)].append(s)

        return list(groups.values())
