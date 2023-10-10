# https://leetcode.com/problems/design-browser-history/,Medium

# Brute
# T.C. -> O(n)
# S.C. -> O(n)


class BrowserHistory:
    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.currIdx = 0

    def visit(self, url: str) -> None:
        if self.currIdx == len(self.hist) - 1:
            self.hist.append(url)
            self.currIdx += 1
        else:
            self.hist = self.hist[: self.currIdx + 1]
            self.hist.append(url)
            self.currIdx += 1

    def back(self, steps: int) -> str:
        self.currIdx = max(0, self.currIdx - steps)
        return self.hist[self.currIdx]

    def forward(self, steps: int) -> str:
        self.currIdx = min(len(self.hist) - 1, self.currIdx + steps)
        return self.hist[self.currIdx]


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Node:
    def __init__(self, prev=None, next=None, data="") -> None:
        self.prev = prev
        self.next = next
        self.data = data


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(None, None, homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        self.curr.next = Node(self.curr, None, url)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while steps:
            if self.curr.prev is None:
                return self.curr.data
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.data

    def forward(self, steps: int) -> str:
        while steps:
            if self.curr.next is None:
                return self.curr.data
            steps -= 1
            self.curr = self.curr.next
        return self.curr.data
