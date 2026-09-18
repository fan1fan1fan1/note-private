## TypeScript前置

不要使用中文 特殊符号 空格名称(路径)



#### 1.下载Node.js



#### 2.npm安装typescript

WinR / PowerShell    输入 npm i -g typescript

本机最后的安装路径 D:\22820\node.js\node_global

查看检验方式 输入 tsc / npx tsc -v

 

#### 3.环境变量

找到ts.cmd路径 添加到path里



#### 4.创建ts文件     .ts



#### 5.编译

使用tsc对ts文件进行编译

​	ts -> 编译 -> js

​	在ts所在目录 cmd 执行   tsc xxx.ts  /  npx tsc 1.HelloTS.ts

​	生成一个js文件 即编译成功

​	

​	学习tsconfig后 直接在webstorm的终端内输入tsc也可编译





## TypeScript操作

#### 1.基本数据类型

let 

number  string  boolean  字面量  any  unknown  void  never  object  array  tuple  enum 



#### 2.编译模式

​	监视模式

​		webstorm终端中输入 tsc xxx.ts -w  /  npx tsc xxx.ts -w   

​		监视 + 实时应用: 不用手动编译 但只能作用于当前文件 如果同时运行两个文件 无法同步

​		ctrl + c 停止 退出



#### 3.编译选项

在tsconfig内写

​	include[ ]运行时包含路径 

​	exclude[ ]运行时不包含路径

​	 extends[ ] 

​	files[ ]  

​	compilerOptions{}

​		其中的内置选项:

​			项目选项: target 版本号

​					 lib 

​					module 

​					outDir 指定编译后文件所在的目录

​					outFile 将代码合并为一个文件

​					allowJs

​					checkJs 检查语法规范

​					removerComments 是否移除注释

​					noEmit 不生产编译后的文件

​					noEmitOnError 当有错误时不生成编译后的文件

​					strict 所有严格检查的总开关

​					alwaysStrict 设置编译后的文件是否使用严格规则

​					noImplicitAny 不允许隐式any

​					noImplicitThis 不允许不明确类型的this

​					strictNullChecks 严格检查空值



#### 4.webpack打包

​	看vite

​	npm init -y

​	cnpm i -D webpack webpack-cil typescript ts-loader clean-webpack-plugin 





## React Native (RN)

#### 1.介绍

混合开发

React的原生(Native)扩展

通过React语法开发ios和android



#### 2.安装node.js



#### 3.安装React Native脚手架

npm install -g react-native-cli



#### 4.其他必备

- `Android SDK`

- `Android SDK Platform`

- `Android Virtual Device`

  ​

#### 5.搭建安卓环境

- jdk(java)

- android stdio

- android skd

- 配置环境变量

  ​



#### 6.创建项目

初始化项目  		  npx @react-native-community/cli@latest init myproject

进入项目			  cd myproject

运行项目(android)     yarn react-native run-android



遇到的问题: 

##### (一)没找到java 

​	解决Java问题: 找到android stdio的jdr目录 添加系统变量 本机位置为: D:\22820\androidstudiojava\jbr

​		变量名: JAVA_HOME

​		变量值: D:\22820\android studio java\jbr

​	path中添加 %JAVA_HOME%\bin

​	检验是否添加成功 powershell输入 echo $env:JAVA_HOME

​								java -version



##### (二)没找到手机模拟器

(1)先打开 MuMu 模拟器，进入模拟器主界面

(2)管理员 PowerShell 执行

```
adb kill-server
```

```
adb start-server
```

(3)连接模拟器（优先 7555，失败就换 16384）

```
adb connect 127.0.0.1:7555
# 备选 adb connect 127.0.0.1:16384
```

(4)校验是否识别成功

```
adb devices
```

列表里出现 `127.0.0.1:7555  device` 就代表正常，可以执行 RN 启动命令

(5)重新启动项目 cd 项目 -> yarn xxxxx



##### (三)没有魔法

(1)打开项目里面这个文件： D:\myproject\android\gradle\wrapper\gradle-wrapper.properties

找到这一行：

```
distributionUrl=https\://services.gradle.org/distributions/gradle-9.4.1-bin.zip
```

把它替换成腾讯国内镜像：

```
distributionUrl=https\://mirrors.cloud.tencent.com/gradle/gradle-9.4.1-bin.zip
```

保存文件。

(2)再打开 D:\myproject\android\build.gradle

把 repositories google() mavenCentral()

改成

```
repositories {
    maven { url 'https://maven.aliyun.com/repository/public' }
    maven { url 'https://maven.aliyun.com/repository/google' }
    google()
    mavenCentral()
}
```

(3)重新启动项目 cd 项目 -> yarn xxxxx



##### (四)只能用jdk17



##### (五)找不到Android SDK路径



#### 7.调试操作

点击模拟器

快捷键 ctrl + m

点选debug

自动跳转浏览器



## 使用Expo创建RN项目

代码内容在App.js

#### 1.配置

node.js



#### 2.创建项目

cd 项目文件

npx create-expo-app@latest

y

expo-demo    (起一个项目名)



#### 3.进入项目

cd expo-demo

一定要是包含\package.json的目录下



#### 4.运行!!!!!!!!!!

npx expo start

生成二维码可以真机扫 确保同一个wifi 

需要本机有Expo go软件

扫描时选 在expo go中打开

也可以

打开二维码下方链接ip exp://..................



#### 5.学习时可以选用创建空白项目 

npx create-expo-app@latest --template black



#### 6.快捷键

运行后按键盘a可以打开模拟器

按键盘j打开调试窗口

输入?可以显示所有快捷键

按m可以打开模拟器菜单 真机菜单摇一摇手机



#### 7.文字必须写进Text



#### 8.样式 

写在

const styles: = StyleSheet.create({	

})

默认使用了flex布局

调整大小时不要写px 不写单位

后写的样式会把前面的样式覆盖掉 哪怕是同一行逗号后面



#### 9.Hook钩子

内置api

##### (1) useState状态管理

​	管理组件的局部状态

##### (2) useEffect

​	处理副作用(数据获取等)

##### (3) useReducer

​	统一管理复杂状态

##### (4) useContext

​	访问全局的Context数据



#### 10.使用map遍历并渲染数据



#### 11.运行真实接口

##### (1)进入文件夹目录 cd xxxx

##### (2)安装依赖包 npm i

##### (3)初始化数据库 客户端

​	npx prisma generate

##### (4)npm start

##### (5)接口文档 插件文档

​	https://clwy-app.apifox.cn/

##### (6) 如果跟安卓模拟器宽口冲突了

​	npx prisma studio 检测

​	npx prisma studio -p 5556   修改端口

##### (7)数据库



#### 12.发起网络请求

(1)验证端口项目是否启动成功

npm start

(2)const

(3)async await

​	如果需要局域网地址 终端输入 ipconfig 最后一组WLAN 10.148.105.177 就是 

​	代替 localhost

​	这个局域网地址可能每次重启电脑都变

(4) view输出



#### 13.useEffect自动运行

有运行时机 不停止就一直运行 创造时机方式:[ ]



#### 14.依赖项



#### 15.加载中 .... 组件

组件使用方法: (1) 在文档复制完整的需要插件的代码

​		        (2) 新建xxx.js 粘贴全部代码

​			(3) 引用进主项目文件中



#### 16.自定义网络错误组件



#### 17.useReducer统一管理状态



#### 18.useContext全局共享数据



#### 19.ScrollView组件



#### 20.FlatList组件

长文本



#### 21.路由 Expo Router

(1) cd D:/22820/Desktop/code/12.app/TSReact/expo-demo

(2) git所在目录 输入 
npx expo install expo-router react-native-safe-area-context react-native-screens expo-linking expo-constants expo-status-bar

y

(3) 打开项目的package.json

​	main部分 改成 expo-router/entry

(4) 在根目录新建app目录

(5) 新建 index.js

​	这个就是主项目文件 

(6) app.json中细节可以修改 



#### 22.Link组件

实现页面跳转



#### 23.布局文件、Stack(页面堆栈)、Slot(插槽)



#### 24.router方法 js跳转



#### 25.页面传递参数和动态路由



#### 26.Tapbar



#### 27.模态页Modal



#### 28.液态玻璃



#### 29.自定义Hook useLoadMore实现加载更多



#### 30.自定义组件 带进度条的WebView



#### 31.访问网页三种方式

##### (1) Linking

git:     npx expo install expo-linking

文件中导入 import * as Linking from 'expo-linking'

onPress={() => {

​	Linking.openURL("https://www.baidu.com");

}}



##### (2) WebBrowser

git:   npx expo install expo-web-browser

文件引入:   import * as WebBrowser from 'expo-web-browser'

onPress={() => {

​	await WebBrowser.openBrowserAsync("https://www.baidu.com");

}}



##### (3) WebView

git:  npx expo install react-native-webview

进入src/app/settings目录

新建一个url.js

import { useLocalSearchParams } from 'expo-router'
import ProgressWebView from '@/components/shared/ProgressWebView'
export default function Details(){ 
	const { uri } = uselocalSearchParams()
	return <ProgressWebView source={{ uri }} />

}



#### 32.expo-video视频播放器

git:  npx expo install expo-video



## 准备发布上架

#### 1.应用配置 app.json

前四个配置 依次是 应用名称 Expo项目的标识符 深层链接配置 版本号

深度链接:scheme     可以通过 xxxx://协议打开这个app

版本号     1.0.0   主版本号.次版本号.修订号



#### 2.ios、android加配置

"ios";{

​	"bundleIdentifer": "cn.xxx.app"

}

"android":{

​	"package": "cn.xxx.app"

}



#### 3.环境变量

在后面学习用EAS打包的时候，会自动读取.env文件里的环境变量。但是大家注意：不要将.env放在.gitignore or .easignore文件里排除
还有很多情况下，本地与发布上线的应用，环境变量不一样。
可以将.env，改名为.env.development，复制了再新建一个.env.production



本地与发布上线的应用环境变量不一样

可以将.env改名为.env.development

复制了再新建一个.env.production改为你的线上接口就行



#### 4.Expo BuildProperties配置

git:  npx expo install expo-build-properties

文件配置:

"plugins": [

​	[

​	"expo-build-properrties",

​	{

​		"android":{

​			"buildArchs":["arm64-v8a"],

​			"usesCleartextTraffic":true

​		}

​	}

​	]

]



#### 5.Figma

制作应用图标与启动屏



#### 6.Expo SplashScreen

应用图标与启动屏配置   app.json



#### 7.EAS注册与配置 eas.json

##### (1)Expo官方的EAS云打包

每个月可以免费打包15次



打开Expo官方网站(可能需要梯子)

安装EAS命令行   本地终端  

npm install -g eas-cli

输入eas login

eas build:configure

打开项目中生成的eas.json

production中添加

"production": {

​	"autoIncrement": true,

​	"android"L{

​		"buildType": "apk"

​	}

}

这样生成的就是.apk



代码提交git仓库(不必须)

eas build --platform android

回车

得到网址复制打开(不要关闭窗口)

n

下载apk

可以重命名



##### (2)EAS本地打包  macOS和Linux系统



##### (3)自己手动用Xcode和Android Studio手动打包



#### 8.注册开发者平台

苹果 一年688

安卓免费 但必须绑定公司 推荐小米的和应用宝的

小米开发者官网   https://dev.mi.com/xiaomihyperos



#### 9.App上架

(1)获取iOS Android的公钥和指纹信息

(2)备案

(3)申请软件著作与部署隐私政策网站

(4)安卓兼容性测试 与发布商店

