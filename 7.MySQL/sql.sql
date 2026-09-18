/* 数据库:
 	1.分类
 		非关系型数据库: 数据与数据间独立
 		非关系型数据库并没有统一存储结构标准，现常见结构有键值、文档、JSON类型等，对高性能需求设计
 	关系型数据库: 数据与数据间存在关系
 		数据按照类别进行存储，每个类别存储到一个容器（表）中，表和表之间可以建立关系，可以进行关联操作，性能相对一般


 	2.关系型数据库存储设计规则(E-R模型)
		遵循ER模型
			E(Entity)代表实体类别，关系型数据库中一类数据，对应数据库中的一张'表'存储
			R(Relationship)'表'和'表'可以维护某种'关系'，可以通过'关系'进行多表操做


	3.容器简述
		1.库 容器 最大的存储单位 里面有很多表
		2.表 类似java类 可以创建多个页
		3.行
		4.列 最小的存储单位


	4.数据库简述
		数据库管理系统 DataBase Management System  -> DBMS

		下载  https://dev.mysql.com/downloads/mysqlL


	5.图形用户界面(GUI)应用程序
	 	这类应用程序具有用户友好的图形界面，用户可以通过鼠标点击.拖放等方式与应用进行交互

	  命令行界面(CLI)或后台服务应用程序
		这类应用程序通常在后台默默运行，没有图形用户界面，用户通过在命令行或终
		端中输入文本命令与其进行交互。

		数据库属于命令行应用程序


	6.sql结构化查询语言简述
		SQL：Structure Query Lanquage。（结构化查询语言）
		SQL被美国国家标准局(ANSI)确定为关系型数据库语言的美国标准，后来被国际化标准组织(ISO)采纳为
		关系数据库语言的国际标准，可以使用SQL命令进行关系型数据库操作。

		指令 -> 数据库软件 -> 数据库

		SQL包括了所有对数据库的操作，主要是由数据定义、数据操纵、数据查询、数据控制、事务控制等SQL语言的使用规定组成。

		1.创建和修改盛放数据的容器（数据定义DDL）
		2.表中添加、修改、删除数据（数据操纵DML）		基础和重点
		3.表中数据多条件查询（数据查询DQL）

		4.事务启动、提交和回滚（事务控制TCL）			扩展和拔高
		5.账号创建、权限控制（数据控制DCL）


	7.终端使用sql操作
		1.cmd
		2.连接mysql服务指令 -> mysql -u你的用户名 -p你的密码
						   -> mysql -u 你的用户名 -p你的密码 -h端口号   (-h127.0.0.1 -P 3306)
						   -> mysql -u 你的用户名 -p你的密码 -h端口号 当前数据库名(mysql01)
				密码加密版: -> mysql -u 你的用户名 -p -h端口号
							  你的密码

			-u <username>：	用于指定你要连接的MySQL数据库的用户名。
			p<password>：	表示密码，后面紧跟着密码，中间没有空格。如果你不希望在命令行中显示密码，可以不指定密码，
						 	直接-p，然后在提示下手动输入密码。
			-h <hostname>：	用于指定 MySQL 服务器的主机名或者 IP 地址。如果 MySQL 在本地运行，可以用 localhost.
			-P <port>：		用于指定连接MySQL 服务器的端口号，默认情况下是3306。
			<database name>：是你要连接的数据库的名称。连接后会默认使用这个数据库。

			注释:  # 或 //(此处必须有个空格) 或 中间星号*

		3.输入指令
			select version();  当一个指令输入结束时 要有分号

		4.关闭exit
 */



/* 可视化工具语言
   1.mysql -uroot -p

   2.SHOW DATABASES;   查看有哪些数据库
     USE 数据库名;      使用某个数据库
     SHOW TABLES;      查看数据库里有哪些表
     exit              退出

   3.SQL语言四类：
   	数据定义DDL 库的创建 表的创建
    数据操纵DML 删除修改数据
    数据控制DCL 新增删除用户 密码修改 权限管理
    数据查询DQL 查询数据


   4.数据库定义语句DDL介绍
	数据定义语言(Data Definition Language)。
	DDL用于定义和管理数据库的结构，包括库、表、索引、视图等数据库对象的创建、修改和删除。
	DDL不涉及对数据的操作，而是关注数据库的结构和元数据（容器）。
	DDL关键字:	CREATE：用于创建数据库、表、索引、视图等。
				ALTER：用于修改数据库对象的结构，如修改表结构、添加列、删除列等。
				DROP：用于删除数据库对象，如删除表、删除索引等。


   5.ctrl shift +   字号变大

   6.sql内容字母大小写不敏感

   7.同一个数据库软件 不能有两个重名的数据库
     同一个数据库	 不能有两个重名的表
     同一个表         不能有两个重名的字段

   8. host='localhost',     # 主机名 ID地址
      port=3306,            # 端口 默认3306
      user='root',          # 账户名
      password='Fy051121.', # 密码
      autocommit=True       # 设置自动提交

   9.想控制mysql开启 停止
   	  net start MySQL
   	  net stop MySQL

   10.标识符命名规范（基于阿里巴巴规范手册）
        1. 注释应该清晰、简洁地解释SQL语句的意图、功能和影响。
        2.库、表、列名应该使用小写字母，并使用下划线()或驼峰命名法。
        3.库、表、字段名应该简洁明了，具有描述性，反映其所存储数据的含义，
        4.库名应于对应的程序名一致例如：程序名为EcommercePlatform数据库名命名为
        ecommerce_platform"
        5.表命名最好是遵循“业务名称_表”的作用 例如：alipay_task 、force_project、trade_config
        6.列名应遵循“表实体_属性”的作用例如：product_name或 productName
*/



/* 库管理：创建库DDL  (一)
	创建库，我们必须指定库名，可能指定字符集或者排序方式!
        方式1：如果当前库存在会报错
        CREATE DATABASE 数据库名;

        方式2：推荐
        CREATE DATABASE IF NOT EXISTS 数据库名；

        方式3：创建指定字符集库或者排序方式
        CREATE DATABASE 数据库名CHARACTER SET字符集；
        CREATE DATABASE 数据库名COLLATE 排序规则；

        方式4：创建指定字符集和排序规则库
        CREATE DATABASE 数据库名 CHARACTER SET 字符集 COLLATE 排序规则;

    字符集: 编码格式 utf-8 -> utf8mb4
    排序规则: 设定大小写是否敏感 utf8mb4_0900_ai_ci(不区分) 或 utf8mv4_0900_as_cs(区分)

	#查看默认字符集和排序方式命令
	SHOW VARIABLES LIKE 'character_set_database';
	SHOW VARIABLES LIKE 'collation_database';
*/
create database if not exists ms;
create database if not exists ms character set utf8mb4;
create database if not exists ms character set utf8mb4 collate utf8mb4_0900_as_cs;



/* 库管理 管理库  (二)
    查看和使用库，包括展示和切换库等命令
    方式1：查看当前所有库
    SHOW DATABASES；

    方式2：查看当前使用库
    SELECT DATABASE();

    方式3：查看指定库下所有表
    SHOW TABLES FROM 数据库名；；

    方式4：查看创建库的信息
    SHOW CREATE DATABASE 数据库名：

    方式5：切换库/选中库
    USE数据库名;

    注意：要操作表格和数据之前必须先说明是对哪个数据库进行操作，先use库
*/
use ms;
show databases;
select database();
show tables from ms;
show create database ms;



/* 管理库 修改库  (三)
    1.修改库编码字符集
        ALTER DATABASE 数据库名 CHARACTER SET 字符集；               #修改字符集abk utf8
        ALTER DATABASE 数据库名 COLLATE 排序方式；                   #修改排序方式
        ALTER DATABASE 数据库名 CHARACTER SET 字符集COLLATE排序方式； #修改字符集和排序方式
        注意：DATABASE不能改名。一些可视化工具可以改名，
             它是建新库，把所有表复制到新库，再删旧库完成的。(备份数据 删除旧库 创建新库 恢复数据)

    2.删除库
    删除数据库前要三思，是不是有刁民要害朕，确认好再删除，否则真要提桶跑路!!
        方式1：直接删除库
        DROP DATABASE 数据库名；
        方式2：判断并删除库（推荐）
        DROP DATABASE IF EXISTS 数据库名;
*/
alter database ms collate utf8mb4_0900_ai_ci;



# 表管理 创建表  (四)
/* 1.语法
    CREATE TABLE posts (
        post id INT AUO_INCREMENT PRIMARY KEY.
        title VARCHAR(255) NOT NULL COMMENT 'The title of the blog post',
        content TEXT NOT NULL COMMENT 'The content of the blog post',
        author id INT NOT NULL COMMENT 'The ID of the author of the post'
        created at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'The timestamp when the post was created'
        CONSTRAINT fk author FOREIGN KEY (author id) REFERENCES authors(author id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT 'Table storing blog posts';

   2.精炼写法
   create table 表名(
   create table if not exists 表名(
        列名 数据类型 [列可选约束类型] [comment '列注释描述'],
        列名 数据类型 同上,
        列名 数据类型 同上
   )[表可选约束] [comment '表注释描述']
*/



/* 数据类型 多种
    可包含有符号和无符号类: int,  unsigned int

    (1)int类: int smallint integer (标准)
             mediumint tinyint bigint (mysql方言)

                  smallint -32968 - 32767
       mysql方言： tinyint 1字节 无符号 0- 2/8-1 有符号 -2 7 / 2/7-1          -128 - 127
                  mediumint 3字节 无符号 0 - 2/24 -1 有符号 -2 23 / 2/23-1   -8388608 - 8388607
                  bigint 8字节 无符号 0- 2/64 -1 有符号 -2 63 / 2/63-1

    (2)浮点类: float(M,D)  M最多24,D最多8     M为所有位数和 D为小数点位数
              double(M,D) M最多53,D最多30

       eg. float(5,2) 这个范围内的最大值是999.99

    (3)定点数: decimal(M,D) 不失去精度 完全可以替代浮点数 M最多65,D最多30

    (4)字符串: char(M)    固定长度 可以不设定长度 如果声明8位 输入的字符少于8 剩余空间空格占有 M最多255
              varchar(M) 可变长度 必须给一个长度范围 相反 可伸缩实际长度

        插入值 CHAR(4) 所需存储 VARCHAR(4) 所需存储
         ' '    ' '    4bytes    ''      1byte
         'ab'   'ab'   4bytes   'ab'     3bytes
        'abcd' 'abcd'  4bytes  'abcd'    5bytes

    (5)文本类型: 可用于替代字符串 text
        tinytext    小文本
        text        文本 声明时不指定长度 不能超过规定的一行最大限制
        mediumtext  中等文本
        longtext    大文本

        开发经验：短文本，固定长度使用char 例如：性别，手机号
                短文本，非固定长度使用varchar 例如：姓名，地址
                大文本，建议存储到文本文件，使用varchar记录文件地址，不使用TEXT，直接存储大文本，他性能非常较差!

    (6)时间类型
        year        yyyy或yy            1901 - 2155 也可以只有后两位
        time        hh:mm:ss            -838:59:59 - 838:59:59
        date        yyyy-mm-dd          1000-01-01 - 9999-12-03
        datetime    yyyy-mm-dd hh:mm:ss 1000-01-01 00:00:00 - 9999-12-31 23:59:59
        timestamp   yyyy-mm-dd hh:mm:ss 1970-01-01 00:00:00 - 2038-01-19 03:14:07

        扩展：DATETIME和TIMESTAMP类型自动初始化和更新
            #方式1：插入默认当前时间和修改自动更新当前时间
            ts TIMESTAMP DEFAULT CURRENT_ TIMESTAMP ON UPDATE CURRENT TIMESTAMP.
            dt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

            #方式2：插入默认当前时间
            ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP.
            dt DATETIME DEFAULT CURRENT_TIMESTAMP

        注意情况
            1，时间类型就是一个特殊格式的字符串, 插入数据的时候 I!, 时间类型需要自动赋值, 需要手动添加相关的设置!
            2.扩展自动填写时间；
                1.插入默认添加时间
                datetime I timestamp default current timestamp
                2.修改默认更改时间（插入的默认时间）
                datetime I timestamp default current_timestamp
                on update current_timestamp;
            3.演示：创建t2表，
                注册日期 字段插入自动添加时间, 更新数据不变（插入数据的时候，自动维护时间, 后续修改数据, 时间不变!）
                更新日期 字段插入自动添加时间, 更新数据时间改变（插入数据需要自动维护时间, 修改数据也需要维护时间!）
*/
use ms;
show tables;  # 查看数据库中表

# 1.基本数据类型
create table t1(
    t1_age tinyint unsigned comment '年龄,无符号,范围0-255',
    t1_number bigint unsigned comment '学号,选最大的,无符号',
    t1_height float(5,2) unsigned comment '身高,选最小的,无符号浮点数 两位小数点 多的小数位四舍五入处理'
);

# 2.时间类
create table t2(
    register_time datetime default current_timestamp comment '插入自动维护时间',
    update_time datetime default current_timestamp on update current_timestamp comment '插入维护时间,修改数据自动更新'
);



/* 表管理 修改表 (五)
    修改表中列（字段）

    1.修改表，添加一列[可以指定X字段前或者后]
    ALTER TABLE 表名 ADD 字段名 字段类型[FIRSTIAFTER 字段名];

    2.修改表，修改列名
    ALTER TABLE 表名 CHANGE 原字段名 字段名 新字段类型 [FIRSTIAFTER 字段名];

    3.修改表，修改列类型
    ALTER TABLE 表名 MODIFY 字段名 新字段类型 [FIRSTIAFTER 字段名];

    4.修改表，删除一列
    ALTER TABLE表名 DROP 字段名；

    5.修改表名
    ALTER TABLE 表名RENAME [TO]新表名：

    删除表
    1.删除表
        DROP TABLE[IF EXISTS]数据表1[.数据表2,…数据表n];
    2.清空表数据
        TRUNCATE TABLE 表名;
        注意：删除表和清空表数据命令都是无法回滚的!动作不可以，执行之前需三思!
*/



/* 数据操纵语言 修改 DML   (六)
    数据操作语句(Data Manipulation Language)。
    DML用于数据库数据插入、删除、更新三种操作。
    DML不影响库表结构，但是会真正影响数据库数据。
    DML关键字: INSERT：用于数据插入关键字。 行是库最基本单位 插入根据行插入
              UPDATE：用于数据修改关键字。
              DELETE：用于数据删除关键字。

    1.插入 insert
        值的数量要等于表的所有列的数量 值的类型和顺序要一一对应

        情况1：为表的一行所有字段（列）插入数据
            INSERT INTO 表名 VALUES (value1, value2..);
            值列表中需要为表的每一个字段指定值，并且值的顺序必须和数据表中字段定义时的顺序相同。

        情况2：为表的一行指定字段（列）插入数据（推荐）
            INSERT INTO表名（列名1，列名2...…） VALUES（value1, value2.….）；
            值列表中需要为表名后指定的列指定值，并且值的顺序和类型必须和指定的列顺序相同。

        情况3：同时插入多条记录
            INSERT INTO 表名 VALUES (valuel, value2.….) ..... (value1, value2, .……);
            或者
            INSERT INTO 表名（列名1,列名2....…） VALUES （value1, value2.……）.… （valuel, value2.……）;

        情况1、情况2都可以转成一次插入多表数据，只需要在values后面写多个（值1, 值2...）即可，（）代表一行
        字符和日期型数据应包含在单引号中。

   2.修改 update
        情况1：修改表中所有行数据（全表修改）
            UPDATE table_name
            SET column1=value1, column2=value2. … , column=valuen
        更新表中所有行的指定列数据。

        情况2：修改表中符合条件行的数据（条件修改）
            UPDATE table_name
            SET column1=value1, column2=value2, … , column=valuen
            [WHERE condition]
        条件修改只是在后面添加where，where后面指定相关的条件即可。

    不添加where，代表修改一个表中的所有行的数据,反之，只修改符合where条件的
    如果修改多个列 set 列名=值，列名=值

    3.删除
        情况1：删除表中所有行数据（全表删除）
        DELETE FROM table_name;
        情况2：删除表中符合条件行的数据（条件删除）
        DELETE FROM table_name [WHERE condition]
 */
create database  if not exists dml_d1;
use dml_d1;
create table students(
    stu_id int comment '学号',
    stu_name varchar(100) comment '姓名',
    stu_age tinyint unsigned comment '年龄',
    stu_birthday date comment '生日',
    stu_height decimal(4,1) default  200 comment '身高,保留一位小数'
);

# 插入一名学生信息
insert into students values (1,'z',18,'1990-06-06', 185.5);
insert into students(stu_id, stu_name, stu_age, stu_birthday,stu_height) values (2,'4',18,'1990-06-01', 185.0);
# values如果不写会使用默认值
# 两名学生信息可以同时输入   (信息....),(信息....)

insert into students(stu_id, stu_name, stu_age, stu_birthday,stu_height)
values (6,'张三',21,'2002-05-10',175.5),
       (7,'李四',20,'2003-02-15',168.0),
       (8,'王五',22,'2001-09-20',180.2),
       (9,'赵六',19,'2004-03-08',165.8),
       (10,'钱七',23,'2000-12-01',172.3);

# 修改
update students set stu_name = '黄六' where stu_id = 8;

# 年龄小于20的 身高加2.0
update students set stu_height = stu_height + 2.0 where stu_age < 20;



# 大案例
drop table if exists list;
create table list(           # 创建表 list为表名
	id int,                  # 整数类型表
	name varchar(10),        # 文本 长度为数字 做长度最大限制 str
	age float                # 浮点数类型表
	#birth_date 重复,         # 日期类型
	#create_time timestamp   # 时间戳类型
);
# drop table list 删除表               drop table if exists list 删除表

# 1.插入INSERT 可以只插入一个元素 也可以全部插入
# insert into list(id) VALUES(1),(2),(3);
insert into list(id, name, age) VALUES(1, '小周', 31),(2, '小林', 26);

# 2.更新UPDATE
update list set name = '小陈' where id = 1;
# update list set age = 32;  危险操作

/* 3.删除DELETE
	delete from list where name = '小林';
	delete from list where age < 30;
	delete from list;  # 删除全部
*/



/* 查询表 DQL   (七)
    数据查询语句(Data Query Language)
    DQL用于查询数据库数据操作。
    DOL不影响库表结构，也不会影响原表的数据。
    DQL会基于原表数据查询出一个虚拟表。
    DQL关键字:  SELECT：用于查询数据的关键字。

    分为单表查询和多表查询
        单表: select语法,where条件,运算符号,单行多行函数,分组与排序等
        多表: select语法,where条件,运算符号,单行多行函数,分组与排序等,多表数据合并语法

    情况1：非表查询 简单运算
        SELECT 1;
        SELECT 9/2;
        SELECT VERSION:
    类似Java控制台输出，直接输出结果。

    情况2：指定表
        SELECT 列名1.列名2.列名3 FROM 表名；
        或者
        SELECT表名.列名，表名. FROM表名；
    指定表，查询表中的全部或者某些列。
    列和列之间使用[，] 分割，如果是全部列可以使用*替代
    * 代表获取表中所有字段

    情况3：查询列起别名
        SELECT 列名1 as别名，列名2.列名3 as别名FROM 表名；
        或者
        SELECT 列名1别名，列名2.列名3别名FROM 表名；
    查询列可以起别名，as 可以省略。
    起别名的意义主要是简化列名或者对应后期Java数据属性等
    如果别名想要区分大小写，可以添加双引号 例如："Name”

    情况4：去除重复行
        SELECT DISTINCT 列名[，列名，列名] FROM表名；
    完全重复 每个值都重复才会去重
    指定列值去重复行，可以指定单列或者多列，但是DISTINCT关键字只写一次且在前面。

    情况5：查询常数
        SELECT ‘尚硅谷' as corporation，列名，列名…FROM表名；
    SELECT 查询还可以对常数进行查询。就是在 SELECT 查询结果中增加固定的常数列。
    这列的取值是我们指定的，而不是从数据表中动态取出的。

    情况6: 显示表结构
        使用命令行查看表结构
        DESCRIBE employee;
        或
        DESC employees;

        在没有可视化工具场景下可以查看表结构。其中，各个字段的含义分别解释如下：
            Field：表示字段名称。
            Type：表示字段类型。
            Null：表示该列是否可以存储NULL值。
            Key：表示该列是否已编制索引。L
            PRI表示该列是表主键的一部分；
            UNI表示该列是UNIQUE索引的一部分；
            MUL表示在列中某个给定值允许出现多次。
            Default：表示该列是否有默认值，如果有，那么值是多少。
            Extra：表示可以获取的与给定列有关的附加信息，例如AUTO INCREMENT等

    情况7: 过滤数据 重要
        SELECT 字段1,字段2 FROM 表名
                                WHERE 过滤条件;
        先过滤where条件 返回符合的指定列

        解释：就是对表的行数据进行筛选，符合条件的行，在进行结果列的查询!
        语法：select 列信息 from 表信息 where [ 条件 and or xor 条件 and or xor 条件 ] true | false
        总结：from 作用 执行参照和查询的表
             where 作用 进行表中行的数据筛选
             select 作用 进行符合条件行的数据类的筛选
 */
# 使用select语句进行查询
select id, name from list;
select * from list;  # 查询全部快捷写法 有*的 *必须放前面

# 基础查询过滤
select id, name from list where age < 30;
select id, name, ifnull(age,0) from list where id = 1;

# ifnull(列,为null时给的默认值)



/* 运算符
   1.算术运算符
        %   *   +   -   /   DIV()整除
   2.比较运算符
        >   >=   <   <=   <>或!=不等于   =等于   <=>安全等于(方言)   is null(NULL值测试)
        is not null(NOT NULL值测试)   between...and(值是否在范围内)  not between...and
        in()值是否在一组值中    not in()值是否不在一组值中   like简单模式匹配   not like简单模式匹配否

        注意：比较运算符的结果为1、0、null    1代表true，0和null代表false
        操作适用于数字和字符串。根据需要，字符串会自动转换为数
        字，数字会自动转换为字符串，不需要考虑类型‘1'=1 为true

   3.逻辑运算符
        and &&     not !    or ||    xor逻辑异或
 */
select 100+1;
select 5%2;
select 1=0; # 0
select 1<=>1; # 1
select 'zap' <> 'zaap'; # 1
select 2 between 1 and 3;
select 2 in (0,3,5,7);
select 'aaa' like '%'; # % 表示任意字符串
select 'a' like '_'; # _表示一个字符 可叠加
select not 10; # 反转 0
select not 0; # 1



/* 函数
    单行函数和多行函数
    1.单行函数:
        (1.数值函数
                abs()  sign()返回数据符号正负数  pi()圆周率  ceil() ceiling()大于或等于的最小
                floor()小于或等于的最小  least()最小  greatest()最大  mod()余数
                rand()随机数 可以写参数 种子  round(x)四舍五入最接近的数 可以写参数y 小数点
                truncate(x,y)x截断为y位小数 sqrt()
        (2.字符串函数
                char_length() length() concat()拼接字符串 insert()替换 replace() upper() ucase()
                lower() lcase()  left() right() trim()去掉开始与结尾的空格 substr()取部分字符串
                find_in_set()返回子字符串出现位置 reverse()  nullif()比较两个字符串是否相等
        (3.时间函数
                返回当前时间: curdate() current_date() curtime() current_time() now() sysdate()
                            utc_date()  utc_time()
                year() month() day() hour() minute() second() monthname()月份  dayname()星期
                weekday()星期从0开始 quarter()季节 week() weekofyear()第几周  dayofyear()一年第几天
                dayofmonth()一个月第几天 dayofweek()星期从1开始
                date_add() add_date()差值时间  date_sub subdate()差值日期
        (4.流程函数 if() ifnull()
         (多行)  case
                    when condition1 then result1
                    when condition2 then result2
                    else default_result
                end [as alias_name]

                case expr
                    when value1 then result1
                    when value2 then result2
                end [as alias_name]
        (5.多行聚合函数
                AVG（列名）计算某一列的平均值（数值类型）
                SUM（列名）计算某一列的和（数值类型）
                MIN（列名）计算某一列的最小值（任意类型）
                MAX（列名）计算某一列的最大值（任意类型）
                COUNT（列名/ * /1）计算某一列或者行的记录数（任意类型）
           注意：聚合函数不能嵌套调用。比如不能出现类似“AVG(SUM(字段名称))”形式的调用。

    select语句 select关键字查询
        基本查询部分 select ...
                   from ...
                   where ... 多表的连接条件
                   and ...   不包含组函数的过滤条件
        高级处理部分 group by ...
                   having ... 包含组函数的过滤条件
                   order by ... asc/desc
                   limit ...
 */
select abs(-1);
select now();
select date_format(now(), '%Y年%m月%d日');
use dml_d1;
select avg(stu_age),min(stu_id),sum(stu_height) from students;


/*
 group by关键字 分组聚合
   聚合函数:
 	sum() 求和
 	avg() 求平均值
 	min() 求最小值
 	max() 求最大值
 	count() 求数量
*/
#select id, avg(age),count(age) from list group by list.id


# order by 对查询结果排序  asc升序   desc降序
select * from list order by age;  # 按年龄
#select * from list order by age > 31 order by id desc; # 按id


# 结果分页设置和数量显示 limit
select * from list limit 2, 1;    # 结果限制 从第2条开始取，只输出1条



/* 查询高级处理
   1.分组查询
        select 分组列,分组列,聚合函数                    -> 一个二维表 分组列 分开后有部分聚合 最后查找某些特性输出
        from table
        [where condition]
        [group by 分组列,分组列...having分组后条件]
   2.排序
        select 列,列,函数
        from table
        [where condition]
        [group by 排序列 asc|desc,排序列 asc|desc]
        asc表示正序 desc表示倒序
        只有第一列完全相同 第二列才会生效
   3.切割查询(mysql方言)
        分页查询 将结果分页 一段一段展示
        select 列,列,函数
        from table
        [where condition]
        [limit[位置偏移量], 行数]    limit必须放最后

        查询页数公式  limit(page-1)*size,size;

 */
select stu_id,count(*) from students group by stu_id;
select stu_id,count(*),avg(stu_height) from students group by stu_id having avg(stu_height>185.0);

select * from students order by stu_id desc;


/* select关键字查询总结
    基本查询部分 select ...
               from ...
               where ... 多表的连接条件
               and ...   不包含组函数的过滤条件
    高级处理部分 group by ...
               having ... 包含组函数的过滤条件
               order by ... asc/desc
               limit ...

    1.顺序不能换
        书写顺序 select 列名 from 表 where 条件 and|or 条件 group by 分组字段 having 分组后又条件
                            order by 排序规则参照 asc|desc limit offset,number;
        执行顺序 from ... where ... group by ... having ... select ... order by ... limit ...
                   数据源   筛选前置条件      分组   分组后的数据过滤  select显示列信息(排序 切割)

    2.where后面不能使用select产生的列 因为这时候没有列生成
    2.having和group by后可以使用select产生的列
 */



/* 数据库约束
    限制语法
    分类: 1.域级约束(列级约束)
            非空约束：NOT NULL，列非空约束!
            默认值约束：DEFAULT，某列默认值!
            检查约束：CHECK，检查约束!
         2.实体级约束(行级约束)
            主键约束：PRIMARY KEY，主键唯一且不为空约束!
            唯一约束：UNIQUE，限制某一列值表中唯一!
            自增长约束：AUTO INCREMENT，数字类型字段插入数据自增长约束!
         3.引用级约束(多表约束)
            参照（外键）约束：FOREIGN KEY，限定表中某一列，正确引用其他表的数据值!
    添加时机：创建表时直接添加(CREATE TABLE)
            创建表之后，通过ALTER TABLE语句添加

    非空约束
        作用: 限制某个字段/列的值不允许为空
        关键字: NOT NULL
        特点: 默认：所有类型列默认都可以为null，包括数字类型。
             列上添加：非空约束只能添加到列上!
             多次使用：一个表中可以有很多列进行非空限定!
             空值判定：空字符串不是null，0也不是null!
        添加
            建表时添加
                CREATE TABLE 表名称(
                    字段名 数据类型
                    字段名 数据类型 NOT NULL.
                    字段名 数据类型NOT NULL
                );
            建表后修改
                alter table 表名称modify字段名 数据类型not null;
        删除
            alter table 表名称modify字段名 数据类型NULL；
            或
            alter table 表名称modify字段名 数据类型：
            #不加默认允许为null，
 */
create table emp1(
    e_name varchar(20) not null,
    e_age int
);
desc emp1;
alter table emp1 modify e_age int not null;


/* 默认值约束
   作用: 限定某个字段/某列的添加默认值
   关键字: default
   特点: 位置约定：默认值约束不能添加到唯一或者主键上，其他列都可以。
        生效时机：当插入数据时，没有显示赋值，赋予默认值!
        细节特点：添加约束时，default默认值，默认值对应正确数据类型!
    添加
        建表时添加
            create table 表名称(
                字段名 数据类型 default 默认值，
                字段名 数据类型 not null default默认值
            )；
        建表后修改
            alter table 表名称 modify 字段名 数据类型default 默认值;
            #如果这个字段原来有非空约束，你还保留非空约束，那么在加默认
            值约束时，还得保留非空约束，否则非空约束就被删除了
            alter table 表名称 modify 字段名 数据类型default 默认值 not null;
    删除
        alter table 表名称modify字段名 数据类型；
        #删除默认值约束，也不保留非空约束
        alter table 表名称modify字段名 数据类型 not null;
        #删除默认值约束，保留非空约束
 */
create table emp2(
    name varchar(20) default '二狗子',
    age int not null
);
desc emp2;
alter table emp2 modify age int default 18 not null;
insert into emp2 (name) values ('张三');
alter table emp2 modify name varchar(20);

/* 检查约束
    作用: 检查某个字段的值是否符合xx要求,一般是值的范围
    关键字: check(限制表达式)
    特点: 新特性：5.7版本不支持check约束，8+版本才支持check约束。
         万能约束：check（表达式），可以自定义表达式，变成任何约束!
         不推荐：不推荐使用check约束，进行数据检查，建议程序级限制!
    添加
        建表时添加
            create table 表名称(
                字段名 数据类型，
                check（表达式），#check约束属于表级别， 不用添加到列后
                字段名 数据类型 not null default默认值
            )：
        建表后修改
            alter table 表名 add constraint约束名CHECK（表达式）：
            #约束名不能重复
    删除
        alter table 表名drop constraint约束名；
 */
create database  if not exists dml_d1;
use dml_d1;                                                    # 使用数据库
create table emp3(                                              # 创建表
    gender char,
    check(gender in ('男','女')),
    age int
);
alter table emp3 add constraint age_ck check (age > 18);        # 赋值
desc emp3;                                                      # 展示
select *                                                        # 查约束名字 执行一下 结果就是约束名
from information_schema.table_constraints
where table_schema = 'dml_d1'
and table_name = 'emp3';
#alter table emp3 drop constraint emp3_chk_1;                    # 删除 需要约束名字


/* 主键约束
    主键: 在任何情况下，确保表中的行数据少有一列是不重复的!避免整行数据的不重复!那么永远不重复，且不会为null的
          列，我们就可以称作：主键列（主键）例如：学生的学号、员工的编号、以及我们的身份证号等等
    主键分类: 1.自定义主键：人为创建一列，专门用来做主键，它的使命就是保证行数据不重复!例如：学号，身份证号等等
             2.自然主键：不是人为创建的列，数据实体自带的属性列，当前环境下，此属性列唯一且不为空，可以做主键，
                      但是它有两个使命：第一，承担实体属性值 第二，作为表的主键列!例如：DNA序列等等
    主键特点: 主键数量：每个表中只能有一个主键。
             单一和复合：主键可以由单个列或者多个列构成（复合主键）。
             主键列类型：可以是任意类型，只要唯一早不重复即可。唯一且不为null
             主键命名：主键一般采用identify （标识）单词缩写 xxid xx id等，但没有强制要求。
             主键索引：创建主键约束时，系统默认会在所在的列或列组合上建立对应的主键索引（能够根据主键查询的，就
                     根据主键查询效率更高）。如果删除主键约束了，主键约束对应的索引就自动删除，
                     主键索引固定命令：PRIMARY。
    主键约束: 根据主键样式约束
    添加
        建表时添加
            create table 表名称(
                字段名 数据类型 primary key，#列级模式
            );
            create table表名称(
                字段名 数据类型，
                [constraint 约束名] primary key（字段名）#表级模式
            );
        建表后修改
            ALTER TABLE表名称 ADD PRIMARY KEY（字段列表）；
            #字段列表可以是一个字段，也可以是多个字段
    删除
        删除主键约束，不需要指定主键名，因为一个表只有一个主键，删除主键约束后，非空还存在，唯一消失。
        #删除主键约束和索引
        alter table 表名称 drop primary key;
 */
create table emp8(
    e_id int primary key,
    primary key (e_id)
);
alter table emp8 drop primary key;


/* 唯一约束
   作用: 限定某个字段或组合字段,在表中数据唯一
   关键字: unique
   特点: 约束数量：同一个表可以有多个唯一约束。
        空值处理：唯一性约束允许列值为空。
        约束名称：在创建唯一约束的时候，如果不给唯一约束命名，就默认和列名相同。
    添加
        建表时添加
            create table 表名称(
            字段名 数据类型 unique,
            字段名 数据类型 unique key);
            create table 表名称(
            字段名 数据类型
            [constraint 约束名] unique key（字段名））
        建表后修改
            ALTER TABLE table_name
            ADD CONSTRAINT constraint_name UNIQUE（列名，列名）；
    删除
        #查看约束
        SELECT *
        FROM INFORMATION SCHEMA.TABLE_CONSTRAINTS
        WHERE TABLE_SCHEMA='库名'
        AND TABLE_NAME=‘表名；
        # 删除约束
        ALTER TABLE table_name
        DROP CONSTRAINT constraint_name;
 */
create table emp5(
    phone varchar(11) unique key,
    unique key(phone)
);

/* 自增长约束
   作用: 限定某个整数,插入数据不显示维护,值自动增长
   关键字: auto_increment
   特点: 添加位置：只能添加到键列（主键，唯一），普通列不可以。
        约束数量：每一张表只能有一个自增长约束。一般都是主键
        数据类型：增加自增长约束的列必须是整数类型。
        特殊情况：如果给自增长字段设置O或者null，列数据会自增长赋值，如果设置的
        是非零和非空数据，那么将真实设置值!
    添加
        建表时添加
            create table 表名称(
            字段名 数据类型 primary key auto_increment
            );
            create table 表名称(
            字段名 数据类型 unique key auto_increment，
            );
        建表后修改
            alter table 表名称modify字段名 数据类auto_increment;
    删除
        #alter table 表名称modify字段名 数据类型 auto_increment;
        #给这个字段增加自增约束
        alter table 表名称modify字段名 数据类型；
        #去掉auto_increment相当于删除
 */
create table emp9(
    e_id int primary key auto_increment,
    e_name varchar(10)
);
desc emp9;
insert into emp9 (e_name) values ('ergouzi'),('驴蛋蛋');
alter table emp9 modify e_name varchar(10) auto_increment;

/* 参照约束 外键约束
    添加
        建表时添加
            create table 主表名称(
                字段1 数据类型 primary key
            );
            #子表中添加主外键约束
            create table子表名称(
                字段1 数据类型 primary key.
                [CONSTRAINT<外键约束名称>] FOREIGN KEY (外键)references 主表名(主键) [on update xx][on delete xx]
            );
        建表后修改
            alter table 从表名 add [CONSTRAINT 约束名]FOREIGN
            KEY（从表的字段） references主表名（被引用字段）[on
            update xx][on delete xx];
    删除
        (1)第一步先查看约束名和删除外键约束
        SELECT *FROM information_schema.table_constraints WHERE table_nam
        ‘表名称';#查看某个表的约束名
        ALTER TABLE 从表名 DROP FOREIGN KEY 外键约束名;
        (2)第二步查看索引名和删除索引。(注意，只能手动删除)
        SHOW INDEX FROM表名称；#查看某个表的索引名
        ALTER TABLE 从表名DROP INDEX索引名；

    [on update xx][on delete xx]区域约束 连坐
    约束等级设计
        Cascade     在父表上update/delete记录时，同步update/delete子表的匹配记录!
        Set null    在父表上update/delete记录时，将子表上匹配记录的列设为null，但是要注意子表的外键列不能为not null!
        No action   如果子表中有匹配的记录，则不允许对父表对应候选键进行update/delete操作!
        Restrict    【默认】同no action，都是立即检查外键约束!
        Set default 父表有变更时，子表将外键列设置成一个默认的值，但Innodb不能识别!
        最好是采用：ON UPDATE CASCADE ON DELETE RESTRICT的方式。

    示例：当主表中的行被删除或更新时，从表中的相关行也会被相应地删除或更新。
        ALTER TABLE 从表名 ADD CONSTRAINT外键约束名
        FOREIGN KEY （从表外键列） REFERENCES 主表名（主表主键列）
        ON DELETE CASCADE
        ON UPDATE CASCADE;
 */
select *
from information_schema.TABLE_CONSTRAINTS
where TABLE_SCHEMA = 'dml_d1'
and TABLE_NAME = '';

create table emp10(
    sid int primary key auto_increment,
    sname varchar(20),
    constraint s_s_1_kf foreign key (sname) references students(stu_name)
);

create table emp11(
    sid int primary key auto_increment,
    sname varchar(20)
);
alter table emp11 add constraint s_s_2_kf foreign key (sname) references emp10(sname);
alter table emp11 drop foreign key s_s_2_kf;
show index from emp10;
#alter table emp10 drop index s_s_1_kf;



/* 数据库多表关系
    多(两两之间)     表(数据)
    通过主外键建立的关联
    1.一对一
        外键一定是唯一的
        处理一张表的冷热数据 冷数据放在一个表 热数据放在一个表 形成一对一关系
        两个表之间的每行数据都是唯一的对应关系!
        例如，一个员工与其唯一的员工档案。
    2.一对多
        解决冗余问题
        一个表关联另一个表多行数据，反方向只关联一行数据!
        例如，一个作者与多个文章的关系。
    3.多对多
        额外创建一个中间表 靠中间表维护
        两个表中的记录都可以与对方表中的多个记录相关联!
        例如，学生和课程之间的关系，一个学生可以选修多门课程，而一门课程也可以由多个学生选修。
 */

# 一对一维护:
#主表：员工表
CREATE TABLE emp(
    e_id int primary key auto_increment,
    e_name varchar(20) NOT NULL,
    e_age int default 18,
    e_gender char default'男'
);
#子表：档案表1（正常存在外键 外键唯一unique）
CREATE TABLE profile1(
    p_id int primary key auto_increment,
    p_address varchar(100)NOT NULL,
    p_level int default 10,
    e_id int unique,#外键唯一
    CONSTRAINT s_p_1 FOREIGN KEY(e_id)
    references emp(e_id)
);
#子表：档案表2（外键直接当主键 共用主键）
    CREATE TABLE profile2(
    e_id int primary key auto_increment,
    p_address varchar(100) NOT NULL,
    p_level int default 10,
    CONSTRAINT s_p_2 FOREIGN KEY
    (e_id) references emp(e_id)
);

# 一对多维护:
#主表：作者表
CREATE TABLE author(
    a_id int primary key auto_increment,
    a_name varchar(20) NOT NULL,
    a_age int default 18,
    a_gender char default'男'
);
#子表：文章表（外键）
CREATE TABLE blog(
    b_id int primary key auto_increment,
    b_title varchar(100) NOT NULL,
    b_content varchar(600)NOT NULL,
    a_id int, #外键
    CONSTRAINT a_b_fk FOREIGN KEY(a_id)
    references author(a_id)
);

#多对多维护:
#主表：学生表
CREATE TABLE student(
    s_id int primary key auto_increment,
    s_name varchar(20) NOT NULL,
    s_age int default 18
);
#中间表：student_course
CREATE TABLE student_course(
    sc_id int primary key auto_increment,
    s_id int,
    c_id int,
    FOREIGN KEY(s_id) references student(s_id),
    FOREIGN KEY(c_id) references course(c_id)
);
#主表：课程表
CREATE TABLE course(
    c_id int primary key auto_increment,
    C_name varchar(10) NOT NULL,
    c_teacher varchar(10)
);



/* DQL 数据库多表查询语言
    前边学的DQL单表查询语法 + 多表数据合并语法

    多表数据合并语法: 水平合并语法 + 垂直合并语法 + 子查询语法

    垂直合并语法: union(有去重效果) / union all(全部合并)    (div)
                将多个表的结果汇总 不要求主外键
        细节：实现要求：只要求合并的结果集之间的列数和对应列的类型相同即可
             主外键要求：union只是结果集垂直汇总，不涉及行数据水平连接，不要求有主外键
             重复数据认定：一行中的所有列值都相同，认定为重复行

    水平合并语法: 连接查询 更重要      (span)
                将多个表的结果水平整 要求一定得有关系 有主外键
            语法：内连接 外连接(常用) 自然连接
            细节：核心要求：水平连接是行和行数据连接，要求两个表必须有关系（主外键）
                 正确连接：为了正确的将行数据之间连接，水平连接需要额外判定主外键相等
                 拆表产物：因为关系型数据库特点，数据进行拆表存储，所以水平连接语法非常重要
                 语法理解：别看水平连接有多种语法，但是基本大同小异，只要理解内外区别即可

    子查询语法: 在sql语句中嵌套另一个完整的select查询语句 称为子查询 内部查询
            标量查询：子查询返回单行单列，这个值通常用于条件判断、过滤或者作为SELECT查询的一部分
            行子查询：子查询返回一行多列，通常用于更新或插入数据，或者作为一个整体来比较。
            列子查询：子查询返回一列多行，通常用于IN、ANY、ALL等条件中，或者作为其他查询的条件。
            表子查询：子查询返回多行多列，通常不能用于查询条件，用于连接或联合查询中的虚拟表。
 */
create table a(
    aid int,
    aname varchar(20),
    ajob varchar(20)
);
create table b(
    bid int,
    bname varchar(20),
    bjob varchar(20)
);
insert into a values(1,'aaa','zzz'),(2,'bbb','fff'),(3,'ccc','nnn');
insert into b values(4,'aaa', 'sss'),(5,'bbb','mmm'),(6,'ccc','lll');

# 去重合并
select aid,aname from a union select bid,bname from b;

# 不去重合并
select aid,aname from a
union all
select bid,bname from b;



/* 水平合并 内连接查询语法
    select * from 表1 [inner] join 表2 on 表1.主键 = 表2.外键 (标准)
    select * from 表1,表2 where 表1.主键 = 表2.外键   (非标准 mysql方言)

    连接查询必须添加主外键相等条件 为了避免添加错误数据
    多表查询考虑不同表存在相同字段名的问题:
        我们在处理列名相同字段时 使用了起别名的方法 name as sname  id as sid
                              或者提示表的名字 表名.列名
        此处如果与遇到了相同表名 可以使用同样的方法 from 表 别名    |    from as 别名
 */
select a.aid, b.bid from a inner join b on a.aid = b.bid;
select a.aid, b.bid from a,b where a.aid = b.bid;
select a.aid, b.bid from a inner join b on a.aid = b.bid where a.aid>1;
select a.aid, b.bid from a,b where a.aid = b.bid and a.aid>1;

# 3+合并
create table c(
    cid int,
    cname varchar(20),
    cjob varchar(20)
);
insert into c values(7,'aaa','zzz'),(8,'bbb','fff'),(9,'ccc','nnn');

select a.aid, b.bid, c.cjob
from a inner join b on a.aid = b.bid
inner join c on c.cjob = a.ajob
where a.aid>2;

select a.aid, b.bid, c.cjob
from a,b,c where a.aid = b.bid and c.cjob = a.ajob and a.aid>2;



/* 水平合并 外连接查询语法
    select * from 表1 left [outer] join 表2 on 表1.主键 = 表2.外键    左外
    select * from 表1 right [outer] join 表2 on 表1.主键 = 表2.外键   右外

    外连接会返回所有符合条件的行 同时返回为匹配的行
    分为左外连接 右外连接 指定其中一个表为主表
    必须添加主外键相等
    外连接的连续性 from 逻辑主表 left join 表2 on 主=外 left join 表3 on 主=外 left join ...
 */
select * from a left join b on a.aid = b.bid;
select a.aid, b.bid, ifnull(a.aname, '空') from a left join b on a.aid = b.bid where a.aid>2;



/* 自然连接语法
    内外连接升级版
    但是也值得注意，除了主外键其他列名相同，它也会自动判定相等!稍显不靠谱!

    语法： SELECT * FROM emp NATURAL JOIN dept；      #自然内连接
          SELECT * FROM emp NATURAL LEFT JOIN dept; #自然左外连接
          SELECT * FROM emp NATURAL RIGHT JOIN dept;#自然右外连接

    细节1：自然连接就是内和外连接语法升级版本
        自然连接可以变成内连接或者外连接，会自动查找相同的列判定相等!
        使用自然连接要求：主外键命名要相同，除了主外键命名要不同!
    细节2：自然连接可以指定判定哪些列
        例如：employees e JOIN departments d USING (department_id);
        使用USING指定数据表里的同名字段进行等值连接。
        因为其繁琐性，不是很推荐使用!
 */



/* 自连接
    不是连接形式 只是特殊语法
    eg. 通过一列信息查同一列其他人信息   员工编号->领导编号 本身是同一列信息 查找
 */
select a.aid,b.bid from a left join b on a.aid = b.bid where a.aid = 2;



/*子查询 标量子查询 行子查询 列子查询 表子查询
  嵌套子查询
  同表查询
  update(先查询 再更新)
  delete(先查询 再删除)
  insert(先查询 再插入)
 */
select a.aid from a where a.aid > (select b.bid from b);

# 标量子查询(单行单列)
select * from a where aid > (select max(bid) from b);
# 行子查询(单行多列)
select * from a where (aid, aname) = (select bid, bname from b where bid=1);
# 列子查询(多行单列)
select * from a where aid in (select bid from b);
# 表子查询(多行多列)
# ()内语句执行完查询出一个子表 临时标记为tmp
select * from a
join (select aid, count(*) from a group by aid) tmp
on a.aid = tmp.aid;


# update 嵌套子查询
select a.aid from a where a.aname = 'aaa';
update b set b.bid = (select aid from a where a.aname = 'aaa') where b.bid is null;

# 同表查询
select a.aid from a where a.aname='aaa';
update a set a.aname = (select a.aname from a where a.aid='aaa') where a.aid='bbb'; # 执行失败
update a set a.aname = (select a.aname from (select a.aname from a where a.aid='aaa') as tmp) where a.aid='bbb';
# 将内层子查询 再嵌套一层子查询 释放原有表的引用


# delete
select a.aid from a where a.aname = 'ccc';
delete from a where a.aid = (select a.aid from a where a.aname = 'ccc');


# insert
create table employee like a; # 只是复制表结构 表头
insert into employee (select * from a);

# 更快捷
create table employer as (select * from b);



/* 数据库事务
    数据库事务(transaction)是一套操作数据命令的有序集合，一个不可分割的工作单位。
    事务中单个命令不会立即改变数据库数据，当内部全部命令执行成功，统一更新数据，当有命令失败，可以进行状态回滚。
    事务由事务开始与事务结束之间执行的全部数据库操作组成。

    事务作用: 1.为数据库操作序列提供了一个从失败中恢复到正常状态的方法
             2.当多个应用程序在并发访问数据库时，以防止彼此的操作互相干扰
    事务ACID特性
        原子性(Automicity)  原子性是指事务是一个不可分割的工作单位，事务中的操作要么都发生，要么都不发生。
        一致性(Consistency) 事务内部的操作的状态前后一致，成功都成功，失败都失败，避免部分成功出现错误数据。
        隔离性(Isolation)   事务的隔离性是指一个事务的执行不能被其他事务干扰，即一个事务内部的操作及使用的数据
                           对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
        持久性(Durability)  持久性是指一个事务一旦被提交，它对数据库中数据的改变就是永久性的，接下来的其他操作
                           和数据库故障不应该对其有任何影响

    事务的开启、提交、回滚
        MySQL默认情况下是自动提交事务。
        默认每一条语句都是一个独立的事务，一旦成功就提交了。语句报错失败就回滚。
        我们的目标：将多条语句加入到一个事务中
        方案1：手动提交模式
            #开启手动提交事务模式（取消自动提交事务）
            set autocommit = false;或 set autocommit =0;
            #上面语句执行之后，它之后的所有sql，都需要手动提交才能生效，直到恢复自动提交模式
            #恢复自动提交模式
            set autocommit = true; 或 set autocommit = 1;
            #查看是否自动提交
            show variables like 'autocommit';
 */
set autocommit = false;   # 设置当前连接为手动提交模式
update a set aname='aaa' where aid = 1;
commit;   # 提交
# rollback; 回家


/* 方案2：自动提交模式下开启独立事务
    #也可以在自动提交模式下，开启一个事务。
    start transaction;
    #添加多个sql命令
    #最后可以提交或者回滚
    commit;或 rollback;
 */
start transaction;      #开始事务
update a set aname='aaa' where aid = 1;
#下面没有写commit;那么上面这句update语句没有正式生效。
commit;   # 提交
# rollback; 回滚



/* 注意事项
    MySQL默认情况下是自动提交事务。
    每一条语句都是一个独立的事务，一旦成功就提交了。一条语句失败，单独一条语句不生效，其他语句
    是生效的。
    我们的目标：将多条语句加入到一个事务中

    方案3：DDL语句不支持事务（注意注意）
        #说明：DDL不支持事务
        #DDL：create,drop，alter等创建库、创建表、删除库、删除表、修改库、修改表结构等这
        些语句不支持事务。
        #换句话只对insert.update.delete语句支持事务。
        TRUNCATE表名称；清空整个表的数据，不支持事务。把表drop掉，新建一张表。
 */
START TRANSACTION;
TRUNCATE a;
ROLLBACK; # 回滚 无效


/* 事务隔离性
    一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
    隔离级别            概述                    脏读  不可重复读  幻读
    read-uncommitted   读未提交事务数据          是     是        是
    read-committed     读已提交事务数据(oracle)  否     是        是
    repeatable-read    可重复度(mysql)          否     否        是（小概率）
    serializable       串行化和序列化            否     否        否

    数据库事务的隔离性：一个事务与其他事务隔离的程度称为隔离级别。数据库规定了多种事务隔离级别，
    不同隔离级别对应不同的干扰程度，隔离级别越高，数据一致性就越好，但并发性能越弱。
        脏读：一个事务读取了另一个事务未提交数据；
        不可重复读：一个事务读取了另一个事务提交的修改数据。
        幻读：一个事务读取了另一个事务提交的新增、删除的记录情况，记录数不一样，像是出现幻觉。

    #修改隔离级别：  set transaction isolation='隔离级别；
    #查看隔离级别：  select @@transaction_isolation;
 */



/* 数据备份和还原
   备份
    不是代码 是终端指令 要在mysql未连接的时候执行

    1.备份 单库单表
        mysqldump -u用户名 -p密码 库名 表名 > backup.sql备份文件库
    2.备份单库多表
        mysqldump -u用户名 -p密码 库名 表名1,表名2,表名... > backup.sql备份文件库
    3.备份单库全部表
        mysqldump -u用户名 -p密码 库名 > backup.sql备份文件库

    还原
        binlog日志   C:\ProgramData\MySQL\MySQL Server 8.0\my.ini
                                                          \Data中带长数字号的 记录了对数据库的所有指令操作

        具体恢复操作: #1. 清空原有的日志文件
                    RESET MASTER;                                            清空日志

                    #2.准备数据, 插入数据 -> 000001日志文件
                    CREATE DATABASE test08_binlog;                           新建库
                    USE test08_binlog;                                       使用binlog
                    CREATE TABLE table_01(                                   新建表
                        id INT PRIMARY KEY AUTO INCREMENT.
                        NAME VARCHAR(20)NOT NULL
                    INSERT INTO table_01(NAME) VALUES('二狗子').(‘驴蛋蛋');    执行指令

                    #3.重启一个新的日志文件->000002日志文件                      创建新日志
                    FLUSH LOGS;

                    #4. 将删除数据和插入数据植入第二个日志文件 -> 000002日志文件    植入刚刚对新库的操作日志内容
                    DELETE FROM table_01 WHERE id = 2; #删除驴蛋蛋
                    INSERT INTO table_01(NAME)VALUES(‘狗剩子')；
                    SELECT * FROM table_01;

        查看binlog内容 日志文件清单
            #1.查看日志文件清单
            SHOW BINARY LOGS,

            #结果
            Log_name         File_size Encrypted
            my_logbin.000001 1023      No
            my_logbin.000002 787       No

            #2.查看日志文件信息
            SHOW BINLOG EVENTS,#查看第一个日志文件000001
            SHOW BINLOG EVENTS [IN "指定查看日志文件名’ FROM Pos值 LIMIT OFFSET, ROW_COUNT], #查看指定日志文件

        使用工具mysqlbinlog 作用:可以展示binlog命令清单
                               可以产看binlog日志内容细节
                               可以把binlog日志文件(xxxxx.000001)转换成sql文件 并可以自行设置导出 位置
 */
show binary logs;
show binlog events;
show binlog events in 'NINE-bin.000694';



/* 窗口函数
   窗口函数总体上可以分为序号函数、分布函数、前后函数、首尾函数和其他函数，如下表：
    函数分类 函数                函数说明
    序号函数 ROW_NUMBER()       顺序排序
            RANK()             并列排序，会跳过重复的序号，比如序号为1、1、3
            DENSE_RANK()       并列排序，不会跳过重复的序号，比如序号为1、1、2
    分布函数 PERCENT_RANK()     等级值百分比
            CUME_DIST()        累积分布值
    前后函数 LAG(expr. n)       返回当前行的前n行的expr的值
            LEAD(expr, n)      返回当前行的后n行的expr的值
    首尾函数 FIRST_VALUE(expr)  返回第一个expr的值
            LAST_VALUE(expr)   返回最后一个expr的值
    其他函数 NTH_VALUE(expr, n) 返回第n个expr的值
            NTILE(n)           将分区中的有序数据分为n个桶，记录桶编号

   语法1: 多行函数 over ([partition by 字段名 order by 字段名 asc[desc]])
   语法2: 多行函数 over 窗口名 ... window 窗口名 as ([partition by 字段名 order by 字段名 asc[desc]])
 */