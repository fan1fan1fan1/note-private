"""
1.安装
    pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple

2.新建文件 可以先创建项目 后生成django
    python -m django startproject MyDjango .

3.新建文件夹app
    python manage.py startapp book

4.代码

5.运行django 终端
    python manage.py runserver


运行mysql
1.setting中输入数据库信息

2.view中导包 def 数据库函数
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

3.运行django

4.迁移
    python manage.py migrate

5.重新启动
    python manage.py runserver

6.生成迁移文件 migrations
    python manage.py makemigrations
"""


