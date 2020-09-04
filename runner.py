import pymysql
import re
from config import Config
from feeds.channelnewsasia_feed import ChannelNewsAsiaFeed
from feeds.mothershipsg_feed import MotherShipSGFeed
from feeds.nytimes_feed import NYTimesFeed
from feeds.scmp_feed import SCMPFeed
from feeds.straitstimes_feed import StraitsTimesFeed
from feeds.theguardianuk_feed import TheGuardianUKFeed
from feeds.theindependent_feed import TheIndependentFeed
from feeds.theonlinecitizen_feed import TheOnlineCitizenFeed
from feeds.todayonline_feed import TodayOnlineFeed

FEEDS = [StraitsTimesFeed, MotherShipSGFeed, TheOnlineCitizenFeed, TheIndependentFeed, NYTimesFeed, SCMPFeed,
         TheGuardianUKFeed, TodayOnlineFeed, ChannelNewsAsiaFeed]
# FEEDS = [ChannelNewsAsiaFeed]

class Runner:
    def __init__(self):
        self.db = pymysql.connect(host=Config.MYSQL_HOST,
                                  port=Config.MYSQL_PORT,
                                  user=Config.MYSQL_USER,
                                  password=Config.MYSQL_PASSWORD,
                                  database=Config.MYSQL_DB,
                                  cursorclass=pymysql.cursors.DictCursor)

        self.topics = self.get_topics()
        self.titles = []

    @staticmethod
    def __has_same_title_topicId(cursor, title, topicId):
        sql = "select 1 from rss_table where title = %s and topic_id = %s"
        cursor.execute(query=sql, args=[title, topicId])
        fetcho = cursor.fetchone()
        return True if fetcho != None else False

    def get_topics(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * from topics ")

        return cursor.fetchall()

    def save(self, news, topic):

        if news['title'] not in self.titles:
            self.titles.append(news['title'])

        try:
            cursor = self.db.cursor()
            has_same_title_topicId = self.__has_same_title_topicId(cursor=cursor, title=news['title'], topicId=topic['id'])
            if not has_same_title_topicId:

                sql = """INSERT INTO `rss_table` (`title`, `source_link`, `date_created`, `processed`, `topic_id`,  
                    `date_create_unix`) 
                    VALUES (%s, %s, %s, '0', %s, %s)
                """

                cursor.execute(query=sql, args=[news['title'], news['source_link'], news['date_created'], topic['id'],
                                                news['date_create_unix']])

                rss_id = cursor.lastrowid

                sql = """
                    INSERT INTO `rss_source_link` (`source_id`, `rss_id`, `topic_id`) VALUES (%s, %s, %s)
                """

                cursor.execute(query=sql, args=[news['__source_id'], rss_id, topic['id']])
                self.db.commit()
            else:
                pass

            
        except Exception as ex:
            print(ex)

            self.db.rollback()

    def check_topics(self, news):

        for topic in self.topics:
            title = news['title'].lower()
            
            # if any(kw in title for kw in topic['keywords'].lower().split(',')):
            #     print ('\n title => ', title)
            #     self.save(news=news, topic=topic)
            for kw in topic['keywords'].lower().split(','):
                if re.search(r'\b' + kw + r'\b', title):
                    print ('\n title => ', title)
                    self.save(news=news, topic=topic)

    def run(self):
        for _feed_all in FEEDS:
            # print (_feed_all, ' <<=== _feed \n\n')
            for _feed in _feed_all:
                for _news in _feed:
                    self.check_topics(_news)


