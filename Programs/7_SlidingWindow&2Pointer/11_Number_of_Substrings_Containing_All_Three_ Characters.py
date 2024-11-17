# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters , Medium

# Brute
# T.C. - O(N^2)
# S.C  - O(1)


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c = 0
        k = 3

        for i in range(len(s)):
            hmap = {}
            for j in range(i, len(s)):
                if s[j] not in hmap:
                    hmap[s[j]] = 1
                else:
                    hmap[s[j]] += 1

                if len(hmap) == k:
                    c += 1

        return c


# Optimal
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c = 0
        last_seen_index = {"a": -1, "b": -1, "c": -1}

        for i in range(len(s)):
            if s[i] == "a" or s[i] == "b" or s[i] == "c":
                last_seen_index[s[i]] = i

            # Find all substring that ends with s and given cond holds true
            if (
                last_seen_index["a"] > -1
                and last_seen_index["a"] > -1
                and last_seen_index["a"] > -1
            ):
                idx = min(last_seen_index.values())
                c += idx + 1

        return c
