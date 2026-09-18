package Math;

import java.io.IOException;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.RoundingMode;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Random;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class API1 {
    public static void main(String[] args) throws IOException, ParseException {
        // API java内部设定的方法

        // 记类名和作用 养成查阅API的习惯

        // API一 Math 数学工具类 私有化构造方法 所有的方法都是静态的

        /* abs 求绝对值
            max 求最大值
            pow 求次幂
            sqrt 求平方根
            round 四舍五入
            ceil 向上取整
            floor 向下取整
            random 求随机数
         */
        System.out.println(Math.abs(-10));
        System.out.println(Math.max(10, 20));
        System.out.println(Math.pow(2, 3));
        System.out.println(Math.sqrt(4));
        System.out.println(Math.round(3.5));
        System.out.println(Math.ceil(3.1));
        System.out.println(Math.floor(3.9));
        // 求1-100的随机数
        System.out.println(Math.random() * 100);



        // API二 System 系统工具类 私有化构造方法 所有的方法都是静态的

        /* 1.退出程序public static void exit(int status)
            0 正常退出 1 异常退出
         */
        System.exit(0);


        /* 2.获取当前时间的毫秒值public static long currentTimeMillis()
            计算代码执行到此处的时间
         */
        long timeT = System.currentTimeMillis();
        System.out.println(timeT);


        /* 3.数组的复制
            public static void arraycopy
             (Object src, int srcPos, Object dest, int destPos, int length)
             原数组        起始索引      目标数组        起始索引      复制的长度(个数)

            数组的类型必须一致
            数组长度必须大于等于复制的长度
            如果数组为引用类型 复制的是地址 子类可以复制父类的属性 但是不能复制父类的方法
        */
        int[] arr = {1, 2, 3, 4, 5};
        int[] arr2 = new int[5];
        System.arraycopy(arr, 0, arr2, 0, 5);
        for (int i = 0; i < arr2.length; i++) {
            System.out.println(arr2[i]);
        }



        /* API三 Runtime
            表示虚拟机运行环境

            public static Runtime getRuntime() 获取当前虚拟机的运行环境
            public void exit(int status) 退出程序 停止虚拟机
            public int availableProcessors() 获取当前虚拟机的处理器cpu数量
            public long maxMemory() JVM能从系统中获取总内存大小 单位byte
            public long totalMemory() 获取当前虚拟机的总内存
            public long freeMemory() 获取当前虚拟机的空闲内存
            public Process exec(String command) 执行系统cmd命令
         */
        // 1.获取Runtime的对象
        Runtime r1 = Runtime.getRuntime();
        Runtime r2 = Runtime.getRuntime();
        System.out.println(r1 == r2);

        // 2.exit 停止虚拟机
        Runtime.getRuntime().exit(0);

        // 3.获取cpu的线程数
        System.out.println(r1.availableProcessors());

        // 4.获取内存的大小
        System.out.println(r1.maxMemory() / 1024 / 1024);
        System.out.println(r1.totalMemory() / 1024 / 1024);
        System.out.println(r1.freeMemory() / 1024 / 1024);

        // 5.运行cmd命令
        // 打开一个记事本
        Runtime.getRuntime().exec("notepad");
        /*
            exec报错 按住alt+回车 选择第一个 在包名后加一些东西取消报错

            shutdown关机 需要加上参数执行
            -s 默认在1分钟之后关机
            -t 指定时间
            -s -t 指定时间关机
            -a 取消关机操作
            -r 关机并重启
         */
        Runtime.getRuntime().exec("shutdown -s -t 30");

        // 有一个恶搞好基友的项目案例



        /* API四 Object
            所有的类的父类
            方法：
                public Object() 空参构造 构造方法
                public String toString() 调用对象的toString方法 变成字符串输出
                public boolean equals(Object obj) 比较两个对象是否相等 首先比较地址值、数据类型、数据内容
                public int hashCode() 返回对象的哈希值
                public Class<?> getClass() 返回对象的Class对象
                public Object clone() 创建对象的副本
         */
        // 1.空参构造
        Object obj = new Object();

        // 2.toString()
        System.out.println(obj.toString());
        /* String str = obj.toString
           System.out.println(str)

           想要的是对象的属性 但是toString()方法是Object类的方法 没有属性
           所以我们需要重写toString()方法

           @Override (不在同一个文件)
            public String toString() {
                return "Object{name = " + name + ", age = " + age + "}";
            }
         */


        // 3.equals()
        System.out.println(obj.equals(obj));
        /* Student s1 = new Student;
           Student s2 = new Student;
           result = s1.equals(s2);
           System.out.println(result);

           结果：false
           如果没有进行重写 我们使用Object方法比较 比较地址值
           原因：equals方法是Object类的方法 比较的是对象的地址 地址值不同
           所以我们需要重写equals方法 比较属性值

           @Override 不在同一个文件
            public boolean equals(Object obj) {
                if (this == obj) {
                    return true;
                }
                if (obj == null || getClass() != obj.getClass()) {
                    return false;
                }
                Student student = (Student) obj;
                return age == student.age && Objects.equals(name, student.name);
            }

            stringBuilder != String
            数据类型不同 不需要继续比较
         */


        // 4.clone()
        /*
           在类包中先重写clone方法
           @Override
           public Object clone() {
               return super.clone();
           }

           同时在类名上实现Cloneable接口 (标记性接口)
           public class  implements Cloneable {
               ...
           }

           在测试类中
           Object obj3 = obj.clone();
           假设需要实现强转 Object obj3 = (Object) obj.obj3.clone();
            System.out.println(obj3);
         */

        /* 克隆分深克隆和浅克隆
            深克隆：克隆对象的属性 以及属性的属性
            浅克隆：克隆对象的属性 但是属性的属性不克隆

            深克隆：需要重写clone方法 并且在类名上实现Cloneable接口 并且属性的类也需要实现Cloneable接口
            浅克隆：不需要重写clone方法 但是在类名上实现Cloneable接口 但是属性的类不需要实现Cloneable接口

            注意：如果属性的类没有实现Cloneable接口 那么属性的属性也不会克隆
         */



        /* 深克隆第三方工具
            Gson gson = new Gson();

            String s = gson.toJson(obj); 变成字符串
            System.out.println(s);

            gson.fromJson(s, obj.getClass()); 再把字符串变回对象
            System.out.println(obj)
         */



        /* API五 Objects工具类
            提供一些方法 实现一些功能
            public static boolean equals(Object a, Object b) 先做非空判断，比较两个对象
            public static boolean isNull(Object obj) 判断对象是否为空
            public static boolean nonNull(Object obj) 判断对象是否不为空

            判断相等
            @Override
            public boolean equals(Object o) {
                if (this == o) return true;
                if (o == null || getClass() != o.getClass()) return false;
                Student student = (Student) o;
                return age == student.age && Objects.equals(name, student.name);
            }

            测试类
            Student s1 = new Student("张三", 18);
            Student s2 = new Student("张三", 18);

            boolean result = Objects.equals(s1, s2);
            System.out.println(result);

            System.out.println(Objects.isNull(s1));
            System.out.println(Objects.nonNull(s1));
         */



        /* API六 BigInteger
            大整数
            超出了long的范围 999999999999999999999999999999999
            可以表示任意大小的整数
            但是运算速度慢

            public BigInteger(int num, Random rnd) 获取随机大整数 范围(0, 2的num次方-1)
        常用 public BigInteger(String val) 把字符串变成大整数 (里边写整数)
            public BigInteger(String val, int radix) 获取指定进制的大整数
                                          表示进制
        常用 public static BigInteger valueOf(long val) 把long类型的整数变成大整数
                                                       静态方法获取BigInteger的对象 内部有优化
            对象一旦创建 内部记录的值不能发生改变
            创建了一个b1值 就不能再改变

         */

        // 1.获取随机大整数
        Random r = new Random();
        BigInteger b1 = new BigInteger(10, r);
        System.out.println(b1);  // 从0-2的10次幂-1中 获取一个随机数

        // 2.把字符串变成大整数
        // 就是输出一个超过int范围的数字 用的多
        // " "必须输入整数 否则报错
        BigInteger b2 = new BigInteger("1234567890");
        System.out.println(b2);

        // 3.获取指定进制的大整数
        // " " 必须输入整数 否则报错 且必须和进制吻合
        BigInteger b3 = new BigInteger("1010101010", 2);
        System.out.println(b3);

        // 4.静态方法获取
        // 范围小 在long的范围内取值
        // -16 到 16 进行了优化 已创建好
        BigInteger b4 = BigInteger.valueOf(100);
        System.out.println(b4);

        BigInteger b5 = BigInteger.valueOf(1000000000000000000L);
        System.out.println(b5); // L表示long类型 不能超过范围



        /* API七 BigInteger的运算
            加法：add
            减法：subtract
            乘法：multiply
            除法：divide
            取余：remainder
            获取商和余数：divideAndRemainder
            比较是否相同：equals
            次幂：pow
            较大值：max
            较小值：min
            转为int：intValue 超出范围报错
         */

        // 1.创建对象
        BigInteger bd1 = BigInteger.valueOf(10);
        BigInteger bd2 = BigInteger.valueOf(5);

        // 2.相加
        BigInteger bd3 = bd1.add(bd2);
        System.out.println(bd3);

        // 3.除法
        BigInteger[] bd4 = bd1.divideAndRemainder(bd2);
        System.out.println(bd4.length);
        System.out.println(bd4[0]);
        System.out.println(bd4[1]);

        // 4.比较是否相同
        System.out.println(bd1.equals(bd2));

        // 5.次幂
        System.out.println(bd1.pow(2)); // pow、里必须是数字

        // 6.较大值 max
        System.out.println(bd1.max(bd2));

        // 7.转为int 不能超出范围
        System.out.println(bd1.intValue());

        // 8.转为long 不能超出范围
        System.out.println(bd1.longValue());

        BigInteger bd5 = BigInteger.valueOf(100);
        int i = bd5.intValue();
        System.out.println(i);


        /* BigInteger底层存储方式
            通过二进制补码
            以32位为一组 mag表数组
            然后转成十进制
            放进一个数组中
         */



        /* API八 BigDecimal
            大浮点数
            超出了double的范围
            可以表示任意大小的浮点数
            但是运算速度慢

            考虑二进制中小数的计算方法复杂

            BigDecimal用于小数的精度计算 用于表示很大的小数

            创建对象时推荐使用字符串的方式 也就是在输入数字时 ""
         */

        // 1.创建对象
        BigDecimal bdd1 = new BigDecimal("10.0");
        BigDecimal bdd2 = new BigDecimal("5.0");

        // 2.相加
        BigDecimal bdd3 = bdd1.add(bdd2);
        System.out.println(bdd3);

        // 3.静态方法获取对象
        BigDecimal bdd4 = BigDecimal.valueOf(10.0);
        System.out.println(bdd4);



        /* 如果表示数字不大 没有超出double范围 建议使用静态方法
            public static

           如果表示数字很大 超出double范围 建议使用构造方法
            修饰符 class(){}

           如果传递数字是0-10间整数(小数不行) 包括边界 方法会返回已经创建的整数 不会new
         */



        /* BigDecimal的使用 常见方法
            1.创建对象
            2.静态方法获取对象
            3.常用方法
                1.加法 add
                2.减法 subtract好久哦，
                3.乘法 multiply
                4.除法 divide 精确几位 舍入模式
                5.取余 remainder
                6.比较大小 compareTo
                7.格式化输出 setScale
                8.四舍五入 round
                9.取整 floor
                10.取余 abs
                11.取反 negate
                12.取最大数 max
                13.取最小数 min
         */


        // 1.加法
        BigDecimal bbd1 = BigDecimal.valueOf(10.0);
        BigDecimal bbd2 = BigDecimal.valueOf(2.0);
        System.out.println(bbd1.add(bbd2));

        // 2.除法
        BigDecimal bbd3 = bbd1.divide(bbd2);
        System.out.println(bbd3);

        // 如果除不尽
        BigDecimal bbd4 = bbd1.divide(bbd2, 2, RoundingMode.HALF_UP);
                                   // 除以谁  保留小数 四舍五入
        System.out.println(bbd4);



        /* API九 正则表达式Regex
            1.用来校验字符串是否符合某种规则
            校验手机号 邮箱 密码 验证码
            2.在一段文本中查找满足要求的内容

            qq.matches("正则表达式");

            正则表达式： 只能表示一个字符
                \转义字符 改变后面字符的含义
                1.\\d 表示数字 [0-9]
                2.\\D 表示非数字 [^0-9]
                3.\\w 表示字母数字下划线
                4.\\W 表示非字母数字下划线
                5.\\s 表示空格
                6.\\S 表示非空格
                7.\\. 表示任意字符
                8.\\| 表示或
                9.\\^ 表示以什么开头
                10.\\$ 表示以什么结尾
                11.\\* 表示0个或多个

                [] 表示范围
                1.[abc] 只能是a b或c
                2.[^abc] ^取反  表示除了a b c
                3.[a-zA-Z0-9] 范围 包括端点 a-z A-Z 0-9
                4.[a-d[0-9]] 表示a到d或0到9
                5.[a-z&&[def]] 表示a到z且包含d e f
                6.[a-z&&[^def]] 表示a到z且不包含d e f
                7.[a-z&&[^m-p]] 表示a到z且不包含m到p

                X? 表示0个或1个
                X* 表示0个或多个
                X+ 表示1个或多个
                X{n} 正好n次
                X{n,} 至少n次
                X{n,m} 至少n次 最多m次
         */

        System.out.println("a".matches("[abc]"));
        System.out.println("ab".matches("[abc][abc]"));
        // 正则表达式依次只能匹配一个字符

        System.out.println("3".matches("\\d"));  // true
        System.out.println("_".matches("\\w"));  // true
        System.out.println("你".matches("\\W"));  // true

        System.out.println("23-F".matches("[a-zA-Z0-9]"));  // False

        // 正则快捷方式 String r = ""; 右键双引号 anyRule
        String re = "";



        /* 首先校验一个手机号 要求6-20位数字 不能有其他字符 且0不能开头
            String qq = "12345678901234567890";
            int len = qq.length();

            def:
            if(len < 6 && len > 20){
                return false;
            }

            if(qq.startsWith("0")){
                return false;
            }

            for(int i = 0; i < len; i++){
                char c = qq.charAt(i);
                if(c < '0' || c > '9'){
                    return false;
                }
            }
            return true;
         */

        // 使用正则表达式 校验上述qq号
        String qq = "12345678901234567890";
        System.out.println(qq.matches("[1-9]\\d{5,19}"));



        /* 案例一 校验手机号 13112345678 13712345667 13912345667
            1手机号以1开头
            [3-9]手机号第二位只能是3-9
            \\d{9}手机号后面9位只能是数字
         */
        String phone = "1[3-9]\\d{9}";
        System.out.println("13112345678".matches(phone));
        System.out.println("13712345667".matches(phone));
        System.out.println("13912345667".matches(phone));

        String phone2 = "0\\d{2,3}-?[1-9]\\d{4,9}";
        System.out.println("010-12345678".matches(phone2));
        System.out.println("010-1234567".matches(phone2));
        System.out.println("010-123456789".matches(phone2));


        // 案例二 邮箱号码
        String email = "[a-zA-Z0-9_]+@[a-zA-Z0-9]+(\\.[a-zA-Z0-9]+)+";
                                            // \\.打一个.
                                            // []+匹配一个或多个 (\\.[]+)一个或多个
        System.out.println("123456@qq.com".matches(email));
        System.out.println("zhangshan@163.com.cn".matches(email));
        System.out.println("123456@qq.com.cn.com".matches(email));



        // 正则忽略字母大小写方法 在该字符前面加 (?i)
        System.out.println("aA1234567890123456X".matches("(?i)[1-9]\\d{16}(\\d[x] | x)"));


        // 案例三 身份证号
        String id = "[1-9]\\d{16}(\\d(?i)x)";



        // API十 爬虫
        /* Pattern类
            所属于 java.util.regex包    java.util.regex.Pattern
            作用： 编译正则表达式
            方法：
                compile(String regex) 编译正则表达式
                matches(String regex, CharSequence input) 校验字符串是否符合正则表达式
                split(CharSequence input) 按照正则表达式分割字符串
                replaceAll(CharSequence input, String replacement) 替换字符串
                replaceFirst(CharSequence input, String replacement) 替换第一个字符串
                find() 查找字符串
                start() 查找字符串开始位置
                end() 查找字符串结束位置
                group() 查找字符串分组
         */

        /* Matcher类
            所属于 java.util.regex包     java.util.regex.Matcher
            作用： 匹配正则表达式
                  文本匹配器 按照正则表达式的规则去读取字符串 从头开始读取
            方法：
                find() 查找字符串
                start() 查找字符串开始位置
                end() 查找字符串结束位置
                group() 查找字符串分组
         */

        // 1.已知一句话 爬取该句
        String str ="Java自从95年问世以来，经历了很多版本，目前企业中用的最多的是Java8和Java11," +
        "因为这两个是长期支持版本，下一个长期支持版本是Java17，相信在未来不久Java17也会逐渐登上历史舞台";

        // zhengze1(str); 函数

        // 2.获取正则表达式的对象
        Pattern p = Pattern.compile("Java\\d{0,2}");

        // 3.获取文本匹配器
        Matcher m = p.matcher(str);

        // 4.循环
        while(m.find()){
            String s = m.group();
            System.out.println(s);
        }



        /* 特殊情况
            1.只获取指定数据的某相同波分 如：Java8 Java11 Java17 -> 只输出三个Java
                Java(?=8|11|17)
                =表示Java后面跟随的数据 但我们只输出前半部分
            2.只要除了指定位置的文本
                Java(?!8|11|17)
                !表示Java后面跟随的数据 但我们只输出前半部分
         */



        /* 贪婪爬取 非贪婪爬取
            默认贪婪爬取 尽可能多的爬取
            非贪婪爬取 尽可能少的爬取
            贪婪爬取：.*
            非贪婪爬取：.*? 即在正常爬取后面加?

            已知字符串 abbbbbbbaaaaaaa

            按照ab+的方式爬取ab b尽可能多 贪婪爬取 abbbbbbb
            按照ab+的方式爬取ab b尽可能少 非贪婪爬取 ab
         */
        String strR = "abbbbbbbaaaaaaa";
        String regex = "ab+";
        Pattern P = Pattern.compile(regex);
        Matcher M = P.matcher(strR);
        while(M.find()){
            System.out.println(m.group());
        }


        /* 正则表达式在字符串中使用
            matches
            replaceAll 替换所有
            split 切割
         */
        strR.replaceAll("[[a-zA-Z0-9]&&[^ ]]+","vs");
        // 把正则中的结果变成vs

        String[] arr1 = strR.split("[[a-zA-Z0-9]&&[^ ]]+"); // 把正则的位置用a切割 输出原来的字符串数据
        for (int j = 0; j < arr1.length; j++) {
            System.out.println(arr1[j]);
        }



        /* 正则分组 以左括号为基准 只看左括号 以左括号先后区分一二三组
            捕获分组 把这一组的数据捕获出来 再用一次
            (.).+\\1

            非捕获分组 把这一组的数据捕获来 仅仅是把数据括起来 但不保存 再用一次
            (?:正则) (?=正则) (?!正则)

            (.) 把首字母看作一组
            \\1 把首字母拿出来再次使用
            *   作用于\\1 表示后面重复的内容出现0次或多次

            正则内部使用 \\组号 \\1
            正则外部使用 $组号   $1
         */



        /* 时间相关
            1.时间相关类
                Date 时间 日期
                Calendar  日历类
                SimpleDateFormat 格式化时间

                优化代码 维护数据安全
                ZoneId Instant ZonedDateTime
                DateTimeFormatter
                LocalDate LocalTime LocalDateTime
                Duration Period ChronoUnit
         */

        /* API十一 Date时间类
            javabean类 空参默认指系统当前时间
                       有参表示指定时间

            public class Date{
                private long time; 当前时间的毫秒值

                public Date(){ 空参构造方法
                    this.time = System.currentTimeMillis();
                }

                public Date(long time){ 有参构造方法
                    this.time = time;
                }

                get set方法
                public long getTime(){
                    return time;
                }
                public void setTime(long time){
                    this.time = time;
                }
            }
         */

        // 1.创建对象表示一个时间
        Date d1 = new Date();
        System.out.println(d1);

        // 2.创建对象表示一个时间
        Date d2 = new Date(0L); // 此时输入的数据类型为long 最好再数字尾加L
        System.out.println(d2);

        // 3.setTime 修改
        d2.setTime(1000L);
        System.out.println(d2);

        // 4.getTime 获取
        System.out.println(d2.getTime());



        // 练习一 打印时间原点开始一年之后的时间
        Date d3 = new Date(0L);
        long time = d3.getTime();
        time += 1000L * 60 * 60 * 24 * 365; // time加上一年的毫秒值
        d3.setTime(time);
        System.out.println(d3);



        // 练习二 比较时间谁在前在后
        Date d4 = new Date(1000L);
        Date d5 = new Date(2000L);
        System.out.println(d4.before(d5)); // d4是否在d5之前 true
        System.out.println(d4.after(d5)); // d4是否在d5之后 false

        /* d4和d5是对象 不能直接比较 d4>d5 ×
            取地址值
            long time4 = d1.getTime();
            long time5 = d2.getTime();
            time4 > time5
         */



        /* API十二 simpleDateFormat类
            格式化 把时间格式化成指定的格式 年月日时分
            解析 把指定格式的时间解析成时间


            构造方法
            1.空参使用默认格式
            public SimpleDateFormat(){
                this.pattern = "yyyy-MM-dd HH:mm:ss";
            }
            2.指定格式
            public SimpleDateFormat(String pattern){
                this.pattern = pattern;
            }


            常用方法
            1.格式化 日期对象->字符串
            public String format(Date date){
                return format(date.getTime());
            }
            2.解析 字符串->日期对象
            public Date parse(String source){
                return new Date(parse(source).getTime());
            }


            模式 y年 M月 d日 H时 m分 s秒 E星期
             2025-8-11 23:11:00
            yyyy-MM-dd HH:mm:ss yyyy年MM月dd日 HH:mm:ss
         */

        // 1.利用空参创建simpleDateFormat对象
        SimpleDateFormat sdf = new SimpleDateFormat();
        Date D1 = new Date(0L);

        // 2.格式化 日期->字符串
        String str1 = sdf.format(D1);
        System.out.println(str1);


        // 1.利用有参创建SimpleDateFormat对象
        SimpleDateFormat sdf1 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss EE");
        // 2.格式化 日期->字符串
        String str2 = sdf1.format(D1);
        System.out.println(str2);


        // 1.定义一个字符串表示时间
        String str3 = "2025-8-11 23:11:00 星期一";

        // 2.利用有参创建SimpleDateFormat对象
        SimpleDateFormat sdf2 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss EE");

        // 3.解析 字符串->日期对象 异常add一个标签
        Date D3 = sdf2.parse(str3);
        System.out.println(D3);



        // 练习一 将---变成年月日
        String da = "2025-8-11";
        SimpleDateFormat sdf3 = new SimpleDateFormat("yyyy-MM-dd");
        Date D4 = sdf3.parse(da);
        SimpleDateFormat sdf4 = new SimpleDateFormat("yyyy年MM月dd日");
        String str4 = sdf4.format(D4);
        System.out.println(str4);



        // 练习二 秒杀活动 比较两个时间
        String str5 = "2025-8-11 11:11:11";
        String str6 = "2025-8-11 11:11:12";
        SimpleDateFormat sdf5 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        Date D5 = sdf5.parse(str5);
        Date D6 = sdf5.parse(str6);
        System.out.println(D5.before(D6));
        System.out.println(D5.after(D6));



        /* API十三 Calendar
            代表日历对象 可以单独修改 获取年月日
            1.Calendar是一个抽象类 不能直接创建对象


            public static Calendar getInstance(){ 获取当前时间的日历对象
                return new GregorianCalendar();

                public final Date getTime() 获取日历对象
                public final setTime() 设置日历对象
                public long getTimeInMillis() 获取时间毫秒值
                public void setTimeInMillis(long time) 设置时间毫秒值
                public int get(int field) 获取指定字段的值
                public void set(int field,int value) 设置指定字段的值
                public void add(int field,int amount) 对指定字段的值进行加减
            }
         */

        // 1.获取日历对象
        // 会根据系统的不同时区来获取不同的日历对象 默认表示当前时间
        Calendar c = Calendar.getInstance();

        // 2.修改一下日历代表的时间 两种方法Date和setTime
        Date d = new Date(0L);
        c.setTime(d);
        System.out.println(c);

        // 3.获取时间单位
        // 时间单位放在一个数组中 索引 0纪元 1年 2月 3周(年中) 4周(月中) 5日
        int year = c.get(1);      // c.get(Calender.YEAR)
        int month = c.get(2) + 1; // c.get(Calender.MONTH)
        int day = c.get(5);       // c.get(Calender.DAY_OF_MONTH)



        /* 月份0-11           0表示1月 11表示12月
           星期日是一周中的第一天 1星期日 2星期一

           由于这种误差 我们可以写一个函数解决这个问题

           查表法 让数据和索引产生对应关系
        */
        System.out.println(year+getWeek(c.get(7)));

        // 4.修改
        c.set(Calendar.YEAR,2025);

        // 5.增加
        c.add(Calendar.MONTH,1);
        System.out.println(c);







    }

    private static void zhengze1(String str) {
        // 2.获取正则表达式的对象
        Pattern p = Pattern.compile("Java\\d{0,2}");

        // 3.获取文本匹配器:  m匹配器对象 str大串(话) p规则
        // m要在str中找符合p规则的小串
        Matcher m = p.matcher(str);

        // 4.使用文本匹配器 开始读取是否有满足规则的子串
        boolean b = m.find();

        /*while(m.find()){
            System.out.println(m.group());
        }
        */

        // 5.获取匹配到的子串 根据find结果 截取字串
        String s = m.group();
        System.out.println(s);

        // 6.第二次调用find 读取后面的内容 读取到第二个满足的字串 返回
        boolean bo = m.find();
        System.out.println(bo);
        System.out.println(m.group());
    }

    // 查表法
    public static String getWeek(int index){
        String[] arr = {"","星期日","星期一","星期二","星期三","星期四","星期五","星期六"};
        return arr[index]; // 0索引为空
    }

}