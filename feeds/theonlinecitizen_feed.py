from feeds.base_feed import BaseFeed


# class TheOnlineCitizenFeed(BaseFeed):
#     def __init__(self):
#         super(TheOnlineCitizenFeed, self).__init__()
#         self.feed_src = 'https://www.theonlinecitizen.com/feed/'
#         self.source_id = 13

TheOnlineCitizenFeed = []
URIList = ['https://www.theonlinecitizen.com/feed/']
class TheOnlineCitizenFeedAll(BaseFeed):
    
    def __init__(self, uri):
        super(TheOnlineCitizenFeedAll, self).__init__()
        self.feed_src = uri
        self.source_id = 13

for uri in URIList:
    try:
        TheOnlineCitizenFeed.append(TheOnlineCitizenFeedAll(uri).get_news())
    except:
        pass