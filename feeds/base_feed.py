import datetime
import time

from dateutil import parser

import feedparser
import requests


class BaseFeed:

    def __init__(self):
        self.feed_src = None
        self.entries = None

    def get_content(self):
        r = requests.get(url=self.feed_src)
        x = feedparser.parse(r.content)
        self.entries = x['entries']

    def get_news(self):
        self.get_content()

        result = []

        for entry in self.entries:

            published = parser.parse(entry['published'])
            # published = published.replace(tzinfo=datetime.timezone.utc) - published.utcoffset()
            unix_time = int(time.mktime(published.timetuple()))

            result.append({
                "title": entry['title'],
                "source_link": entry['link'],
                "date_created": published,
                "date_create_unix": unix_time,
                "__class_name": self.__class__.__name__,
                "__source_id": self.source_id
            })

        return result
