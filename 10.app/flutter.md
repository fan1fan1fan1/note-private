## flutter环境

1.安装flutter环境
 https://docs.flutter.dev/install/manual

2.增加环境变量  path中增加bin的路径

3.cmd 输入flutter

4.使用git 输入flutter
	git中输入clear清屏

5.git中输入 flutter doctor 验证是否成功

6.处理问题:
[!] Network resources
   X A network error occurred while checking "https://maven.google.com/": 信号灯超时时间已到
! Doctor found issues in 2 categories.

在环境变量中直接新建
变量名 = FLUTTER_STORAGE_BASE_URL
变量值 = https://storage.flutter-io.cn
变量名 = PUB_HOSTED_URL
变量值 = https://pub.flutter-io.cn

7.安装android stdio
	打包方法 左上角 build  generate App Bundles or APKs 选APK

8.进入新建项目后 需要更改 gradle/wrapper/ .properties的distributionUrl 改成国内镜像

9.安装mumu模拟器用于android stdio模拟安卓手机 开启网络桥接模式

10.继续完善flutter 在android stdio中找到设置 sdk

11.sdk tools 中 android sdk command-line Tools 下载 apply

12.git中输入 flutter doctor --android-licenses

13.环境变量 path 添加 D:\22820\SDK\platform-tools

14.如果git   flutter doctor中仍不是全对号 toolchain
	(1)android stdio左上角tools   SDK manager 复制上方路径
	(2)git执行flutter config --android-sdk "复制路径"
	(3)flutter doctor --android-licenses
	(4)flutter doctor

15.配置flutter会得到dart环境
	验证dart指令 git中输入 dart --version

16.dart语言主要使用编辑器 Trae   (AI编辑器)

17.在Trae中安装Dart插件
	Trae介绍: 有两种ai编程模式 

​		(1) Tap/CUE 在设置中可以选择   在写代码时点击tap键可以自动填充
	        (2) Builder协作模式 运用对话框 vide coding

18.开始学习Dart







## 执行Flutter项目

#### 1.git中先指定要创建的项目位置 

​	cd D:xxx\xxx     注意是\不是/



#### 2.创建项目(web)   

​	输入   flutter create --platforms web 项目名称



#### 3.Trae中安装插件

​	Flutter 和 Awesome Flutter Snippets



#### 4.需要chrome浏览器



#### 5.Trae中打开创建的项目 

​	lib目录下的main.dart



#### 6.点击主函数上的run / Trae右下角Chrome英语  

 (默认打开的是一个按钮计数器)



#### 7.解析Flutter项目目录

​	(1) .开头的文件      不用在意 编辑器自动生成的缓存之类
	(2) lib                      源代码                                                 (重要)
	(3) test                    单元测试
	(4) web                   web平台的配置和资源文件 不用在意
	(5) pubspec.yaml   项目依赖和配置文件                           (重要)
	(6) build                  打包时需要



#### 8.启动runApp和Widget

​	runApp函数是Flutter内部提供的一个函数 启动一个Flutter应用就是从调用这个函数开始的
	widget表示控件 组件 部件 的含义  Flutter中万物皆Widget 一个项目就是由不同的widget组合起来的



#### 9.Flutter默认Material库

​	设计风格 打开计数器那个风格 可以统一交互和视觉体验



#### 10.基础组件 MaterialApp (类似前端的html框架)

​	特性:整个应用被MaterialApp包裹 方便我们对整个应用的属性进行整体设计
	属性: title 标题部分 可选
		 theme 主题
		 home 内容主体
	home部分中包含Scaffold组件 用于构建Material Design风格的核心组件 包含属性:
		appBar                             页面顶部的应用栏，通常用于显示标题、导航按钮和操作菜单
		body                                 页面的主要内容区域，可以放置任何其他组件，是页面的核心
		bottomNavigationBar       底部导航栏，方便用户在不同核心功能页面间切换
		backgroungColor             设置整个 Scaffold 的背景颜色
		floatingActionButton        悬浮操作按钮，常用于触发页面的主要动作

全文件只要有一个MaterialApp



#### 11.Flutter自定义组件

​	无状态组件 有状态组件

特性            	 StatelessWidget（无状态）   		     	StatefulWidget（有状态）
核心特征     	 一旦创建，内部状态不可变                     	持有可在其生命周期内改变的状态
使用场景      	 静态内容展示，外观仅由配置参数决定  	交互式组件，如计数器、可切换开关、表单输入框
生命周期     	 相对简单，主要是构建(build)		                更为复杂，包含状态创建、更新和销毁
代码结构		              单个类 						两个关联的类：Widget 本身和单独的 State 类

###### (1) 无组件状态 StatelessWidget: 

​	定义一个类 继承StatelessWidget类并实现build方法    返回值为Widget

###### (2) 有组件状态 StatefulWidget: 

​	动态交互 状态改变时 组件会及时更新

​	定义两个类 第一个类继承StatelessWidget类 接收和定义最终参数 核心是创建State对象

​			   第二个类继承State第一个类名 管理所有可变数据和业务逻辑 实现build  返回一个Widget



#### 12.点击事件

GestureDetector    使用GestureDetector包裹被点击的元素 传入onTap方法

组件类别                             核心组件                    			 主要特点/适用场景

专用按钮组件        ElevatedButton、 TextButton.       		内置点击动画和样式，通过onPressed参数处理点击逻辑
			   OutlineButton、 FloatingActionButton
视觉反馈组件                       InkWell                                        提供点击事件(onTap)，有MaterialDesign风格的水纹扩散效果
其他交互组件        IconButton、Switch、Checkbox                具有特定功能的交互式控件、点击事件(onPressed)



#### 13.状态更新 setState

计数器



#### 14.组件生命周期 有状态组件

生命周期阶段          函数名                                    调用时机与核心任务
创建阶段			createState()                          Widget初始化调用，创建State对象
				init5tate()                                State对象插入Widget树立刻执行，仅执行一次
				didChangeDependencies()    initState后立刻执行，当所依赖的InheritedWidget更新时调用，可能多次

构建与更新阶段	build()                         	       构建UI方法，初始化或更新后多次调用
				didUpdateWidget()                 父组件传入新配置时调用，用于比较新旧配置

销毁阶段			deactiveate()                          当State对象从树中智时移除时调用
				dispose()                                当Statc对象被永久移除时调用，释放资源，仅执行一次



#### 15.布局组件

组件类别			核心组件				                  主要特点/使用场景
基础容器	     Container、 Center、 Align、 Padding	  提供装饰、对齐、边距等基础样式和布局控制，是使用频率极高的组件
线性布局	     Row、Column					          在水平或垂直方向线性排列子组件，是构建界面的基础
弹性布局       Flex, Expanded, Flexible		                  按照比例分配剩余空间，实现自适应布局，常与Row和Column配合使用
层叠布局       Stack, Positioned                                         让子组件重叠堆叠，用于实现如图片上叠加文字、悬浮按钮等效果
流式布局	      Wrap, Flow						  当主轴空间不足时自动换行或换列，常用于标签、滤镜等动态宽高内容的排列
滚动布局        ListView, GridView					   提供可滚动的列表或网格视图，高效展示大量数据



#### 16.文本组件

属性			类型			作用说明
data			String		必需。要显示的文本内容。
style			TextStyle		文本样式，可设置颜色、大小、粗细等。
textAlign		TextAlign		文本在容器内的水平对齐方式，如 .left, .center。
maxLines		int			文本显示的最大行数。



#### 17.文本输入组件

属性				作用说明
controller			文本编辑器控制器，用于获取、设置文档内容及监听变化
decortation		当时输入框的外观、如标签、提示文字、图标、边框等
style				定义输入文本的样式
maxLines			最大行数
onChanged		输入内容发生变化时执行的回调函数
onSubmitted		用户提交输入时的回调函数



#### 18.图片

分类					作用说明
Image.asset()			加载项目资源目录(assets)中的图片。需要在 pubspec.yaml文件中声明资源路径
Image.network()		直接从网络地址加载图片
Image.file()			加载设备本地存储中的图片文件
Image.memory()		加载内存中的图片数据

常用属性：
分类			类型					作用说明
width/ height   double				设置图片显示区域的宽度和高度
fit			BoxFit				控制图片如何适应其显示区域，例如是否拉伸、裁剪或保持原比例
alignment	AlignmentGeometry   	图片在其显示区域内的对齐方式，如Alignment.center
repeat		ImageRepeat			当图片小于显示区域时，设置是否以及如何重复平铺图片



#### 19.滚动组件

组件					特点											使用场景
SingleChildScrollView	让单个子组件可以用滚动，所有内容一次性渲染		长表单、设置页、内容不固定但是总量不多的页面
Listview				线性列表，通过builder可以实现懒加载，性能优异		聊天记录、新闻、常见的单列滚动的数据列表
GridView				网格布局列表，支持懒加载，可以固定列数			图片墙、商品网格、应用图标列表
CustomScrollView		复杂布局方案，通过组合多个Sliver组件实现滚动		电商首页、社交App个人主页多个滚动紧密联动
PageYiew			整页滚动效果，支持横向和纵向					应用引导页、图片轮播图、书籍翻页



#### 20.组件通信

通信方式			  方向		     适用场景
构造函数传递		  父→子		     简单的数据传递
回调函数			  子→父                子组件通知父组件
InheritedWidget	  祖先→后代         跨层级数据共享
Provider			  任意组件间	     状态管理推荐方案
EventBus			  任意组件间         全局事件通信
Bloc/Riverpod		  任意组件间         复杂状态管理



#### 21.网络请求 Dio

trae中找到打开后里面有pubspec.yaml的文件目录地址

在trae终端输入命令 flutter pub add dio

(pub仓库 固定命令   flutter pub add xxx)

或者

在pubspec.yaml里无缩进输入

cupertino_icons: ^1.0.8

dio: ^5.11.0



基本使用: Dio().get(地址).then().catchError()

​					 ↑成功    ↑失败



#### 22.路由管理

构建多页面应用的核心 通过Navigator和Route来管理页面栈 实现页面跳转和返回

###### (1) 基本路由: 

​	无需提前注册路由 跳转时创建MaterialPageRoute实例即可

​	跳转新页面: Navigator.push(BuildContent content, Route route)

​	返回上一页: Navigator.pop(BuildContent content)

###### (2) 命名路由:

​	需要在MaterialApp中注册一个路由表(rootes)并设置initialRoute(首页)

###### (3) 传递参数:

​	用于页面间数据通信

​	命名路由传递参数:	Navigator.pushNamed(context, 地址, argumengs:{ 参数 })   参数一般map类型										

​		       接收参数: ModalRoute.of(context)?.settings.arguments

​		       接收时机: initState获取不到路由参数,放置在Future.microtask(异步微任务)中

​	基础路由传递参数:  组件构造函数传递参数(父传子)

​		      接收参数:  组件构造函数接收参数(父传子)

​		      接收时机:  initState可获取到基础路由的构造函数传参

###### (4) 动态路由与高级控制:

​	如果需要根据参数动态生成页面 或 实现路由拦截 onGeneerateRoute和onUnknownRoute

