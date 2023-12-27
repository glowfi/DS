# https://leetcode.com/problems/word-ladder-ii/description/ , Hard


# Better
# T.C. - Cant be predicted as there can be multiple transformation from startword to endWord
# S.C  - Cant be predicted as there can be multiple transformation from startword to endWord


from collections import deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        q = deque([[[beginWord]]])

        wordList = set(wordList)
        ans = []

        while q:
            tmp = []
            for i in range(len(q)):
                data = q.popleft()

                word = data[0][-1]
                seq = data[0]
                if word == endWord:
                    ans.append(seq)

                for idx in range(len(word)):
                    for i in range(97, 123):
                        currWord = word[:idx] + chr(i) + word[idx + 1 :]
                        if currWord in wordList:
                            tmp.append(currWord)
                            q.append([[*seq, currWord]])

            for i in range(len(tmp)):
                if tmp[i] in wordList:
                    wordList.remove(tmp[i])

        return ans


# Optimal
# T.C. - Cant be predicted as there can be multiple transformation from startword to endWord
# S.C  - Cant be predicted as there can be multiple transformation from startword to endWord

from collections import deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        q = deque([[beginWord, 1]])

        wordList = set(wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
        mpp = {}
        mpp[beginWord] = 1
        mn_length = float("inf")
        ans = []

        while q:
            for i in range(len(q)):
                word, steps = q.popleft()
                if word == endWord:
                    mpp[endWord] = steps
                    mn_length = min(steps, mn_length)

                for idx in range(len(word)):
                    for i in range(97, 123):
                        currWord = word[:idx] + chr(i) + word[idx + 1 :]
                        if currWord in wordList:
                            q.append([currWord, steps + 1])
                            mpp[currWord] = steps + 1
                            wordList.remove(currWord)

        if mn_length == float("inf"):
            return ans

        def dfs(word, index, tmp, ans):
            if index == 1:
                ans.append(list(tmp)[:])
                return

            for idx in range(len(word)):
                for i in range(97, 123):
                    currWord = word[:idx] + chr(i) + word[idx + 1 :]
                    if currWord in mpp and mpp[currWord] == index - 1:
                        tmp.appendleft(currWord)
                        dfs(currWord, index - 1, tmp, ans)
                        tmp.popleft()

        dfs(endWord, mn_length, deque([endWord]), ans)

        return ans


# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

# beginWord = "a"
# endWord = "c"
# wordList = ["a", "b", "c"]

# obj = Solution()
# print(obj.findLadders(beginWord, endWord, wordList))
