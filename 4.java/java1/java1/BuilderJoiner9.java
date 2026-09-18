import java.util.Scanner;
import java.util.StringJoiner;

public class BuilderJoiner9 {
    public static void main(String[] args) {
        // StringBuilder类: 主要用于字符串的拼接、修改、反转


        // StringBuilder可以看作是一个容器 创建之后里面的内容是可变的
        /*
           StringBuilder创建方法
            public StringBuilder()              创建一个空的字符串容器
            public StringBuilder(String str)    创建一个字符串容器 并将str中的内容添加到容器中

           StringBuilder常用方法
            public StringBuilder append(String str 任意类型)  在容器末尾添加字符串
            public StringBuilder reverse()                 反转容器中的字符串
            public int length()                           返回容器中的字符串长度
            public String toString()                      将容器中的字符串转换为String类型
         */


        // 在StringPractice8中 我们进行字符串拼接 效率低 可以使用StringBuilder类

        // 1.创建对象
        StringBuilder sb = new StringBuilder("");
        for (int i = 0; i < 9; i++) {
            sb.append(i);
        }

        // 2.打印
        System.out.println(sb); // 此处打印的是sb的属性值 不是地址

        // 3.添加元素
        sb.append(1);
        sb.append(2.3);

        // 4.反转
        sb.reverse();

        // 5.获取长度
        System.out.println(sb.length());

        // 6.转换为String类型
        String str = sb.toString();
        System.out.println(str);



        // 链式编程
        // 1.创建对象
        StringBuilder sb2 = new StringBuilder("");
        // 2.添加元素
        sb2.append(1).append(2.3).append("Hello").append(true);
        // 3.打印
        System.out.println(sb2);



        // 案例一 字符串反转 判断是否为回文数
        // 1.键盘输入一个字符串
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个字符串: ");
        String str1 = sc.next();

        // 2.反转字符串
        StringBuilder sb3 = new StringBuilder(str1);
        sb3.reverse().toString();
        System.out.println(sb3);

        // 3.比较
        if (str1.equals(sb3.toString())) {
            System.out.println("是回文数");
        }
        else {
            System.out.println("不是回文数");
        }



        // 案例二 定义一个方法将指定数组中的元素拼接成一个字符串
        // 1.定义一个数组
        int[] arr = {1, 2, 3, 4, 5};

        // 2.调用方法
        String result = arrayToString(arr);
        System.out.println(result);



        // StringJoiner 用于对类似将数组拼成字符串的解决方法

        /* StringJoiner也可以看成是一个容器
           StringJoiner创建方法
            public StringJoiner(间隔符号) 创建一个StringJoiner对象，指定拼接时的间隔符号
            public StringJoiner(间隔符号, 开始符号, 结束符号)

           StringJoiner使用方法
            public StringJoiner add(添加的元素) 向StringJoiner中添加元素
            public int length() 返回长度（字符出现的个数）
            public String toString() 将StringJoiner转换为String类型
         */



        // 1.已知数组
        int arr1[] = {1, 2, 3};

        // 2.创建StringJoiner对象
        StringJoiner sj = new StringJoiner(",","[","]");

        // 3.遍历数组添加到StringJoiner中
        for(int i=0; i<arr.length; i++){
            sj.add(arr[i] + "");
        }
        System.out.println(sj);



        StringJoiner sj2 = new StringJoiner("---");

        sj.add("aaa").add("bbb").add("ccc");

        int length = sj.length();
        System.out.println(length);

        String str2 = sj.toString();
        System.out.println(str2);



        // 简单案例
        String s1 = "abc";
        String s2 = "a" + "b" + "c";
        System.out.println(s1 == s2);   // true


        StringBuilder SB = new StringBuilder();

        System.out.println(SB.capacity());  // 容量 16
        System.out.println(SB.length());    // 长度 没添加任何东西 0

        SB.append("abc");
        System.out.println(SB.capacity());  // 容量 16
        System.out.println(SB.length());    // 长度 3

    }
    // 方法


    // 定义一个方法将指定数组中的元素拼接成一个字符串
    public static String arrayToString(int[] arr) {
        // 1.创建一个空的字符串容器
        StringBuilder sb = new StringBuilder();

        // 2.拼接数组的括号
        sb.append("[");

        // 3.遍历数组
        for (int i = 0; i < arr.length; i++) {
            // 4.拼接数组的元素
            if (i == arr.length - 1) {
                sb.append(arr[i]);
            }
            else {
                sb.append(arr[i]).append(", ");
            }
        }

        // 5.拼接数组的括号
        sb.append("]");

        return sb.toString();
    }
}
