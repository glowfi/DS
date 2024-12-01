# https://leetcode.com/problems/word-ladder/ , Hard

# Optimal
# T.C. - O(n*m*26)
# S.C  - O(n)

from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        q = deque([[beginWord, 1]])

        wordList = set(wordList)

        while q:
            for i in range(len(q)):
                word, steps = q.popleft()
                if word == endWord:
                    return steps

                for idx in range(len(word)):
                    for i in range(97, 123):
                        currWord = word[:idx] + chr(i) + word[idx + 1 :]
                        if currWord in wordList:
                            q.append([currWord, steps + 1])
                            wordList.remove(currWord)
        return 0
