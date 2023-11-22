# https://leetcode.com/problems/k-th-symbol-in-grammar/ , Medium

# Brute
# T.C. - O(n*k)
# S.C  - O(n^2) + O(n*k)


class Solution:
    def getNewVal(self, st):
        new = ""
        for i in range(len(st)):
            if st[i] == "0":
                new += "01"
            else:
                new += "10"
        return new

    def kthGrammar(self, n: int, k: int) -> int:
        ans = []

        def helper(n, ans):
            if n == 0:
                return "0"
            val = str(helper(n - 1, ans))
            ans.append(list(val))
            return self.getNewVal(val)

        helper(n, ans)
        return int(ans[n - 1][k - 1])


# Brute
# T.C. - O(log(n))
# S.C  - O(n)


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0

        tot = 2 ** (n - 1)
        mid = tot // 2

        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            return int(not self.kthGrammar(n - 1, k - mid))
