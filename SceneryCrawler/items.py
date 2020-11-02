from scrapy import Item, Field


class SceneryItem(Item):
    """
    景点信息
    """
    name = Field()
    intro = Field()
    review_count = Field()
    per_cost = Field()
    total_score = Field()
    serve_score = Field()
    env_score = Field()
    category = Field()
    location = Field()
    address = Field()
    pic = Field()
    source = Field()
    url = Field()
    ref_url = Field()


class ReviewItem(Item):
    """
    用户评论
    """
    name = Field()
    content = Field()
    publish_time = Field()
    pics = Field()
    scenery_name = Field()
    source = Field()
    url = Field()
    home_url = Field()


class CheckInItem(Item):
    """
    用户打卡数据
    """
    member_id = Field()
    name = Field()
    shop_name = Field()
    shop_address = Field()
    check_in_time = Field()
    source = Field()


