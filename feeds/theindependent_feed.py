from feeds.base_feed import BaseFeed


# class TheIndependentFeed(BaseFeed):

#     def __init__(self):
#         super(TheIndependentFeed, self).__init__()
#         self.feed_src = 'http://theindependent.sg/feed/'
#         self.source_id = 15



TheIndependentFeed = []
URIList = ['http://theindependent.sg/feed/']
class TheIndependentFeedAll(BaseFeed):
    
    def __init__(self, uri):
        super(TheIndependentFeedAll, self).__init__()
        self.feed_src = uri
        self.source_id = 15

for uri in URIList:
    try:
        TheIndependentFeed.append(TheIndependentFeedAll(uri).get_news())
    except:
        pass