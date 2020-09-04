from feeds.base_feed import BaseFeed


# class TodayOnlineFeed(BaseFeed):
#     def __init__(self):
#         super(TodayOnlineFeed, self).__init__()
#         self.feed_src = 'https://www.todayonline.com/hot-news/feed'
#         self.source_id = 14


TodayOnlineFeed = []
URIList = ['https://www.todayonline.com/hot-news/feed']
class TodayOnlineFeedAll(BaseFeed):
    
    def __init__(self, uri):
        super(TodayOnlineFeedAll, self).__init__()
        self.feed_src = uri
        self.source_id = 14

for uri in URIList:
    try:
        TodayOnlineFeed.append(TodayOnlineFeedAll(uri).get_news())
    except:
        pass