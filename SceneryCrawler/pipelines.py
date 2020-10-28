import pymysql
from SceneryCrawler.items import SceneryItem, ReviewItem
import logging


class MySQLPipeline:
    """
    同步机制写入MySQL
    """
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="123456", db="scenery", charset='utf8', port=3306)
        self.cursor = self.conn.cursor()
        self.logger = logging.getLogger(__name__)

    def process_item(self, item, spider):
        if isinstance(item, SceneryItem):
            insert_sql = """
                        insert into sceneries(`name`, intro, score, category, location, address, pic, review_count, `source`, url)
                        values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                    """ % (item.get('name', None), item.get('intro', None), item.get('score', None), item.get('category', None),
                           item.get('location', None), item.get('address', None), item.get('pic', None), item.get('review_count', None),
                           item.get('source', None), item.get('url', None))
        elif isinstance(item, ReviewItem):
            insert_sql = """
                        insert into reviews(`name`, content, pics, scenery_name, `source`, url)
                        values ("%s", "%s", "%s", "%s", "%s", "%s")
                    """ % (item.get('name', None), item.get('content', None), item.get('pics', None), item.get('scenery_name', None),
                           item.get('source', None), item.get('url', None))

        try:
            self.cursor.execute(insert_sql)
            self.conn.commit()
            self.logger.info(item.get('name', None) + '  插入成功！')
        except Exception as e:
            self.conn.rollback()
            self.logger.error(e)

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()