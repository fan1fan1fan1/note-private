# 类型注释
""" 变量:类型
    作用 检查工具 对代码进行类型判断 协助做代码提示
    第三方工具IDE 如pycharm
"""

# 基础数据类型注解 常用
var_1: int = 10
var_2: float = 3.14159
var_3: bool = True
var_4: str = "itheimq"


# 类对象类型注解
class Student:
    pass


stu1: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"itheima": 666}
my_str: str = "ithiema"

# 容器详细注解
my_list1: list[int] = [1, 2, 3]
my_tuple2: tuple[str, int, bool] = ("itheima", 666, True)
my_dict1: dict[str, int] = {"itheima": 666}

# 另一种写法
import random     # 用于生成伪随机数的标准库
import json
var_5 = random.randint(1, 10)  # type: int
var_6 = json.loads('{"name": 666}')  # type: dict[str, int]


def func():
    return 10


var_7 = func()  # type: int


# 函数和方法形参注解
def add(x: int, y: int):
    return x + y


# 函数返回值类型注解
def func(data: list) -> list:
    return data


# union类型
from typing import Union

my_list2: list[Union[str, int]] = [1, 2, "itheima", "itcast"]
my_dict2: dict[Union[str, int]] = {"name": "小周", "age": 31}


# 3.多态 : 完成某个具体的行为(函数) 传入不同的对象 通过相关的继承函数或方法 得到不同的状态
# 在继承中 父类函数作为声明 子类对象用于工作
class Animal:
    def speak(self):
        pass  # 抽象类


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)  # 输出：汪汪汪
make_noise(cat)  # 输出：喵喵喵

# 抽象类
""" 含有抽象方法的类 即使用pass空实现
    相当于定义一个标准 包含一些抽象的方法 
    在抽象类中并不定义具体实现方法
    再定义子类要求其实现
"""

# 抽象类定义
class AC:
    def cool_wind(self):
        """制冷"""
        pass  # 不定义具体内容

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass

# 字类定义
class Midea_AC(AC):
    def cool_wind(self):  # 复写 并给出具体内容
        print("制冷科技")

    def hot_wind(self):
        print("制热科技")

    def swing_l_r(self):
        print("无风感左右摆风")

# 配合多态 定义一个函数 用于调用抽象类
def make_cool(ac:AC):
    ac.cool_wind()

# 调用
midea_ac = Midea_AC()
make_cool(midea_ac)



# 使用python操作mysql    pymysql库

from pymysql import Connection
# 1.获取到MYSQL数据库的创建对象
conn = Connection(
    host='localhost',     # 主机名 ID地址
    port=3306,            # 端口 默认3306
    user='root',          # 账户名
    password='Fy051121.', # 密码
    autocommit=True       # 设置自动提交
)

# 2.打印MYSQL数据库软件信息
print(conn.get_server_info())

# 3.执行非查询性质sql语句      使用python在mysql中创建了一张表
# 获取游标对象
cursor = conn.cursor()
conn.select_db("world") # 先选择数据库

# 使用游标对象 执行sql语句
# cursor.execute("create table test_pymysql(id int);")

# 4.执行查询性质的语句
cursor.execute("select * from list")
# 获取查询结果
results: tuple = cursor.fetchall()
for r in results:
  print(r)   # print(results)

# 5.使用python插入数据
# 使用  链接对象.commit()  确认数据
cursor.execute("insert into list value(3, '小周', 31)")
conn.commit() # 手动确认方法

# 自动确认方法 在连接登录数据库时 输入 autocommit=True

# 6.关闭数据库连接
conn.close()



# Spack 分布式计算框架 大数据处理的统一分析引擎
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspark
"""
# 构建pyspark执行环境入口对象   方法:  类 SparkContext (此为入口对象)
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").\
    setAppName("test_spark_app")

# 基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)

# 打印PySpark的运行版本
print(sc.version)

# 停止SparkContext对象的运行 (停止Pyspark程序)
sc.stop()
"""

