"""
URL configuration for MyDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include # include为了导入book的urls
from django.shortcuts import HttpResponse # 返回对象
from book import views # 导入book
from django.urls import reverse # 导入路由反转



# 1.url与视图映射
""" https://www.baidu.com/s?wd=python
    把百度网页通过链接映射到python
    
    想要 当前django(http://127.0.0.1:8000) 返回信息
        1.定义视图函数 想要有返回信息 此处需要导包 HttpResponse
        2.映射 urlpatterns列表中添加函数信息

def index(request):
    return HttpResponse("hello world")
"""

# 2.url传参 url主体内容在app文件 views.py


# 5.写路由反转 要求指定的路由必须有名字name
def index(request):
    print(reverse("book_detail_query_string"))
    print(reverse("book_str", kwargs={"book_id":1}))
    return HttpResponse("hello world")

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1.
    # path('index/', index, name='index'), 进入/index包含的内容 也可以不写 就是默认进入就访问
    path('', index),

    # 2
    path('book', views.book_detail_query_string), # 函数的括号删掉

    # 2.
    #path('book/<book_id>', views.book_detail_path),
    path('book/<int:book_id>', views.book_detail_path), # 指定传入参数的数据类型

    # 3.
    path('book/<str:book_id>', views.book_str,name='book_str'),
    path('book/<slug:book_id>', views.book_slug),

    # 4.
    path('book/', include('book.urls')),

    # 5.
    path('book', views.book_detail_query_string,name="book_detail_query_string"),

    # 6.
    path('', views.index,name='index'),

    # 7.
    path('info', views.info,name='info'),

    # 8. url使用
    path('baidu',views.baidu,name='baidu'),

    # 10.include
    path('art',views.art,name='art'),

    # 11.
    path('sta', views.static,name='sta'),

    # 13.
    path('book/add', views.add_book, name='add_book'),
    path('book/query', views.query_book, name='query_book'),
    path('book/order', views.order_book, name='order_book'), # -order_book 加负号 倒序排序
    path('book/update', views.update_book, name='update_book'),
    path('book/delete', views.delete_book, name='delete_book'),

]
