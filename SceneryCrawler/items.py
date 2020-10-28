from scrapy import Item, Field


class SceneryItem(Item):
    """
    景点信息
    """
    name = Field()
    intro = Field()
    score = Field()
    category = Field()
    location = Field()
    address = Field()
    pic = Field()
    review_count = Field()
    source = Field()
    url = Field()


class ReviewItem(Item):
    """
    用户评论
    """
    name = Field()
    content = Field()
    pics = Field()
    scenery_name = Field()
    source = Field()
    url = Field()

