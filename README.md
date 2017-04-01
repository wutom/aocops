# aocops
#这一个不完善的IT信息管理系统，不要作为生产使用。私有云运维平台第一版，完成云基础信息和业务信息的查询汇总报告功能
#感谢团队中的jiqin，wsk。
#修改添加目录后请更新此文档
#
目录结构
├── aocops  # django 主配置目录, setting.py 主配置文件一般不会修改
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── settings.py
│   ├── settings.py20170116.bak
│   ├── settings.pyc
│   ├── urls.py
│   ├── urls.pyc
│   ├── wsgi.py
│   └── wsgi.pyc
├── api   # 各种api接口模块，脚本和信息存储文件目录
│   ├── aliyun #阿里云 目前只有发送短信接口
│   ├── aws #亚马逊 为开发
│   ├── ldap #ldap认证登陆模块
│   │   └── bin
│   │       ├── auth.py
│   │       └── ldapauth.py
│   └── salt #统一主机信息收集及入库，借用salt实现
│       ├── _grains
│       │   ├── ops_grains.py
│       │   └── test.py
│       ├── bin
│       │   ├── salt_db.py #入库脚本
│       │   ├── salt_grains.py #获取主机信息脚本
│       │   └── test_db.py
│       ├── conf #salt 固定配置信息 未编写
│       └── tempfile #信息存储文件
│           ├── app_info.json
│           └── host_info.json
├── index #django首页模块
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── admin.py
│   ├── admin.pyc
│   ├── migrations
│   ├── models.py
│   ├── models.pyc
│   ├── tests.py
│   └── views.py
├── login ##登陆页，包含忘记密码重置跳转
│   ├── admin.py
│   ├── dj_user.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── views.py
├── manage.py #启动主程序
├── start #自定义启动脚本
├── static #静态文件
│   ├── bit33 #正式
│   └── bt33src #源码
├── templates #静态模板文件
│   ├── admin
│   │   └── base_site.html
│   ├── devtest
│   │   └── create_article.html
│   ├── index
│   │   ├── appinfo.html
│   │   ├── bull.html
│   │   ├── dnsfind.html
│   │   ├── footer.html
│   │   ├── head.html
│   │   ├── hostinfo.html
│   │   ├── hostinfo_p.html
│   │   ├── index.html
│   │   ├── search.html
│   │   └── tem_index.html
│   └── login
│       ├── login.html
│       ├── reset.html
│       ├── resetonclick.html
│       ├── resetuser.html
│       └── verify.htm
├── upload #django上传保存目录
│   └── img
│       
├── vminfo #主机基本信息模块
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── admin.py
│   ├── admin.py20161208.bak
│   ├── admin.py20161212.bak
│   ├── admin.pyc
│   ├── migrations
│   ├── models.py
│   ├── models.py20161208.bak
│   ├── models.py20161212.bak
│   ├── models.py20170104.bak
│   ├── models.py20170110.bak
│   ├── models.pyc
│   ├── tests.py
│   └── views.py
└── vmset #后台信息变更模块
    ├── __init__.py
    ├── __init__.pyc
    ├── admin.py
    ├── admin.pyc
    ├── migrations
    │   ├── __init__.py
    │   └── __init__.pyc
    ├── models.py
    ├── models.pyc
    ├── tests.py
    └── views.py

