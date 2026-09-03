class Twitter:
    def __init__(self):
        self.stack = []
        self.following = {}          # renamed

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.stack.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        followees = self.following.get(userId, [])   # no early return
        for idx in range(len(self.stack) - 1, -1, -1):
            tweetId, author = self.stack[idx]
            if author == userId or author in followees:
                result.append(tweetId)
                if len(result) == 10:
                    break
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following.setdefault(followerId, [])
        if followeeId not in self.following[followerId]:   # avoid dupes
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following.get(followerId, []):
            self.following[followerId].remove(followeeId)