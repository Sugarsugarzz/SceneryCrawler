import pymysql
from SceneryCrawler.items import SceneryItem, ReviewItem, CheckInItem
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
                        insert into sceneries(`name`, intro, review_count, per_cost, total_score, serve_score, env_score, category, location, address, pic, `source`, url, ref_url)
                        values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                    """ % (item.get('name', ''), item.get('intro', ''), item.get('review_count', ''), item.get('per_cost', ''), item.get('total_score', ''),
                           item.get('serve_score', ''), item.get('env_score', ''), item.get('category', ''), item.get('location', ''), item.get('address', ''), item.get('pic', ''), item.get('source', ''), item.get('url', ''), item.get('ref_url', ''))

        elif isinstance(item, ReviewItem):
            insert_sql = """
                        insert into reviews(`name`, content, publish_time, pics, scenery_name, `source`, url, home_url)
                        values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")
                    """ % (item.get('name', ''), item.get('content', ''), item.get('publish_time', ''), item.get('pics', ''), item.get('scenery_name', ''),
                           item.get('source', ''), item.get('url', ''), item.get('home_url', ''))

        elif isinstance(item, CheckInItem):
            insert_sql = """
                        insert into checkins(member_id, `name`, shop_name, shop_address, check_in_time, `source`)
                        values ("%s", "%s", "%s", "%s", "%s", "%s")
                    """ % (item.get('member_id', ''), item.get('name', ''), item.get('shop_name', ''), item.get('shop_address', ''), item.get('check_in_time', ''),
                           item.get('source', ''))

        try:
            self.cursor.execute(insert_sql)
            self.conn.commit()
            self.logger.info(item.get('name', '') + '  插入成功！')
        except Exception as e:
            self.conn.rollback()
            self.logger.error(e)

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()