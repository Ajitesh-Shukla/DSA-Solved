class Twitter:
    '''See how to solve this using heap'''
    def __init__(self):
        '''Adjacency map for follower-followee relationship'''
        self.following_adj_map={}
        '''To post and retreive feed, array looks okay, try it'''
        self.all_tweets=[]
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.following_adj_map:
            self.following_adj_map[userId]=set()    # In case one directly wants to get news feed after posting
        self.all_tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> list[int]:
        i=len(self.all_tweets)-1
        get_news_feed=[]
        while i>=0 and len(get_news_feed)<10:
            if self.all_tweets[i][0]==userId or self.all_tweets[i][0] in self.following_adj_map[userId]:
                get_news_feed.append(self.all_tweets[i][1])
            i-=1
        return get_news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following_adj_map:
            self.following_adj_map[followerId].add(followeeId)
        else:
            self.following_adj_map[followerId]=set()
            self.following_adj_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_adj_map[followerId]:
            self.following_adj_map[followerId].remove(followeeId)