# atp

#### 介绍
自动化测试平台 django2.2 + python3.6.5 + mysql

#### 使用说明
自动化测试平台使用步骤：
（例：接口自动化测试）<br>
    1，添加相关产品<br>
    2，添加接口（app，web）自动化测试用例（用例支持excel导出），测试用例数据存到mysql数据库中<br>
    3，通过sql调用脚本提取mysql数据库中的数据，然后写到对应测试框架中跑自动化测试<br>
    4，依赖jenkins生成对应allure测试报告，并通过jenkins查看对应测试报告结果<br>
    5，allure报告中含有，测试标题，接口地址，请求头信息，传递参数，响应数据，断言信息，log日志数据<br>
    （unittest）<br>
    6，在报告页面查看生成的HTML的测试报告文件存放路径<br>
    7，打开HTML测试报告文件查看测试用例执行情况<br>
    8,简单记录BUG功能；
配置问题：
mysql文件迁移
python manage.py migrate  # 根据数据库迁移文件生成对应SQL语句并执行
python manage.py makemigrations  # 创建数据库迁移文件
![登陆](https://images.gitee.com/uploads/images/2020/0821/174936_c1ffe559_7544664.png "login.png")
![产品页面](https://images.gitee.com/uploads/images/2020/0814/172803_742176da_7544664.png "product.png")
![添加接口用例](https://gitee.com/kuang_yalei/s28/raw/master/%E6%8E%A5%E5%8F%A3%E7%BC%96%E8%BE%91.png "add_apitest.png")
![接口用例列表](https://gitee.com/kuang_yalei/s28/raw/master/%E6%8E%A5%E5%8F%A3%E7%94%A8%E4%BE%8B%E5%88%97%E8%A1%A8.png "api_test.png")
![webUI自动化用例列表](https://images.gitee.com/uploads/images/2020/0814/173305_29362612_7544664.png "web_test.png")
![webUI自动化用例步骤列表](https://images.gitee.com/uploads/images/2020/0814/173339_7abab8a4_7544664.png "web_step.png")
![Bug列表](https://images.gitee.com/uploads/images/2020/0814/173411_687135e9_7544664.png "bug_l.png")
![接口报告页面](https://images.gitee.com/uploads/images/2020/0821/175600_88ea6a28_7544664.png "apis_report.png")
![Allure报告](https://gitee.com/kuang_yalei/s28/raw/master/Allure%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A.png "web_html.png")
