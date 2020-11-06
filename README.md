### 总体
1. 完成对两层字体加密的破解。（每日零点都会更新加密词典，所以每天都要重新获取解密词典）
2. 完成对景点信息的采集。（店铺的同样适用，修改下起始URL即可）
3. 完成对景点/商铺内的所有用户评论数据的采集。
4. 完成对所有用户的打卡记录的采集。

### 问题
- 采集到一定数量，账户就会跳验证码
    - 方案：出现验证码：停止爬虫，刷网页手动验证，再启动爬虫。
- 403，特定页面不能访问
    - 方案：源于Cookie失效。换账号模拟登录，更换Cookie和User-Agent，再启动爬虫。

### Sceneries
北京市的已经采集完毕

### Reviews
约144万条评论，对应百万个用户。
直接访问 /reivew_all页面，极易触发验证码。先访问景点/店铺详情页，然后再访问/review_all好一些。

### Checkin
调用API直接采集，等Reviews采集完开始。
