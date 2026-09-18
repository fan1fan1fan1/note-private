from django.db import models

# Create your models here.



"""
13.model
分继承和不继承两种写法
class Book:   1.不继承
"""
class Book(models.Model): # 2.继承
    name = models.CharField(max_length=100)  # 字符类型char
    author = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now_add=True)  # 自动获取当前时间不用赋值
    price = models.FloatField(default=0)

    """
    id = models.BigAutoField(primary_key=True)
    is_active = models.BooleanField()
    username = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    visit_count = models.IntegerField()
    profile = models.CharField(max_length=200)
    profile = models.TextField()
    website = models.URLField()
    """



    # 15.meta
    class Meta:
        db_table = 'book_table'
        ordering = ['-pub_time']
