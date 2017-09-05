# aocops
#这一个IT信息管理系统
#感谢团队中的jiqin，wsk。
#修改添加目录后请更新此文档
#
___
####此系统基于python2.7 django1.8.3 开发，并在CentOS6和CentOS7正常运行
####模块介绍
	-api #里面包含conf一些可配置信息，例如数据库信息，saltstack信息和自定义的一些脚本模块
	-idcinfo   #数据中心模块 包含了IDC 机柜 设备管理
	-index     #首页各种报表的展现
	-login     #登录验证，找回LDAP密码或通过各种认证的API实现认证登录
	-opsreport #运维详细报表页面
	-static    #一些静态文件存储目录
	-templates #各个模块的模板
	-vminfo    #主机和应用程序APP列表汇总模块 
		   (主机信息获取是依赖saltsatack自动化收集，业务标签需要手动录入。备注如果您的IT运维是基于标准化的可以实现自动化收集分类)
	-vmset     #对于vminfo列表的一些共有属性的分类，例如：维护人，报警类型，业务标签，状态等.
	--settings.py及url.py 请自行生成