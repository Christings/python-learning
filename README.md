## 说明
    code：Python高效实战开发--Django、Tornado、Flask、Twisted的源码
## 一、djangoApps
### 1.1 doubanAPI
    类似于豆瓣图书api，通过restfulAPI给用户提供api，让用户调用api获取内容。
### 1.2 type
    创建一个大型电商类别表;
    定义type表时存在一个问题：
        category_type = models.IntegerField(choices=CATEGORY_TYPE,default='1',verbose_name='类别描述', help_text='类别描述')
        如果不加default，在db中添加字段时提示外键约束；
        如果把default改为null=True,在db中添加字段时提示外键约束,因为parent_category需要的是自身的一个类型，我这么理解的。
        但是如果都不用，数据迁移时不会成功；
    前后端分离；
    解决跨域；
## 二、vueFront——djangoApps的前端程序
    vue环境搭建参考：http://note.youdao.com/noteshare?id=e128d5b1f60e60f3847482708adc9ca7
    
