# https://leetcode.com/problems/reverse-words-in-a-string , Medium

# Question
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


# Constraints:

# 1 <= s.length <= 10^4
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.


# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

# Brute
# T.C. - O(2N) ~ O(N)
# S.C  - O(N)

# Intuition
# extract only words from string and put them into the list
# reverse the list
# return the list by using join keyword


class Solution:
    def split_string_to_words(self, s: str) -> list[str]:
        words: list[str] = []
        tmp: str = ""

        for i in range(len(s)):
            if s[i] == " ":
                if tmp:
                    words.append(tmp)
                    tmp = ""
            else:
                tmp += s[i]

        if tmp:
            words.append(tmp)

        return words

    def reverse_list(self, words: list[str]):
        i, j = 0, len(words) - 1

        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1

    def reverseWords(self, s: str) -> str:
        words = self.split_string_to_words(s)
        self.reverse_list(words)
        return " ".join(words)


# Better
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# use pythons builtin split to split into words
# then reverse the list
# return the reversed list using join keyword


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# reverse whole string first
# Take 2 pointers l and r it will be used to reverse words between them
# keep moving i until you reach non space character , then assign the character at ith index with the character at r index
# when we encounter space , reverse words between l and r index
# move r to one place after space and assign l to r, repeat the above process until i exhauts the string


class Solution:
    def rev(self, i: int, j: int, s: list[str]):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def reverseWords(self, s: str) -> str:
        mutable_str = list(s)

        self.rev(0, len(mutable_str) - 1, mutable_str)

        l, r = 0, 0  # will be used for reversing string
        i = 0  # will be used to traverse string
        # r will be used for writing

        while i < len(mutable_str):
            while i < len(mutable_str) and mutable_str[i] != " ":
                mutable_str[r] = mutable_str[i]
                i += 1
                r += 1

            if l < r:
                self.rev(l, r - 1, mutable_str)
                mutable_str[r] = " "
                r += 1
                l = r

            i += 1

        return "".join(mutable_str[: r - 1])
