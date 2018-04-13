# ProxyPool
### 简介

​	proxypool基于scrapy框架，提供了一个抓取免费IP代理的爬虫框架，只需要编写对应代理网站的网页xpath提取规则，以及添加特有的item清理规则即可完成IP代理网站的爬取。



#### 成果

​	数据库里保持活性的IP代理（http/https/http，https）维持在***550***个左右（数据是三天测试观察，按照项目中的IP代理筛选机制计算）



### 包模块功能

​	item_clean: 自定义item清理规则，内含有通用清理规则usual.py文件。

​	model：用于定义爬取的IP代理和爬取xpath规则的在数据库中的存储模型

​	utils：额外需用是要的工具包

​	其它文件是scrapy框架项目默认生成的



## 模型字段说明

​	爬取规则字段请看“**使用方法**”

​	IP代理字段含义如下表：

| 字段名       | 含义         |
| ------------ | ------------ |
| ip           | ip地址       |
| ip_img_url   | ip图片地址   |
| port         | 端口号       |
| port_img_url | 端口图片     |
| type         | 代理类型     |
| level        | 匿名度       |
| location     | 代理地理位置 |
| speed        | 响应速度     |
| lifetime     | 生存时间     |
| lastcheck    | 上次检查时间 |
| source       | 来源地址     |
| rule_name    | 规则名       |
| indate       | 入库时间     |
| update       | 更新时间     |



## 使用方法

#### 在Git中下载代码

​	执行一下代码即可（SSH）

​	`git clone git@github.com:Barnettxxf/ProxyPool.git`

​	或（HTTP）：

​	`git clone https://github.com/Barnettxxf/ProxyPool.git`



#### 修改数据库配置

​	在model模块的`config.py`文件设置engine连接的数据库信息



#### 初始化xpath规则

​	在initDB.py文件中填写爬取规则，各个字段含义如下表：

| 字段名           | 含义                                                         |
| :--------------- | ------------------------------------------------------------ |
| name             | 爬取规则名字，不能和其他名字重复                             |
| allow_domains    | 允许的域名                                                   |
| start_urls       | 爬取开始的网页地址                                           |
| next_page        | 指定下一页（定义restrict_xpath）                             |
| allow_url        | 允许爬取的网页地址                                           |
| deny_url         | 禁止爬取的网页规则                                           |
| extract_from     | xpath表达式，限制解析区域                                    |
| loop_xpath       | xpath表达式，网页地址的列表，表格等iterable的元素            |
| ip_xpath         | xpath表达式，指向ip的xpath                                   |
| ip_img_xpath     | xpath表达式，指向ip图片链接的xpath，用于下载显示ip的图片以供后面图像识别获取 |
| port_xpath       | xpath表达式，指向port的xpath                                 |
| port_img_xpath   | xpath表达式，指向port图片链接的xpath，用于下载显示port的图片以供后面图像识别获取 |
| location1_xpath  | xpath表达式，ip代理的位置1                                   |
| location2_xpath  | xpath表达式，ip代理的位置2                                   |
| speed_xpath      | xpath表达式，指向speed的xpath                                |
| lifetime_xpath   | xpath表达式，指向lifetime的xpath                             |
| type_xpath       | xpath表达式，指向type的xpath                                 |
| level_xpath      | xpath表达式，指向level的xpath                                |
| lastcheck_xpath  | xpath表达式，指向lastcheck的xpath                            |
| enable           | xpath表达式，是否启用该爬取规则，1为启用，0为禁用            |
| selenium_enable  | xpath表达式，是否使用selelnium中间件下载网页（准备改为用splash服务来渲染js页面...），1为启用，0为禁用 |
| proxy_require    | xpath表达式，是否需要使用代理爬取(需要将该模块的配置指向自己的数据库才能用)，1为启用，0为禁用 |
| straight_request | xpath表达式，是否用requests模块直接请求（准备弃用...），1为启用，0为禁用 |

​	其中name，allow_domains， start_urls，allow_url，deny_url， loop_xpath， ip_xpath是必须有的，否则整个程序不能正常进行。

​	添加rule规则后请执行`initDB.py`文件，将规则存入数据库中。否则规则不起作用。

**温馨提示**：

- deny_url一定要设定，不然爬虫会直接结束的，获取不了页面，暂时不明白原因，明白的小伙伴请告知我（邮箱：1306513796@qq.com）！感谢~ 

- 可以用scrapy shell命令来调试xpath，如下：

  `scrapy shell yoururl --spider=proxypool`

	​	

#### 添加item整理规则

​	在item_clean文件夹中创建和rule.name一样的py文件，必须要实现pipline方法来清理整合item。pipline方法接受到的各个字段值都是**列表类型**的，在自定义整理规则之后，没有处理的字段会启用`usual.py`的规则来清理，里面提供了一般speed和lactcheck字段的清理规则，如果字段值是列表类型，则会取列表的第一个值作为字段值。没有设置xpath提取规则的字段值是空字符串。



#### 启动爬虫

​	~~执行`run_proxypool.py`即可启动爬虫爬取。~~

​	执行`run_startspider.py`即可启动爬虫爬取。



*2018-04-09 更新：*

#### IP代理筛选

​	`model`文件夹增加筛选模型`available.py`，模型字段来自于Proxy，意义相同。

​	`utils`文件夹增加筛选机制文件`filter.py`，实现检测离当前时间2小时内获取的IP，删除5小时以外检测过的IP（做过期处理）。

​	直接运行`filter.py`文件即可进行筛选，也可继承`Filter` 类另外实现。



## BUG

​	~~本爬取ip代理框架是基于scrapy的crawlspider实现的，每个allow_url和deny_url是共享allowed_domian的，这可能会使不同的allow_url在个别域名能导致可爬取，也会导致原本deny_url在某些域名中本禁止而爬取不了。我写了7个暂未发生该情况（ip网站不够= =，不介意小伙伴提供一些让我尝试下~）。解决办法：尽量具体deny_url规则和allow_url规则，缩小不同规则的重合范围。~~

​	2018-04-09更新：

​	测试证明上述Bug比较难控制爬虫爬取的范围，第二种方法也确实有效，可以准确的控制爬取范围，~~但在爬虫最后会报错误（start_request重写掉pass，但这不影响爬取结果，主要是对Twisted不熟，不知道怎么挺Spider，有同学知道请告知哈，邮箱：1306513796@qq.com），尚未解决，虽然不影响数据爬取......~~

​	2018-04-10更新：

​	报错误的问题已经解决。scrapy.Spider有close的静态方法，会调用Spider的closed静态方法（需要自己实现的...）,在closed方法中直接kill掉进程就可以了。



## 参考

​	本框架实现是参考了博文[Scrapy学习笔记(7)-定制动态可配置爬虫](http://jinbitou.net/2016/12/05/2244.html)并根据自己需求改良的，感谢该博文的博主分享！

​	在参考博文中，博主是自定义了启动了爬虫方法，个人认为这不便于用scrapyd部署项目和实现分布式爬虫，所以改了结构，使之都集成在一个spider里和不是每条规则都启用一个spider，但会存在隐患（上述提到的bug）。后面有一个思路，即创建一起启动spider，启动spider不进行爬取任务，仅在初始化时候动态生成各个rule的spider进行爬取，实现不同爬取规则的隔离，又可以用scrapyd部署项目和实现分布式爬虫。该思路的初步代码已完成，startspider即是该思路的实现，`run_startspider.py`用于启动爬虫。欢迎小伙伴尝试和修改~

​	2018-04-09更新：

​	测试证明上述思路效果更好，见BUG处描述。

​	2018-04-10更新：

​	遗留问题已经修复。	