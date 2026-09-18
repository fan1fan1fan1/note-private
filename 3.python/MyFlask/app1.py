# flask安装
# pip install flask
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask

"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "****"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)

点击运行后 打开运行结果的链接数据 打开页面
"""

""" jinja2模板
        static文件夹 存放静态文件
        templates文件夹 存放jinja2模板
        app1.py 项目入口
    
    flask文件仅通过.py即可实现 多文件的为jinja2
"""

# -----------------------------------------------------------------------------------


# 一、导包
from flask import Flask

# 二、使用flask创建了一个对象
app = Flask(__name__)

""" __name__ 代表当前app.py这个模块
    1.出现bug时可以帮助我们快速定位
    2.对于寻找模块文件 提供一个相对路径
"""



# 三、创建一个路由和视图函数的映射 通过装饰器实现
"""
@app.route('/')     # '/' 根路由(路径)  装饰器  可多写
def home():
    return "Hello, Flask!"  # 可改
"""

@app.route('/profile')
def profile():
    return "我是个人中心"  # 访问路径 port后 + /profile   进入访问

""" 带参数的url 路由传参
运行后并不会输出以下def内容 在路由参数里 运行结果的链接打开后在最末添加route参数 打开链接 会出现内容

@app.route('/blog/<blog_id>')  # 此处的<>内容为路由参数    <blog_id>
def blog_detail(blog_id):
    return "您访问的博客是: %s" % blog_id  # 格式化输出  "输出文字信息 %数据类型" % 路由参数

"""

""" 路由参数可以进行优化 设定数据类型 没有空格
@app.route('/blog/<int:blog_id>')
@app.route('/blog/<float:blog_id>')

当在链接中输入错误数据类型时 不会进行访问
"""

# --------------------------------------------------------------------------------------

# 1.debug
""" 环境变量中添加FLASK_DEBUG 1
    1.便于修改后查看结果
    2.便于查找bug
"""

# 2.修改host
""" host域名 主机名 (数字链接地址)
    作用 让其他电脑可以通过该链接访问数据
"""

# 3.修改port
""" port端口号
    监听的端口号 0-65535
    默认5000 若5000端口被占用了 可以通过这种方式运行
"""


# 4.URL与视图
"""
    1.url: https://www.qq.com
           https://www.qq.com:443/path
                                  path位置为可修改部分
    
    http多用80端口 https 443端口
    
    2.url与视图 -> path与视图
    
    3.url重定向
    projects的URL是中规中矩的，尾部有一个斜杠，看起来就如同一个文件夹。访问一个没有斜杠结尾的URL(/projects)时
        Flask会自动进行重定向，帮您在尾部加上一个斜杠(/projects/)。

    简单理解：如果你的路由带了反斜杠那你再访问的时候可以不带因为他会自动帮你加上，但是如果你的路由没有反斜杠你杠上了就会报错
        就一定内容后还有一个斜杠
"""
# 以下两条规则的不同之处在于是否使用尾部的斜杠。
@app.route('/projects/')
def projects():
    return 'The project page'
@app.route('/about')
def about():
    return 'The about page'
# about 的URL没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这个URL 时添加了尾部斜杠(/about/)就会得到一个 404
# “未找到”错误。这样可以保持URL唯一，并有助于搜索引擎重复索引同一页面。



# 5.使用jinja2的函数 返回一个网页 .html
from flask import render_template  # jinja2渲染模板


@app.route('/blog/<int:blog_id>')  # 无法在此处运行 可以拿出去运行
def blog(blog_id):
    return render_template("index.html", blog_id = blog_id)  # 在html文件中传参

# 在index.html中要访问这里的内容 要用双大括号 {{ }}



# render_template flask模板
# 6.模板中访问对象属性
class User:
    def __init__(self,username,email):  # 通过视图传递给html
        self.username = username
        self.email = email


# 传入数据类型多样
@app.route('/')
def index():
    url_str = "www.baidu.com"
    my_list = [1, 5, 3]
    my_dict = {"name": "zhangsan", "email": "@qq.com"}
    # 加上这两个
    user = User("李四", "lisi@qq.com")
    person = {"name": "张三", "email": "zhangsan@qq.com"}

    return render_template("index.html",url_str=url_str,my_list=my_list,my_dict=my_dict,
                           user=user,  # 加上
                           person=person  # 加上
    )



@app.route('/variable')  # 路由
def variable():   # 定义数据
    hobby = "游戏"
    person = {
        "name": "张三",  # 字典
        "email" : "zhangsan@qq.com"
    }
    user = User("李四", "lisi@qq.com")
    # 传递
    return render_template("index.html", hobby=hobby, person=person, user=user)



# 7.request对象
# 路由默认会使用get post需要手动指定
from flask import request
@app.route('/request',methods=['GET'])  # 指定 methods=['POST']
def indexx():
    # 发送get请求
    print(request)
    print(request.args)
    print(request.args.get('page'))
    print(request.args.get('pagenum'))

    # 发送post请求
    """
    if request.method == 'POST':
        #print('post')
        print(request.json.get('name'))
        return "post"
    """
    return render_template('index.html')

# 使用postman进行测试 运行后把链接输入道postman窗口 选择get post请求 输出 看是否正确



# 8.控制代码块 if for switch

# 9.过滤器
""" (1)字符串操作
        safe：禁用转义
        capitalize：把变量值的首字母转成大写，其余字母转小写
        lower：把值转成小写
        upper：把值转成大写
        title：把值中的每个单词的首字母都转成大写
        reverse：字符串反转
        format：格式化输出
        striptags：渲染之前把值中所有的HTML标签都删掉
        truncate: 字符串截断
    
    (2)列表操作
        first：取第一个元素
        last：取最后一个元素
        length：获取列表长度
        sum：列表求和
        sort：列表排序
"""


# web表单
""" 1.表单标签 2.表单域 3.表单按钮
    
    使用Flask-WTF扩展
    
    StringField         文本字段
    TextAreaField       多行文本字段
    PasswordField       密码文本字段
    HiddenField         隐藏文件字段
    DateField           文本字段，值为 datetime,date 文本格式
    DateTimeField       文本字段，值为 datetime.datetime 文本格式
    IntegerField        文本字段，值为整数
    DecimalField        文本字段，值为decimal.Decimal
    FloatField          文本字段，值为浮点数
    BooleanField        复选框，值为True 和 False
    RadioField          一组单选框
    SelectField         下拉列表
    SelectMutipleField  下拉列表，可选择多个值
    FileField           文件上传字段
    SubmitField         表单提交按钮
    FormField           把表单作为字段嵌入另一个表单
    FieldList           一组指定类型的字段

    
        
    写个例子
    目的：实现一个简单的登录的逻辑处理
    1.路由需要有get和post两种请求方式 --> 需要判断请求方式
    2.获取请求的参数
    3.判断参数是否填写 & 密码是否相同
    4. 如果判断都没有问题，就返回一个success
"""


app.secret_key = 'itheima' # 密钥

# 10.flash   消息闪现
from flask import request,flash
# 此处flash 给模板传递消息 需要一个混淆密钥

# 例子
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_again = request.form['password_again']
        print(username, password, password_again)

        if not(username and password and password_again):  # if not all([...])
            #print('参数不完整')
            flash(u'参数不完整')
        elif password != password_again:
            #print('密码不一致')
            flash(u'密码不一致')
        else:
            return 'ok'
    return render_template('index.html')


# --------------------------------------------------------------------------------------

# 四、主入口判断
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2000)

