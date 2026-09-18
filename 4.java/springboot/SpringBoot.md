# SpringBoot



## (一)MyBatis

http://mybatis.org

前身是iBatis 是Apache的一个开源项目

一种orm框架 java'实体类与sql语句之间建立的关系

与数据库有关 建立二维表



### 1.orm

Object Relational Mapping 

对象映射关系 字典

### 2.mybatis程序

#### 新建项目 

24版本: 把类型改成maven   java选21

依赖项: 

web: spring web

sql:MyBatis Framework     MySQL Driver

注意 MyBatis Framework 只支持 Spring Boot 版本 ≥4.0.0 并且 ＜4.1.0‑M1

#### pojo

类似类class文件



## (二)Spring

### 1.介绍

spring是面向Bean编程

Spring相当于一个大的容器 管理着各种不同职能的Bean

分为两大技术: 控制反转IOC    面向切面编程AOP

#### 控制反转IOC 

将对象的控制权从代码本身转到外部容器中 Spring容器

#### 面向切面编程AOP

方法增强的一种手段 



### 2.Spring项目

创建和mybatis相同

依赖只有 spring web





## (三)Spring MVC

### 1.介绍

Spring Web Mvc

表现层框架 是Spring的一部分

MVC:    Model              View                Controller      

​	     ↑ javaBean    ↑JSP/HTML       ↑Serlet



### 2.创建Spring MVC

创建项目 选择 maven   type选最后一个webapp



### 3.视图解析器



Mybatis：持久层框架，数据从程序持久化到 DB 中
Spring 框架：大的一个Bean管理容器，可以管理各种Bean。Controller.
SpringMVC： 表示层框架，请求的派发的。一个字符串请求可以映射到一个后台的一个
Controller，得益于前端控制器。



## (四)Spring Boot

### 1.介绍

是一个脚手架

用于快速搭建SpringBoot的web应用 用来简化Spring的初始搭建及开发过程



### 2.优点

快速构建一个独立的Spring应用程序；
嵌入web服务器: Tomcat、Jetty或者 Undertow，无须部署 WAR文件；
提供starter: POMs来简化Maven配置和减少版本冲突所带来的问题；
对Spring和第三方库提供默认配置（约定大于配置），也可修改默认值，简化框架配置；
无需配置XML--JavaConfig，无代码生成，开箱即用；



### 3.创建项目

springboot

maven

springboot可以选择一些低版本

依赖选: springweb、 mysql driver、 spring data JPA

安装插件SpringBoot