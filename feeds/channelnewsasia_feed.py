from feeds.base_feed import BaseFeed


# class ChannelNewsAsiaFeed(BaseFeed):
#     def __init__(self):
#         super(ChannelNewsAsiaFeed, self).__init__()
#         self.feed_src = 'https://www.channelnewsasia.com/rssfeeds/8395986'
#         self.source_id = 6


ChannelNewsAsiaFeed = []
URIList = [
    'https://www.channelnewsasia.com/rssfeeds/8395986',
    'https://www.channelnewsasia.com/rssfeeds/8395744',
    'https://www.channelnewsasia.com/rssfeeds/8395954',
    'https://www.channelnewsasia.com/rssfeeds/8396082',
    'https://www.channelnewsasia.com/rssfeeds/8395838',
    'https://www.channelnewsasia.com/rssfeeds/8395884'
    ]
class ChannelNewsAsiaFeedAll(BaseFeed):
    
    def __init__(self, uri):
        super(ChannelNewsAsiaFeedAll, self).__init__()
        self.feed_src = uri
        self.source_id = 6

for uri in URIList:
    try:
        ChannelNewsAsiaFeed.append(ChannelNewsAsiaFeedAll(uri).get_news())
    except:
        pass