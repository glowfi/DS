# https://leetcode.com/problems/longest-common-prefix/ , Easy

# Brute
# T.C. -> O(n*len(str[0]))+O(nlog(n))
# S.C. -> O(1)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs.sort()
        longestCommonPrefix = ""
        for i in range(len(strs[0])):
            currPrefix = strs[0][: i + 1]
            flag = 0
            for j in range(1, len(strs)):
                if currPrefix == strs[j][: i + 1]:
                    continue
                else:
                    flag = 1
                    break
            if flag == 0:
                longestCommonPrefix = strs[j][: i + 1]
        return longestCommonPrefix


# Optimal
# T.C. -> O(nlog(n))+O(min(first,last))
# S.C. -> O(1)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Handle one length strs array
        if len(strs) == 1:
            return strs[0]

        # Handle strs array with more than 1 length
        strs.sort()

        # When we sort alphabetically it is enough to check form common prefix b/w the last and first string of the sorted list
        longestCommonPrefix = ""
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                break
            longestCommonPrefix += strs[0][i]

        return longestCommonPrefix
