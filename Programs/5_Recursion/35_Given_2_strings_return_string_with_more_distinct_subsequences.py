# https://practice.geeksforgeeks.org/problems/better-string/1 , Hard

# Brute
# T.C. - O(2^n)+O(2^m)
# S.C  - O(m+n)


class Solution:
    def subsequenceCount(self, idx: int, proc: str, s: str):
        if idx == len(s):
            st = set()
            st.add(proc)
            return st

        tmp = set()

        # Take
        val = self.subsequenceCount(idx + 1, proc + s[idx], s)
        for i in val:
            tmp.add(i)

        # Not take
        val = self.subsequenceCount(idx + 1, proc, s)
        for i in val:
            tmp.add(i)

        return tmp

    def betterString(self, str1, str2):
        count1, count2 = self.subsequenceCount(0, "", str1), self.subsequenceCount(
            0, "", str2
        )

        if len(count1) > len(count2):
            return str1
        elif len(count2) > len(count1):
            return str2
        else:
            return str1
