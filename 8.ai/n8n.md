1.开源自动化工作流软件 
	
	使用ai代替人工完成工作 适合执行重复的任务


2.工作流

	1.快速构建和部署 操作简单
	2.降低技术门槛 非专业人士也可参与过程 
	3.可视化 分享解释和维护


3.n8n用途

	1.聊天机器人
	2.客户关系管理CRM  整理信息 总结行程 销售流程自动化 分析需求等
	3.智能邮件助手 自动将邮件分类 并标注优先级 自动回复和日程安排
	4.内容生成 文案 帖子 广告语 新闻 视频
	5.数据分析


4.同类软件    

	Zapier     
	Make.com      
	n8n


5.使用n8n

	1.自托管 个人全面控制 自定义节点 自己部署服务器
		1.云托管于aws 谷歌云...  (可能收费)
		2.本机部署 没有公网IP webhook节点不能直接使用 需要保持开机状态
			docker desktop
			docker.com/products/docker-desktop
		
	2.官方云托管 简单
		

6.官网 n8n.io


7.配置方式 下载node.js


8.配置环境 

	新建文件夹
	node_global
	node_cache
	
	新建文本文档
	npm config set prefix "文件夹路径"
	npm config set cache "文件夹路径"

	打开命令提示符
	npm config set prefix "文件夹路径"
	npm config set cache "文件夹路径"
	
	检验是否配置成功
	npm config get prefix
	npm config get cache
	
	配置环境变量
	新建系统变量
	变量名  NODE_PATH
	变量值  node_global的路径\node_modules
	
	系统path中添加 %NODE_PATH%
	
	安装npm
	npm install express -g


9.安装n8n

	npm install -g n8n


10.全局启动n8n

	n8n start


11.npx n8n运行

	npx是Node.js自带工具 临时使用一条命令执行n8n
	npx检查本地是否有n8n可执行文件 没有则取npm库下载
	启动n8n 默认监听5678端口
	浏览器访问http://localhost:5678 进入n8n控制台 拖拽节点 搭建自动化工作流
	
	运行方式
	直接 npx n8n


12.节点

	触发结点
		1.点击触发 用于本地测试
		2.Schedule Trigger按照时间间隔自动定期触发
		3.Webhook当外部系统向这个专属URL发送HTTP请求时触发
		4.在线表单被用户提交时触发(填写一个表格触发)
		5.被另一个工作流调用时触发
		6.当接收到消息时触发(聊天机器人 通过对话与工作流方式)
		7.被外部应用的事件触发
		
	ai管理体
		1.在节点后面的加号 -> AI -> AI Agent
		2.记忆 对话窗口
		3.外部工具
		4.输出格式 output pahrser
			AI Agent -> require specific output format 
			-> 选取格式 提示词

	应用 谷歌全家桶 微软全家桶 社交媒体(YouTube Facebook Twitter等)
		AI动画(广告) 笔记 数据库 


13.自定义节点    http请求节点和API

	如果需要的节点不在右侧栏中 需要我们创建新的节点
	
	API 调取调用 后台程序系统 的功能和数据
	API请求 联系了前台需求和后台功能
	
	程序 根据API文档 发送API请求request 给后台系统
	后台系统 返回数据response 给程序     

	使用HTTP Request 完成这个过程
		共四个部分 URL method header body
		
		1.URL https://example.com:443/blog/article?id=123&lang=zh
			   协议    主机host     端口 路径         query parameters 
			        域名/ip地址                    查询参数
			        
		2.method  
			常用method:    GET(接收信息)  POST(发送信息)
			
		3.Header 
			提供更多请求的信息 
			
			eg. Accept:application/json
			意为提供需要的json格式的返回数据
			
		4.Body 
			请求体只存在于POST请求中 包含发送的信息
			
	通过上述自定义节点 http请求 我们可以使用API连接任何外部应用


14.webhook 反向http请求

	后台程序等待外部程序给我们发送信息 并发出回应给http


15.数据处理  json

	json  {"键":"值", " ":" "}
	用于传输数据:  API响应 n8n工作流中的节点数据
	
	json可嵌入  嵌套一个json
	
```
	{
	  "first_name" : "Tomas",
	  "location" : {
	    "city" : "Paris",
	    "country" : "France"
	  }
	}
```
	 
	 引用时 使用$
	 {{$json.first_name}} -> Tomas
	 {{$json.location.city}} -> Paris


16.数据处理 列表

	同类或不同类型对象的集合
	使用[]表示
	
	json中值可以是列表
```
	{ 
	   "cities" : ["los", "san", "diego"]
	}
```

	列表对象可以是json
```
	[
	  {
		 "city" : "Paris",
		 "country" : "France"
	  },
	  { 
		 "cities" : ["los", "san", "diego"]
	  }
	]
```
	此处整个列表称为items  其中每个json称为item


17.操作技巧

	拖拽
	叠加  {{$引用name}} is {{$引用number}} year ago


18.数据处理节点

	1.Merge  融合两个信息
		append        数据叠加 (复制)
		conbine       融合
		sql query     写成sql语言
		choose Branch 从两个数中选一个输出
		
	2.if
		相当于判断语句 选择输出结果 true输出 false不输出
		
	3.filter
		过滤器 在if语句条件下 直接滤走false数据 
		discarded中存放被过滤数据
		
	4.aggregrate
		聚合 把所有的数据聚合在一起 
		
		假设数据类型为json 经过聚合会变成一个json数据 
		类型为列表 存储所有信息
		相当于把一个items的多个item变成了一个item
	
	5.split out
		反向聚合 相当于打开这个item变成items








