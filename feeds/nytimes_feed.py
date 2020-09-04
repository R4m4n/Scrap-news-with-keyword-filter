from feeds.base_feed import BaseFeed


# class NYTimesFeed(BaseFeed):
#     def __init__(self):
#         super(NYTimesFeed, self).__init__()
#         self.feed_src = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
#         self.source_id = 11

# class NYTimesFeedHealth(BaseFeed):
#     def __init__(self):
#         super(NYTimesFeedHealth, self).__init__()
#         self.feed_src = 'https://rss.nytimes.com/services/xml/rss/nyt/Health.xml'
#         self.source_id = 16



NYTimesFeed = []
URIList = [
    'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml', 
    'https://rss.nytimes.com/services/xml/rss/nyt/Health.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Africa.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Americas.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/US.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Education.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/NYRegion.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Business.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/SmallBusiness.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Dealbook.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/MediaandAdvertising.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/YourMoney.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Science.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Space.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Arts.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/ArtandDesign.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Books.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Dance.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Movies.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Music.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Television.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/Theater.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/FashionandStyle.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/DiningandWine.xml',
    'https://www.nytimes.com/services/xml/rss/nyt/Weddings.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/tmagazine.xml',
    'https://www.nytimes.com/services/xml/rss/nyt/Travel.xml',


    ]
class NYTimesFeedAll(BaseFeed):
    
    def __init__(self, uri):
        super(NYTimesFeedAll, self).__init__()
        self.feed_src = uri
        self.source_id = 11

for uri in URIList:
    try:
        NYTimesFeed.append(NYTimesFeedAll(uri).get_news())
    except:
        pass