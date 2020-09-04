from feeds.base_feed import BaseFeed


# class StraitsTimesFeed(BaseFeed):
    
#     def __init__(self):
#         super(StraitsTimesFeed, self).__init__()
#         # self.feed_src = "https://www.straitstimes.com/news/world/rss.xml"
#         # self.source_id = 8
#         StraitsTimesFeedAll("https://www.straitstimes.com/news/world/rss.xml")

StraitsTimesFeed = []
URIList = [
        "https://www.straitstimes.com/news/world/rss.xml",
        "https://www.straitstimes.com/news/business/rss.xml",
        "https://www.straitstimes.com/news/sport/rss.xml",
        "https://www.straitstimes.com/news/lifestyle/rss.xml",
        "https://www.straitstimes.com/news/opinion/rss.xml",
        "https://www.straitstimes.com/news/singapore/rss.xml",
        "https://www.straitstimes.com/news/politics/rss.xml",
        "https://www.straitstimes.com/news/asia/rss.xml",
        "https://www.straitstimes.com/news/tech/rss.xml",
        "https://www.straitstimes.com/news/forum/rss.xml",
        "https://www.straitstimes.com/news/multimedia/rss.xml",
        "https://www.straitstimes.com/sites/default/files/rss_breaking_news.opml",
        "https://www.straitstimes.com/print/life/rss.xml",
        "https://www.straitstimes.com/print/top-of-the-news/rss.xml",
        "https://www.straitstimes.com/print/world/rss.xml",
        "https://www.straitstimes.com/print/opinion/rss.xml",
        "https://www.straitstimes.com/print/forum/rss.xml",
        "https://www.straitstimes.com/print/big-picture/rss.xml",
        "https://www.straitstimes.com/print/home/rss.xml",
        "https://www.straitstimes.com/print/invest/rss.xml",
        "https://www.straitstimes.com/print/insight/rss.xml",
        "https://www.straitstimes.com/print/science/rss.xml",
        "https://www.straitstimes.com/print/education/rss.xml",
        "https://www.straitstimes.com/print/mind-body/rss.xml",
        "https://www.straitstimes.com/print/digital/rss.xml",
        "https://www.straitstimes.com/print/community/rss.xml",
        "https://www.straitstimes.com/print/business/rss.xml",
        "https://www.straitstimes.com/print/sport/rss.xml",
        "https://www.straitstimes.com/sites/default/files/rss_print.opml",
        "https://www.straitstimes.com/sunday-print/top-of-the-news/rss.xml",
        "https://www.straitstimes.com/sunday-print/world/rss.xml",
        "https://www.straitstimes.com/sunday-print/home/rss.xml",
        "https://www.straitstimes.com/sunday-print/invest/rss.xml",
        "https://www.straitstimes.com/sunday-print/insight/rss.xml",
        "https://www.straitstimes.com/sunday-print/sport/rss.xml",
        "https://www.straitstimes.com/sunday-print/life/rss.xml",
        "https://www.straitstimes.com/sites/default/files/rss_sunday_print.opml"
]
class StraitsTimesFeedAll(BaseFeed):
    
    def __init__(self, uri):
        super(StraitsTimesFeedAll, self).__init__()
        self.feed_src = uri
        self.source_id = 8

for uri in URIList:
    try:
        StraitsTimesFeed.append(StraitsTimesFeedAll(uri).get_news())
    except:
        pass