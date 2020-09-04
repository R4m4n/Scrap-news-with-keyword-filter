from feeds.base_feed import BaseFeed


# class MotherShipSGFeed(BaseFeed):

#     def __init__(self):
#         super(MotherShipSGFeed, self).__init__()
#         self.feed_src = "https://mothership.sg/feed/"
#         self.source_id = 12


MotherShipSGFeed = []
URIList = ["https://mothership.sg/feed/"]
class MotherShipSGFeedAll(BaseFeed):
    
    def __init__(self, uri):
        super(MotherShipSGFeedAll, self).__init__()
        self.feed_src = uri
        self.source_id = 12

for uri in URIList:
    try:
        MotherShipSGFeed.append(MotherShipSGFeedAll(uri).get_news())
    except:
        pass