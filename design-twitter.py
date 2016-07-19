
from Collections import deque
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
       self.idcontent = range(100)
       self.idfollowmap = {}#map; a user:a list who he/she follows 
       self.idarticlemap = {}
       self.idarticledeque = deque()

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.idarticlemap[userId] = tweetId
        self.idarticledeque.append(dict(zip([userId],[tweetId])))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        l = []
        while len(l)<=10:
            article = self.idarticledeque.pop()
            if article[userId] is not None:
                l.append(article[userId])
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.idfollowmap[followerId].append(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.idfollowmap[followId]:
            self.idfollowmap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
