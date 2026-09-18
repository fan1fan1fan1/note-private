from flask import Flask,render_template,request,flash   # flask基础
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm # 表单
from wtforms import StringField,PasswordField,BooleanField,SubmitField # 用户注册信息
from wtforms.validators import DataRequired, Email, EqualTo # wtf验证

"""不想写 flash u
import sys
reload(sys)
sys.setfaultencoding("utf-8")
"""


app = Flask(__name__)

app.secret_key = 'itheima'

""" 1.过滤器 列表 第二部分 表单WTForms
    WTForms常用验证函数
        DataRequired    确保字段中有数据
        EqualTo         比较两个字段的值，常用于比较两次密码输入
        Length          验证输入的字符串长度
        NumberRange     验证输入的值在数字范围内
        URL             验证URL
        AnyOf           验证输入值在可选列表中
        NoneOf          验证输入值不在可选列表中
        
        使用Flask-WTF需要配置参数SECRET_KEY。
        CSRF_ENABLED是为了CSRF（跨站请求伪造）保护。SECRET_KEY用来生成加密令牌，当CSRF激活的
        时候，该设置会根据设置的密匙生成加密令牌。在HTML页面中直接写form表单：
    
    使用方法
        1.安装包  
            python -m pip install flask-wtf -i https://pypi.tuna.tsinghua.edu.cn/simple
        2.导包
            from flask import Flask,render_template,request,flash
            from flask_wtf import FlaskForm
            from wtforms import StringField,PasswordField,BooleanField
        3.自定义表单类
        3.
        
        3.写验证函数
        
    例子
    使用WTF实现表单 
    自定义表单类
"""
class LoginForm(FlaskForm):
    # 命名 = 用户名信息,验证
    username = StringField('用户名:',validators=[DataRequired()])
    password = PasswordField('密码:',validators=[DataRequired()])
    password2 = PasswordField('确认密码:',validators=[DataRequired(),EqualTo('password', '密码填写不一致')])
    submit = SubmitField('提交')

@app.route('/form', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('index.html', form=form)

@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm() # 创建对象

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        print(username,password,password2)

        """
        if not all([username,password,password2]):
            flash('参数不完整')
        elif password != password2:
            flash('密码不一致')
        else:
            return 'ok'
        """
        # 验证
        # 此处需要一个CSRF token
        if login_form.validate_on_submit():
            print(username,password,password2)
            return 'success'
        else:
            flash('参数有误')
    return render_template('index.html',form=login_form)





# .蓝图
"""
from book import bookbp
app.register_blueprint(bookbp,url_prefix='/book')
"""




# 数据库 flask-sqlalchemy
""" 1.安装 
        python -m pip install flask-sqlalchemy
        
    2.如果连接的是mysql数据库, 需要安装mysqldb
        python -m pip install flask-mysqldb
        
    3.使用Flask-SQLAlchemy管理数据库
        在Flask-SQLAlchemy中，数据库使用URL指定，而且程序使用的数据库必须保存到Flask配置对象的
        SQLALCHEMY_DATABASE_URI键中。
        
    4.Flask的数据库设置：
        app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:mysql@127.0.0.1:3306/test
        
    5.其他设置：
        # 动态追踪修改设置，如未设置只会提示警告， 不建议开启
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        #查询时会显示原始SQL语句
        app.config['SQLALCHEMY_ECHO']= True
        
    6.相关指令
        SQLALCHEMY_DATABASE_URI
        用于连接的数据库 URI 。例如：sqlite:////tmp/test.dbmysql://username:password@server/db
        
        SQLALCHEMY_BINDS
        一个映射 binds 到连接URI的字典。更多 binds的信息见用Binds 操作多个数据库。
        
        SQLALCHEMY_ECHO
        如果设置为Ture， SQLAlchemy 会记录所有 发给 stderr 的语句，这对调试有用。（打印sql语句）
        
        SQLALCHEMY_RECORD_QUERIES
        可以用于显式地禁用或启用查询记录。查询记录 在调试或测试模式自动启用。更多信息见get_debug_queries()。
        
        SQLALCHEMY_NATIVE_UNICODE
        可以用于显式禁用原生 unicode 支持。当使用 不合适的指定无编码的数据库默认值时，这对于一些数据库适配器是必须的
        （比如Ubuntu上某些版本的PostgreSQL）。
        
        SQLALCHEMY_POOL_SIZE
        数据库连接池的大小。默认是引擎默认值（通常 是5）
        
        SQLALCHEMY_POOL_TIMEOUT
        设定连接池的连接超时时间。默认是10。
        
        SQLALCHEMY_POOL_RECYCLE
        多少秒后自动回收连接。这对 MySQL 是必要的， 它默认移除闲置多于 8 小时的连接。注意如果 使用了 MySQL， 
        Flask-SQLALchemy 自动设定 这个值为2小时。
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Fy051121.@127.0.0.1:3306/test'
          # 直接运行 通过报错可以得到这个变量           用户名   密码        地址         命名
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # 可能已经废弃了
db = SQLAlchemy(app)



""" 常用的SQLAlchemy列选项
    primary_key   如果为True，代表表的主键
    unique        如果为True，代表这列不允许出现重复的值
    index         如果为True，为这列创建索引，提高查询效率
    nullable      如果为True，允许有空值，如果为False，不允许有空值
    default       为这列定义默认值

    常用的SQLAlchemy关系选项 
    backrefl        在关系的另一模型中添加反向引用
    primary         join 明确指定两个模型之间使用的联结条件
    uselist         如果为False，不使用列表，而使用标量值
    order_by        指定关系中记录的排序方式
    secondary       指定多对多中记录的排序方式
    secondary join  在SQLAlchemy中无法自行决定时，指定多对多关系中的二级联结条件
    
    例 写两张表 角色(管理员/普通用户)
              用户(ID)
    
    模型关联 一对多 
        users = db.relationship('User', backref='role')
"""
class Role(db.Model):
    __tablename__ = 'roles' # 表名

    # 定义字段 do.Column表示一个字段
    id = db.Column(db.Integer, primary_key=True)  # 表示主键
    name = db.Column(db.String(64), unique=True)  # 表明不能出现重名

    # 在一的一方，写关联
    # users = db.relationship('User')：表示和User模型发生了关联，增加了一个users属性
    # backref='role'：表示role是User要用的属性
    users = db.relationship('User', backref='role')

    # repr()方法显示一个可读字符串
    def __repr__(self):
        return '<Role: %s %s>' %(self.name, self.id)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 表示外键 表名.id

    # User希望有role属性，但是这个属性的定义，需要再另一个模型中定义

    # 可读字符串
    def _repr_(self):
        return '<User:%s %s %s %s>'% (self.name, self.id, self.email, self.password)


""" 数据库增删改操作
1.基本概念
    在Flask-SQLAlchemy中，插入修改、删除操作，均由数据库会话管理。
        会话用db.session表示。在准备把数据写入数据库前，要先将数据添加到会话中然后调用 commit()方法提交会话。
    在Flask-SQLAlchemy中，查询操作是通过query对象操作数据。
        最基本的查询是返回表中所有数据，可以通过过滤器进行更精确的数据库查询。

    db.session.add(role)                添加到数据库的session中
    db.session.add_all([user1,user2])   添加多个信息到session中
    db.session.commit()                 提交数据库的修改（包括增/删/改）
    db.session.rollback()               数据库的回滚操作
    db.session.delete(user)             删除数据库(需跟上commit)
    
2.常用的SQLAlchemy查询过滤器
    filter()    把过滤器添加到原查询上，返回一个新查询
    filter_by() 把等值过滤器添加到原查询上，返回一个新查询
    limit       使用指定的值限定原查询返回的结果
    offset()    偏移原查询返回的结果，返回一个新查询
    order_by()  根据指定条件对原查询结果进行排序，返回一个新查询
    group_by()  根据指定条件对原查询结果进行分组，返回一个新查询

3.常用的SQLAlchemy查询执行器
    all()           以列表形式返回查询的所有结果
    first()         返回查询的第一个结果，如果未查到，返回None
    first_or_404()  返回查询的第一个结果，如果未查到，返回404
    get()           返回指定主键对应的行，如不存在，返回None
    get_or_404()    返回指定主键对应的行，如不存在，返回404
    count()         返回查询结果的数量
    paginate()      返回一个Paginate对象,它会指定范围内的结果
"""



""" 模拟使用
1.(电脑终端)在终端创建一个数据库                 mysql -uroot -pFy051121.
2.(电脑终端)加中文标识                         create database test charset=utf8;
3.(电脑终端)开启数据库                         use test;
3.运行代码
4.(电脑终端)                                show tables;
5.(电脑终端)                                desc roles;
6.(电脑终端)                                desc user;
7.打开pycharm终端
8.(pycharm终端)                            ipython  / python
9.(pycharm终端)运行所有                      from test import *;
10.(pycharm终端)添加角色                     role = Role(name='admin')
11.(pycharm终端)                           db.session.add(role)
12.(pycharm终端)                           db.session.commit()
13.(电脑终端)                               select * from users;

1.(pycharm终端)删除                         db.session.delete(user)
2.(pycharm终端)                            db.session.commit()
3.(pycharm终端)                            exit

1.(pycharm终端)                            ipython  / python
2.(pycharm终端)运行所有                      from test import *;
3.(pycharm终端)添加角色                      role = Role(name='admin')
4.(pycharm终端)                            db.session.add(role)
5.(pycharm终端)                            db.session.commit()
6.(电脑终端)                                select * from users;
7.(pycharm终端)                            user1 = User(name='z', role_id=role.id)
8.(pycharm终端)                            user2 = User(name='s', role_id=role.id)
9.(pycharm终端)                            db.session.add_all([user1, user2])
10.(pycharm终端)                           db.session.commit()
11.(电脑终端)                               select * from users;
12.(pycharm终端)                           role.user
12.(pycharm终端)                           user1.role

13.添加数据后 (pycharm终端)                  User.query.all()
"""



if __name__ == '__main__':
    # 数据库操作写此处
    db.drop_all() # 代码运行前先删除库 这样就不会有内存残留 重复生成

    db.create_all()
    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()
    # 再次插入一条数据
    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()
    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    us5 = User(name='tang', email='tang@itheima.com', password='158104', roleid = ro2.id)
    us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    db.session.add(all([us1, us2, us3, us4.us5.us6.us7.us8.us9.us10]))
    db.session.commit()

    app.run(debug=True, host="0.0.0.0", port=2000)



