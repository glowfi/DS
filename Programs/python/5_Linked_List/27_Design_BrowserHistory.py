# https://leetcode.com/problems/design-browser-history , Medium, Design

# Question
# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


# Example:

# Input:
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
# Output:
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

# Explanation:
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
# browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
# browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
# browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
# browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
# browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
# browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
# browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
# browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
# browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"


# Constraints:

# 1 <= homepage.length <= 20
# 1 <= url.length <= 20
# 1 <= steps <= 100
# homepage and url consist of  '.' or lower case English letters.
# At most 5000 calls will be made to visit, back, and forward.


# Brute
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Just Keep track of current index
# Move back k steps on back command but dont go out of bounds
# Move forward k steps on forward command but dont go out of bounds


class Node:
    def __init__(self, x: str) -> None:
        self.prev: "Node" = None
        self.next: "Node" = None
        self.url: str = x


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)

    def visit(self, url: str) -> None:
        if self.head.next:
            self.head.next.prev = None
            self.head.next = None

        new_node = Node(url)
        new_node.prev = self.head
        self.head.next = new_node
        self.head = self.head.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.head.prev:
                self.head = self.head.prev
        return self.head.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.head.next:
                self.head = self.head.next
        return self.head.url


# Optimal
# T.C. - O(1)
# S.C  - O(N)

# Intuition
# Use a list to keep track of history


class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist: list[str] = [homepage]
        self.curr_index: int = 0

    def visit(self, url: str) -> None:
        hasNextElems = self.curr_index + 1 < len(self.hist)
        if hasNextElems:
            self.hist = self.hist[: self.curr_index + 1]
        self.hist.append(url)

    def back(self, steps: int) -> str:
        index = max(0, self.curr_index - steps)
        return self.hist[index]

    def forward(self, steps: int) -> str:
        index = min(len(self.hist) - 1, self.curr_index + steps)
        return self.hist[index]
