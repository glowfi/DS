# https://leetcode.com/problems/design-twitter , Medium

# Brute
# T.C. - O(1) postTweet , O(n) getNewsFeed , O(1) follow , O(no_of_followers) -> unfollow
# S.C  - O(n)+O(n)

from collections import defaultdict


class Twitter:

    def __init__(self):
        self.user_following_map = defaultdict(set)  # (uid:[uid,.....])
        self.user_tweets_list: list[list[int]] = []  # [uid,twid]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets_list.append(
            [
                userId,
                tweetId,
            ]
        )

    def getNewsFeed(self, userId: int) -> List[int]:
        k = 10
        res: list[int] = []
        for i in range(len(self.user_tweets_list) - 1, -1, -1):
            usr_id, tweet_id = self.user_tweets_list[i]

            if k == 0:
                break

            if usr_id == userId or usr_id in self.user_following_map[userId]:
                k -= 1
                res.append(tweet_id)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_following_map[followerId].discard(followeeId)


# Optimal
# T.C. - O(1) postTweet , O(F log F) getNewsFeed , O(1) follow , O(no_of_followers) -> unfollow
# S.C  - O(n)+O(n)


from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.user_following_map = defaultdict(set)  # (uid:[uid,.....])
        self.user_tweets_list = defaultdict(set)  # [uid:[twid,timestamp]]
        self.time_stamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets_list[userId].add((tweetId, self.time_stamp))
        self.time_stamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res: list[int] = []

        max_heap = []
        for twid, time_stamp in self.user_tweets_list[userId]:
            heapq.heappush(max_heap, (time_stamp * -1, twid, userId))

        for fid in self.user_following_map[userId]:
            if fid in self.user_tweets_list:
                for twid, time_stamp in self.user_tweets_list[fid]:
                    heapq.heappush(max_heap, (time_stamp * -1, twid, fid))

        k = 10
        while max_heap and k:
            res.append(heapq.heappop(max_heap)[1])
            k -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_following_map[followerId].discard(followeeId)
