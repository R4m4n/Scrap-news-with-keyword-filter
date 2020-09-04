from feeds.base_feed import BaseFeed


# class SCMPFeed(BaseFeed):

#     def __init__(self):
#         super(SCMPFeed, self).__init__()
#         self.feed_src = 'https://www.scmp.comhttps://www.scmp.com/rss/91/feed',
#         self.source_id = 10



SCMPFeed = []
URIList = [
    'https://www.scmp.com/rss/91/feed',
    "https://www.scmp.com/rss/2/feed",
    "https://www.scmp.com/rss/4/feed",
    "https://www.scmp.com/rss/3/feed",
    "https://www.scmp.com/rss/5/feed",
    "https://www.scmp.com/rss/318198/feed",
    "https://www.scmp.com/rss/318199/feed",
    "https://www.scmp.com/rss/318200/feed",
    "https://www.scmp.com/rss/318421/feed",
    "https://www.scmp.com/rss/318202/feed",
    "https://www.scmp.com/rss/318206/feed",
    "https://www.scmp.com/rss/318210/feed",
    "https://www.scmp.com/rss/318208/feed",
    "https://www.scmp.com/rss/318217/feed",
    "https://www.scmp.com/rss/318207/feed",
    "https://www.scmp.com/rss/322262/feed",
    "https://www.scmp.com/rss/322263/feed",
    "https://www.scmp.com/rss/322264/feed",
    "https://www.scmp.com/rss/322265/feed",
    "https://www.scmp.com/rss/322266/feed",
    "https://www.scmp.com/rss/322514/feed",
    "https://www.scmp.com/rss/322243/feed",
    "https://www.scmp.com/rss/318213/feed",
    "https://www.scmp.com/rss/318214/feed",
    "https://www.scmp.com/rss/318215/feed",
    "https://www.scmp.com/rss/318216/feed",
    "https://www.scmp.com/rss/92/feed",
    "https://www.scmp.com/rss/10/feed",
    "https://www.scmp.com/rss/96/feed",
    "https://www.scmp.com/rss/7/feed",
    "https://www.scmp.com/rss/12/feed",
    "https://www.scmp.com/rss/318421/feed",
    "https://www.scmp.com/rss/318200/feed",
    "https://www.scmp.com/rss/6/feed",
    "https://www.scmp.com/rss/17/feed",
    "https://www.scmp.com/rss/76670/feed",
    "https://www.scmp.com/rss/19/feed",
    "https://www.scmp.com/rss/21/feed",
    "https://www.scmp.com/rss/22/feed",
    "https://www.scmp.com/rss/96/feed",
    "https://www.scmp.com/rss/43/feed",
    "https://www.scmp.com/rss/44/feed",
    "https://www.scmp.com/rss/36/feed",
    "https://www.scmp.com/rss/320663/feed",
    "https://www.scmp.com/rss/318218/feed",
    "https://www.scmp.com/rss/318219/feed",
    "https://www.scmp.com/rss/318220/feed",
    "https://www.scmp.com/rss/318221/feed",
    "https://www.scmp.com/rss/318222/feed",
    "https://www.scmp.com/rss/318223/feed",
    "https://www.scmp.com/rss/318224/feed",
    "https://www.scmp.com/rss/318225/feed",
    "https://www.scmp.com/rss/94/feed",
    "https://www.scmp.com/rss/28/feed",
    "https://www.scmp.com/rss/37/feed",
    "https://www.scmp.com/rss/35/feed",
    "https://www.scmp.com/rss/30/feed",
    "https://www.scmp.com/rss/24/feed",
    "https://www.scmp.com/rss/318256/feed",
    "https://www.scmp.com/rss/322296/feed",
    "https://www.scmp.com/rss/25/feed",
    "https://www.scmp.com/rss/318255/feed",
    "https://www.scmp.com/rss/318254/feed",
    "https://www.scmp.com/rss/23/feed",
    "https://www.scmp.com/rss/95/feed",
    "https://www.scmp.com/rss/38/feed",
    "https://www.scmp.com/rss/41/feed",
    "https://www.scmp.com/rss/116/feed",
    "https://www.scmp.com/rss/39/feed",
    "https://www.scmp.com/rss/310895/feed",
    "https://www.scmp.com/rss/40/feed",
    "https://www.scmp.com/rss/117/feed",
    "https://www.scmp.com/rss/47492/feed",
    "https://www.scmp.com/rss/318217/feed",
    "https://www.scmp.com/rss/71/feed",
    "https://www.scmp.com/rss/322658/feed",
    "https://www.scmp.com/rss/322659/feed",
    "https://www.scmp.com/rss/321716/feed",
    "https://www.scmp.com/rss/321721/feed",
    "https://www.scmp.com/rss/321719/feed",
    "https://www.scmp.com/rss/321720/feed",
    "https://www.scmp.com/rss/321713/feed",
    "https://www.scmp.com/rss/72/feed",
    "https://www.scmp.com/rss/322896/feed",
    "https://www.scmp.com/rss/322897/feed",
    "https://www.scmp.com/rss/322898/feed",
    "https://www.scmp.com/rss/322899/feed",
    "https://www.scmp.com/rss/322900/feed",
    "https://www.scmp.com/rss/322901/feed",
    "https://www.scmp.com/rss/323045/feed",
    "https://www.scmp.com/rss/323046/feed",
    "https://www.scmp.com/rss/323047/feed",
    "https://www.scmp.com/rss/323048/feed",
    "https://www.scmp.com/rss/323049/feed",
    "https://www.scmp.com/rss/323050/feed",
    "https://www.scmp.com/rss/323051/feed",
    "https://www.scmp.com/rss/323052/feed",
    "https://www.scmp.com/rss/506035/feed",
    "https://www.scmp.com/rss/506036/feed",
    "https://www.scmp.com/rss/506037/feed",
    "https://www.scmp.com/rss/506038/feed",
    "https://www.scmp.com/rss/506044/feed",
    "https://www.scmp.com/rss/506039/feed",
    "https://www.scmp.com/rss/506042/feed",
    "https://www.scmp.com/rss/505323/feed",
    "https://www.scmp.com/rss/505356/feed",
    "https://www.scmp.com/rss/505326/feed",
    "https://www.scmp.com/rss/505325/feed",
    "https://www.scmp.com/rss/505354/feed",
    "https://www.scmp.com/rss/505355/feed",
    "https://www.scmp.com/rss/505328/feed",
    "https://www.scmp.com/rss/505327/feed"
    ]
class SCMPFeedAll(BaseFeed):
    
    def __init__(self, uri):
        super(SCMPFeedAll, self).__init__()
        self.feed_src = uri
        self.source_id = 10

for uri in URIList:
    try:
        SCMPFeed.append(SCMPFeedAll(uri).get_news())
    except:
        pass

