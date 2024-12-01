# https://leetcode.com/problems/count-and-say/ , Medium

# Brute
# T.C. - O(n*K)
# S.C  - O(n)


# s = "1211" [Take this example and think]


class Solution:
    def getCount(self, st):
        newStr = ""
        i = 0
        c = 0
        while i < len(st):
            if i + 1 < len(st) and st[i + 1] == st[i]:
                c += 1
            else:
                c += 1
                newStr += f"{c}{st[i]}"
                c = 0
            i += 1

        return newStr

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        val = self.countAndSay(n - 1)
        return self.getCount(val)
