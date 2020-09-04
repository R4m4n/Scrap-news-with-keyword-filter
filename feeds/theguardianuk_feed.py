from feeds.base_feed import BaseFeed


# class TheGuardianUKFeed(BaseFeed):
#     def __init__(self):
#         super(TheGuardianUKFeed, self).__init__()
#         self.feed_src = 'https://www.theguardian.com/uk/rss'
#         self.source_id = 9


TheGuardianUKFeed = []
URIList = [
    'https://www.theguardian.com/uk/rss',
    'https://www.theguardian.com/world/rss',
    'https://www.theguardian.com/football/rss',
    'https://www.theguardian.com/uk/sport/rss',
    'https://www.theguardian.com/uk/culture/rss',
    'https://www.theguardian.com/uk/lifeandstyle/rss',
    'https://www.theguardian.com/uk/technology/rss',
    'https://www.theguardian.com/books/rss',
    'https://www.theguardian.com/global-development/rss',
    'https://www.theguardian.com/cities/rss',
    'https://www.theguardian.com/fashion/rss',
    'https://www.theguardian.com/uk-news/rss',
    'https://www.theguardian.com/crosswords/rss',
    'https://www.theguardian.com/games/rss',
    'https://www.theguardian.com/uk/environment/rss',
    'https://www.theguardian.com/artanddesign/rss',
    'https://www.theguardian.com/science/rss',
    'https://www.theguardian.com/uk/business/rss',
    'https://www.theguardian.com/music/rss',
    'https://www.theguardian.com/stage/rss',
    'https://www.theguardian.com/uk/travel/rss',
    'https://www.theguardian.com/uk/money/rss',
    'https://www.theguardian.com/video/rss',

    ]
class TheGuardianUKFeedAll(BaseFeed):
    
    def __init__(self, uri):
        super(TheGuardianUKFeedAll, self).__init__()
        self.feed_src = uri
        self.source_id = 9

for uri in URIList:
    try:
        TheGuardianUKFeed.append(TheGuardianUKFeedAll(uri).get_news())
    except:
        pass