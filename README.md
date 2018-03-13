# 直播平台爬虫
### 项目环境配置
使用语言：python(2和3都兼容)  
使用的库：urllib、re、pymysql、datetime
数据库：mysql   

### 主要实现功能
1. 可以对虎牙，斗鱼直播平台进行爬虫
2. 抓取整个直播平台的全部游戏分区的名字和链接
3. 抓取在各个分区下的主播名称，房间标题，当前观众数，房间链接
4. 通过访问爬取到的房间链接，可以爬取主播的订阅数
5. 使用伪装浏览器

### 将来要实现的功能
1. 爬取主播房间里的贡献榜单，来实现对主播收入的简单统计
2. 添加更多的平台如龙珠，熊猫TV等

### 使用截图
程序开始会自动爬取直播平台全部游戏分区  
![image](https://note.youdao.com/yws/public/resource/ebe0db6e35cc561cc39c167523cad0b4/xmlnote/37827A7C481B4265BEADF6EA8B1A500A/16108)    

输入Y后  
![image](https://note.youdao.com/yws/public/resource/ebe0db6e35cc561cc39c167523cad0b4/xmlnote/ACF2B2E5AB03459C84C6D91A8105733A/16112)    
爬取某个分区后会提醒完成这个分区，然后开始爬取下个分区  
![image](https://note.youdao.com/yws/public/resource/ebe0db6e35cc561cc39c167523cad0b4/xmlnote/056EA84D79D64391B87BDC45D64300BF/16118)    
### 结果展示
#### 数据库link
![image](https://note.youdao.com/yws/public/resource/ebe0db6e35cc561cc39c167523cad0b4/xmlnote/9062AD70E6D84F60AF065BAD179939EE/16121)  
id:主播名称、title：房间标题、js：在线观众、game：分区、link：房间链接、time：时间
#### 数据库主播
![image](https://note.youdao.com/yws/public/resource/ebe0db6e35cc561cc39c167523cad0b4/xmlnote/79ABF0B620F0419083CA60FC3E2D403A/16123)  
id:主播名称、title：房间标题、count：观众订阅量、game：分区、link：房间链接、time：时间


