import java.util.Scanner;

public class String8 {
    public static void main(String[] args) {
        // API: Application Programming Interface 应用程序编程接口 使用已经定义好的方法 直接使用不用编写

        // java API: jdk中提供的各种功能的java类

        // Scanner类: 键盘输入
        // Random类: 随机数

        // 键盘输入
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个字符串(小数): ");
        sc.nextDouble();
        double result = sc.nextDouble();
        System.out.println("输入的数字是: " + result);



        // 字符串 java.lang.String 使用时不需要导包
        // 字符串是常量, 是不可变的, 一旦创建, 就不能修改

        // 字符串可拼接 拼接后会生成新的字符串
        String str1 = "Hello";
        String str2 = "World";
        System.out.println(str1 + str2); // 当前字符串个数为3



        /* 创建String对象的两种方式
            方法一
            直接赋值: String str = "Hello";

            方法二
            使用new关键字: String str = new String("Hello");
                         public String()                创建空字符串
                         public String(String original) 创建一个与original相同的字符串 即根据像想传入的类型 创建字符串
                         public String(char[] chs)      创建一个字符数组的字符串
                         public String(byte[] bytes)    创建一个字节数组的字符串

            直接赋值的方式会在字符串常量池中创建对象, 而使用new关键字的方式会在堆内存中创建对象
            直接赋值的方式会在字符串常量池中创建对象, 而使用new关键字的方式会在堆内存中创建对象
         */



        // 使用new关键字创建字符串
        // 1.传递一个字符串 根据传递的字符串内容再创建一个新的字符串对象
        String str3 = new String("Hello");
        String str4 = new String("Hello");
        System.out.println(str3 == str4); // false 两个对象的地址不同

        // 2.传递一个字符数组 根据传递的字符数组内容再创建一个新的字符串对象
        char[] chs = {'H', 'e', 'l', 'l', 'o'};
        String str5 = new String(chs);
        System.out.println(str5); // Hello

        // 需求 改变这个字符数组内容    eg.修改Hello为helloWorld


        // 3.传递一个字节数组 根据传递的字节数组内容再创建一个新的字符串对象
        // 应用场景: 在网络中传输的数据都是字节信息 需要将字节信息转换为字符串信息
        byte[] bytes = {72, 101, 108, 108, 111};
        String str6 = new String(bytes);
        System.out.println(str6); // Hello



        // 创建String对象的方式
        String s1 = "Hello";
        String s2 = new String();
        String s3 = new String("Hello");

        byte[] Bytes = {72, 101, 108, 108, 111};
        String s4 = new String(Bytes);

        char[] chars = {'H', 'e', 'l', 'l', 'o'};
        String s5 = new String(chars);



        // 对String类的内存模型解释

        // 栈内存 与方法有关 方法运用的时候进栈 执行完就出栈
        // 堆内存 与new有关 new出来的对象都在堆内存中

        /* String Table字符串常量池
            与字符串有关 字符串常量池是在堆内存中

            只有直接赋值的字符串存在常量池中 new出来的字符串不存在常量池中

            串池中存储的是字符串的地址

            直接赋值的字符串可以重复使用
            new出来的字符串不能重复使用  会直接在堆内存中创建一个新的对象

            比较时 基本数据类型比较数据值 引用数据类型比较地址值
            new出来的字符串记录的是地址值 比较的就是数据地址值
        */



        String com1 = "abc";
        String com2 = "abc";
        System.out.println(com1 == com2); // true
        // 直接赋值的数据在串池中 可以重复使用 所以com1和com2指向的是同一个对象

        String com3 = new String("abc");
        String com4 = "abc";
        System.out.println(com3 == com4); // false



        // 字符串比较
        /*
            boolean equals(Object obj)           比较字符串的内容是否相同           eg.用户名密码
            boolean equalsIgnoreCase(String str) 比较字符串的内容是否相同 忽略大小写  eg.验证码
         */

        // 1.创建两个字符串对象
        String com5 = "abc";
        String com6 = new String("abc");

        // 2. ==号比较
        System.out.println(com5 == com6);  // false

        // 3. equals()方法比较 比较字符串对象中内容是否相等
        boolean result1 = com5.equals(com6);
        System.out.println(result1);  // true



        // 一种比较的特殊情况
        // 1.假如键盘输入一个abc
        Scanner sc1 = new Scanner(System.in);
        System.out.println("请输入一个字符串: ");
        String str7 = sc1.next();  // 输入abc

        // 2.代码中再定义一个字符串abc
        String str8 = "abc";

        // 3.比较两个字符串是否相等
        System.out.println(str7 == str8);  // false

        // 得到结论: 键盘输入的字符串与代码中定义的字符串不是同一个对象 键盘录入得到字符串是new出来的
    }
}
