# https://leetcode.com/problems/candy , Hard

# Brute
# T.C. - O(3N)
# S.C  - O(2N)

# Intuition
# + First only think that you have to give only candy wrt to left neighbour only
# + Person at current index should have more candy than its left neighbour based on his rating
# Create a left array and store the candy to assign based on rating,always try to assign 1
# candy to the leftmost member and start checking for further index what to assign based on rating
# + Do the same thing for the right array


from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        left, right = [1 for _ in range(len(ratings))], [1 for _ in range(len(ratings))]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                right[j] = right[j + 1] + 1

        sm = 0

        for i in range(len(ratings)):
            sm += max(left[i], right[i])

        return sm


# Better
# T.C. - O(2N)
# S.C  - O(N)


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for _ in range(len(ratings))]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        prev_candy = 1
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candies[j] = max(1 + prev_candy, candies[j])
                prev_candy += 1
            else:
                prev_candy = 1

        return sum(candies)


# Optimal [peak up peak down method,slope method,unintuitive]
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Until we are in ratings are in increasing order or peak we keep assigning 1 candy more than candy assigned to prev_child
# Until we are in decreasing order we start with 1 and keep assigning 1 more than prev candy
# if down>peak adjust peak child
# if flat surfaces just add one


class Solution:
    def candy(self, ratings: List[int]) -> int:
        sm = 1
        i = 1

        while i < len(ratings):
            # if equal in rating
            if ratings[i] == ratings[i - 1]:
                sm += 1
                i += 1
                continue

            # peak
            peak = 1
            while i < len(ratings) and ratings[i] > ratings[i - 1]:
                peak += 1
                sm += peak
                i += 1

            # down
            down = 0
            while i < len(ratings) and ratings[i] < ratings[i - 1]:
                down += 1
                sm += down
                i += 1

            # adjust peak
            down += 1
            if down > peak:
                sm += down - peak

        return sm
