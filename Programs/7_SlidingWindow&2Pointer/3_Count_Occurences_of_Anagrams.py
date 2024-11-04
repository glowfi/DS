# https://www.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1 , Medium

# Brute
# T.C. - O(n-k*k*z)
# S.C  - O(k)+o(z)


class Solution:
    def isAnagram(self, s1, s2):
        h1, h2 = {}, {}

        for i in s1:
            if i in h1:
                h1[i] += 1
            else:
                h1[i] = 1

        for i in s2:
            if i in h2:
                h2[i] += 1
            else:
                h2[i] = 1

        return h1 == h2

    def search(self, pat, txt):
        c = 0
        k = len(pat)
        n = len(txt)

        for i in range(n - k + 1):
            word = ""
            for j in range(i, i + k):
                word += txt[j]

            if self.isAnagram(word, pat):
                c += 1

        return c


# Optimal
# T.C. - O(2n)
# S.C  - O(patsize)+O(n)


class Solution:
    def search(self, pat, txt):
        c = 0
        k = len(pat)
        n = len(txt)

        l, r = 0, -1

        patMap, currWordMap = {}, {}

        for i in pat:
            if i in patMap:
                patMap[i] += 1
            else:
                patMap[i] = 1

        c = 0
        for i in range(k):
            currChar = txt[i]
            if currChar in currWordMap:
                currWordMap[currChar] += 1
            else:
                currWordMap[currChar] = 1
            r += 1

        if currWordMap == patMap:
            c += 1

        while r < n - 1:
            if currWordMap[txt[l]] == 1:
                del currWordMap[txt[l]]
            else:
                currWordMap[txt[l]] -= 1

            l += 1

            r += 1
            if txt[r] in currWordMap:
                currWordMap[txt[r]] += 1
            else:
                currWordMap[txt[r]] = 1

            if currWordMap == patMap:
                c += 1

        return c
