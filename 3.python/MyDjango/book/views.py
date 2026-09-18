from django.contrib.sites import requests
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.



# 2.url传参
"""
方法一: 通过查询字符串(query string)
    https://www.baidu.com/s?wd=python&wd=python&a=1&b=2
                                      ↑参数
方法二: 在path中携带 http://127.0.0.1:8000/book/2
                                             ↑参数
"""

# 查询字符串
def book_detail_query_string(request):
    # request.GET = {"id":3}
    book_id = request.GET.get('id')  # request.GET['id']同效果但不推荐
    return HttpResponse(f"您查找的图书id是: {book_id} ")
# http://127.0.0.1:8000 进入首页
# http://127.0.0.1:8000/book 进入book页 但内容为空
# http://127.0.0.1:8000/book?id=3 进入book页 内容id=3


# 在path中携带
def book_detail_path(request,book_id):
    return HttpResponse(f"您查找的图书id是: {book_id} ")



# 3.path函数
""" path(route,view,name=None,kwargs=None)
str：非空的字符串类型。默认的转换器。但是不能包含斜杠。
int：匹配任意的零或者正数的整形。到视图函数中就是一个int类型。
slug：由英文中的横杠-，或者下划线-连接英文字符或者数字而成的字符串。
uuid：匹配uuid字符串。
path：匹配非空的英文字符串，可以包含斜杠/。

view:视图函数
name:命名
"""
def book_str(request, book_id):
    return HttpResponse(f"您查找的图书id是：{book_id}")

def book_slug(request, book_id):
    return HttpResponse(f"您查找的图书id是：{book_id}")



# 4.路由模块化
# views不写路由东西 在项目文件中创建 urls文件 负责和主文件的urls路由映射
def movie_list(request, movie_id):
    return HttpResponse("电影列表")
def movie_detail(request, movie_id):
    return HttpResponse(f"您获取的电影id是:{movie_id}")



# 5.路由反转
# 根据给定的路由命名找回路由



# 6.模板渲染 render
from django.shortcuts import render
def index(request):
    return render(request,'index.html')



# 7.模板变量 字典类型
def info(request):
    # 传参
    username = '知了'
    book = {'name':"水浒传",'author':'施耐庵'}
    class Person:
        def __init__(self,name):
            self.name = name

    context = {
        'username': username,
        'book': book,
        'Person': Person('知了课堂'),

        # if
        'age': 18,

        # for
        # for x in person.items/keys/values
        # break/continue 在模板中不存在
        'books': [{'name': '水浒传'}, {'name': '三国演义'}],  # 循环用的图书列表
        'person': {  # 循环用的字典
            'realname': "知了课堂",
            'age': 18,
            'height': 180
        }
    }


    # 如果没写整个context
    # return render(request,'info.html',context={'username':username,'book':book,'context':context})

    # 如果写了包含所有变量的context
    return render(request,'info.html',context)



# 8.模板渲染常见标签
"""
1.if
2.for 写在了上面
3.with 当一个变量的访问较复杂时 可以把该变量缓存到另一个变量上 然后再访问该变量 -> 变量再次命名
4.url
"""
def baidu(request):
    return redirect("https://www.baidu.com")



# 9.模板过滤器
"""
add
cut
date
default
default_if_none
first
last
floatformat
join
length
"""



# 10.模板结构
"""
1.include
    {% include "base.html" %}
2.模板继承 继承可以有多位置 如果用到了extends 该句必须在第一句写
    假设有block.html为父
        <head>
            <meta charset="UTF-8">
            <title>{% block title %}{% endblock %}</title>
        </head>    
        <body>
            {% block body %}{% end block %}
        </body>
    
    index.html为子
        {% extends "base.html" %}
"""

def art(request):
    return render(request,'article.html')



# 11.加载静态文件
def static(request):
    return render(request,'static.html')



# 12.mysql
from django.db import connection
def sql(request):
    # 获取游标对象
    cursor = connection.cursor()
    # 拿到游标对象后执行sql语句
    cursor.execute("select * from list")
    # 获取所有的数据
    rows = cursor.fetchall()
    # 遍历查询到的数据
    for row in rows:
        print(row)
    return HttpResponse("查找成功")

""" mysql驱动安装
我们使用Django来操作MySQL，实际上底层还是通过python来操作的。因此我们想要用Django来操作MySQL，首先还是需要安装一个
驱动程序。在python3中，驱动程序有多种选择。比如有pymysq1以及mysqlclient等。这里我们就使用mysqlc1ient来操作。
mysqlclient安装非常简单。只需要通过pip install mysqlclient即可安装。

常见MySQL驱动介绍：
1.MySQL-python：也就是MySQLdb。是对C语言操作MySQL数据库的一个简单封装。遵循了python DB API v2。但是只支持
  Python2，目前还不支持Python3。
2.mysq1client:
  是MySQL-python的另外一个分支。支持Python3并且修复了一些bug。
3.pymysq1：纯python实现的一个驱动。因为是纯python编写的，因此执行效率不如MySQL-python。并且也因为是纯python编写
  的，因此可以和Python代码无缝衔接。
4.MySQL Connector/Python：MySQL官方推出的使用纯Python连接MySQL的驱动。因为是纯Python开发的。效率不高。
"""

""" cursor对象常用接口：
1.description：如果cursor执行了查询的sq1代码。那么读取cursor.description属性的时候，将返回一个列表，这个列表中装
    的是元组，元组中装的分别是(name, type_code, display_size, internal_size,precisionscale，nu11_ok)，其中name代表的
    是查找出来的数据的字段名称，其他参数暂时用处不大。
2.rowcount：代表的是在执行了sq1语句后受影响的行数。
3.close：关闭游标。关闭游标以后就再也不能使用了，否则会抛出异常。
4.execute(sql[, parameters])：执行某个sq1 语句。如果在执行sq1语句的时候还需要传递参数，那么可以传给parameters参
    数。示例代码如下：
                    cursor.execute("select  from article where id=%s",(1,))
5.fetchone：在执行了查询操作以后，获取第一条数据。
6.fetchmany(size)：在执行查询操作以后，获取多条数据。具体是多少条要看传的size参数。如果不传size参数，那么默认是获
    取第一条数据。
7. fetcha11：获取所有满足sq1语句的数据。
"""



# 13.orm指令    object relational mapping 对象关系映射
""" 1.创建ORM模型：
    ORM模型一般都是放在app的models.py文件中。每个app都可以拥有自己的模型。并且如果这个模型想要映射到数据库中，那么这个app
    必须要放在settings.py的INSTALLED_APP中进行安装。以下是写一个简单的书籍ORM模型。示例代码如下：
        from django.db import models
        class Book(models.Model):
            name = models.CharField(max_length=20, nu11=False)
            author = models.charField(max_length=20,nu11=False)
            pub_time = models.DateTimeField(auto_add_now=True)
            price = models.FloatField(default=0)
            
    2.增删改查
"""
# (2.增加
from book.models import Book
from .models import Book
def add_book(request):
    book = Book(name='三国演义', auther='罗贯中', price=100)
    book.save()
    return HttpResponse('添加成功')

# (3.查询
def query_book(request):
    books1 = Book.objects.all()
    for book in books1:
        print(book.name, book.author, book.price)

    # (4.过滤
    books2 = Book.objects.filter(name='三国演义')
    for book in books2:
        print(book.name, book.author, book.price)

    # (5.获取
    book = Book.objects.get(name='三国演义')
    print(book.name, book.author, book.price)

    try:
        book = Book.objects.get(name='三国演义11')
        print(book.name)
    except Book.DoesNotExist:
        print("图书不存在!")

    return HttpResponse("查找成功!")

# (6.排序
def order_book(request):
    books = Book.objects.order_by('-price')
    for book in books:
        print(book.name, book.author, book.price)
    return HttpResponse('排序成功!')

# (7.修改
def update_book(request):
    books = Book.objects.first()
    books.name = '西游记'
    books.save()
    return HttpResponse('修改成功!')

def delete_book(request):
    books = Book.objects.filter(name='西游记')
    books.delete()
    return HttpResponse('删除成功!')



# 14.field参数
""" 在Django中，定义了一些Field来与数据库表中的字段类型来进行映射。以下将介绍那些常用的字段类型。
1.AutoField: 映射到数据库中是int类型，可以有自动增长的特性。一般不需要使用这个类型，如果不指定主键，那么模型会自
            动的生成一个叫做id的自动增长的主键。如果你想指定一个其他名字的并且具有自动增长的主键，使用AutoField也是可以的。
2.BigAutoField: 64位的整形，类似于AutoField，只不过是产生的数据的范围是从1-9223372036854775807。
3.BooleanField: 在模型层面接收的是True/False。在数据库层面是tinyint类型。如果没有指定默认值，默认值是None。
4.CharField: 在数据库层面是varchar 类型。在 Python 层面就是普通的字符串。这个类型在使用的时候必须要指定最大的长
             度，也即必须要传递max_1ength这个关键字参数进去。
5.DateField: 日期类型。在 python 中是datetime.date类型，可以记录年月日。在映射到数据库中也是date类型。使用这个
             Field可以传递以下几个参数：
                1.auto_now 在每次这个数据保存的时候，都使用当前的时间。比如作为一个记录修改日期的字段，可以将这个属性设置为True。
                2.auto_now_add；在每次数据第一次被添加进去的时候，都使用当前的时间。比如作为一个记录第一次入库的字段，可以将这个属性设置为True。
6.DateTimeField: 日期时间类型，类似于DateField，不仅仅可以存储日期，还可以存储时间。映射到数据库中是datetime类型。
                 这个Field也可以使用auto_now和auto_now_add两个属性。
7.TimeField: 时间类型。在数据库中是time类型。在Python中是datetime.time类型。
8.EmailField: 类似于CharField。在数据库底层也是一个varchar类型。最大长度是254个字符。
9.FileField: 用来存储文件的。这个请参考后面的文件上传章节部分。
10.ImageField: 用来存储图片文件的。这个请参考后面的图片上传章节部分。
11.FloatField: 浮点类型。映射到数据库中是float类型。
12.IntegerField: 整形。值的区间是-2147483648--2147483647。
13.BiglntegerField: 大整形，值的区间是 -9223372036854775808-9223372036854775807
14.PositivelntegerField: 正整形。值的区间是0--2147483647。
15.SmalllntegerField: 小整形。值的区间是-32768--32767。
16.PositiveSmalllntegerField: 正小整形。值的区间是0--32767.
17.TextField: 大量的文本类型。映射到数据库中是Iongtext类型。
18.UUIDField: 只能存储 uuid格式的字符串。 uuid是一个32位的全球唯一的字符串，一般用来作为主键。

19.null
20.blank
21.db_column
22.default
23.primary_key
24.unique
"""



# 15.meta配置
""" 对于一些模型级别的配置。我们可以在模型中定义一个类，叫做Meta。然后在这个类中添加一些类属性来控制模型的作用。
    比如我们想要在数据库映射的时候使用自己指定的表名，而不是使用模型的名称。那么我们可以在Meta类中添加一个db_table的属性。
    示例代码如下：
        class Book(models.Model)
            name = models.charField(max_length=20,nu11=False)
            desc = models.charField(max_length=100,name='description', db_column="description1")
            class Meta:
                db_table = 'book_mode1'


    db_table: 这个模型映射到数据库中的表名。如果没有指定这个参数，那么在映射的时候将会使用模型名来作为默认的表名。
    ordering: 设置在提取数据的排序方式。后面章节会讲到如何查找数据。比如我想在查找数据的时候根据添加的时间排序，
    示例代码如下：
    class Book(models.Model):
        name = models.CharField(max_length=20,nu11=False)
        desc = models.charField(max_length=100, name='description', db_column="description1")
        pub_date = models.DateTimeField(auto_now_add=True)
        class Meta:
            db_table = 'book_mode1'
            ordering = ['pub_date','name']
"""



# 16.数据库外键