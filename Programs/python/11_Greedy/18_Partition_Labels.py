# https://neetcode.io/problems/partition-labels , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(26)

# Intuition
# evry paritions character map should be distinct
# meaning each parition should have uniques set of characters
# characters from partion 1 should not appear on other partion
# + Its a simple two pointer technique
# + when we start a partion we fix the i pointer to 0,0 and currEnd to its last_occurence of character index
# + we move j and try to expand our partion size if we see the last_occurence pf current character
# + is greater than our currEnd, wee keep repeating this process

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur_map: dict[str, int] = {}
        for idx, ch in enumerate(s):
            last_occur_map[ch] = idx

        i, j = 0, 0
        currEnd = 0
        ans = []

        while i < len(s):
            currEnd = last_occur_map[s[j]]
            while j < currEnd:
                if last_occur_map[s[j]] > currEnd:
                    currEnd = last_occur_map[s[j]]
                j += 1
            ans.append(j - i + 1)
            i = currEnd + 1
            j += 1

        return ans
