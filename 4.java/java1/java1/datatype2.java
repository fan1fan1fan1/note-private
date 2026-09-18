import java.util.Scanner;

public class datatype2 {
    public static void main(String[] args){
        // 常见数据在代码中如何书写

        // 整数 小数
        System.out.println(666.66);

        // 字符串
        System.out.println("黑马程序员");

        // 字符
        System.out.println('女');

        // 布尔
        System.out.println(true);

        // 空  null不能直接打印  ""
        System.out.println("null");


        // \t 在打印的时候把前面的字符串长度补齐到8 或者8的整数倍
        // 最少补1个空格 最多补8个空格
        System.out.println("abc" + '\t');   // 补5个空格
        System.out.println("abcd" + '\t');  // 补3个空格
        // 在输出大范围数据时 使用\t 增加可读性 美观


        // 定义变量
        // 变量在使用之前一定要赋值
        int a = 10;
        System.out.println(a);



        // 一开始没有乘客
        int count = 0;

        // 第一站：上去一位乘客
        count += 1;

        // 第二站：上去两位乘客，下来一位乘客
        count = count + 2 - 1;

        // 第三站：上去两位乘客，下来一位乘客
        count = count + 2 - 1;

        // 第四站：下来一位乘客
        count = count - 1;

        // 第五站：上去一位乘客
        count = count + 1;

        // 请问：到了终点站，车上一共几位乘客。
        System.out.println(count);   // 3



        /* java 中
            二进制书写需要以0b开头
            八进制以0开头
            十六进制以0x开头
        */



        byte b = 10;  // byte  范围最小的数据类型
        short s = 20;
        System.out.println(b);  // 10

        long l = 50;   // 定义long类型变量时 需要在数值后面加L 作为后缀

        float f = 10.1F;   // float 后缀F

        double d = 20.2;

        char c = 'a';

        boolean o = true;



        /* 键盘录入 Scanner类 (3)
            1.导包 导包要写在类定义上边
              import java.util.Scanner;
        */

        // 2.创建对象 sc为变量名可更改
        Scanner sc = new Scanner(System.in);

        // 3.接收数据 i为变量名可更改
        int i = sc.nextInt();

        // 4.输出数据
        System.out.println(i);



        /* 键盘录入 格式
              import java.util.Scanner;
              Scanner sc = new Scanner(System.in);
              int i = sc.nextInt();
              System.out.println(i);
        */



        /* 键盘录入第一套体系
            遇到空格、制表符、回车就停止 这些符号后面的数据不会被接收
            nextInt(); 只能接收整数 接收其他类型会报错
            nextDouble(); 接收小数
            next(); 接收字符串 char
         */

        // Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个整数");
        int num1 = sc.nextInt();  // 输入 123 456
        System.out.println(num1);

        System.out.println("请输入第二个整数");
        int num2 = sc.nextInt();  // 输入 123 此处不需要录入 因为第一次录入有空格
        System.out.println(num2);

        // 在输入上述两个整数时 中间一个空格 理论上输出结果为123 456 123
        // 但nextInt遇到空格时就会停止录入 并把下面的数据赋给了第二次录入
        // 因此输出结果 123 456



        // 键盘录入第二套体系
        // nextLine(); 接收字符串 可以接收空格制表符 遇到回车才停止
        // Scanner sc = new Scanner(System.in);
        System.out.println(System.in);
        System.out.println("请输入第一个字符串");  // abc def
        String line1 = sc.nextLine();
        System.out.println(line1);

        System.out.println("请输入第二个字符串");  // abc
        String line2 = sc.nextLine();
        System.out.println(line2);

        // 输出结果为 abc def abc

        // 键盘录入两套体系不能混用 混淆空格的可行性2




        // 使用插件MarsCode 可以直接运行java代码
        // 快捷键: 选中代码 按alt+shift+R 即可运行
        /*
            数据类型转换
                自动类型转换
                    小范围数据类型 变量名 = 大范围数据类型数值;
                    例如:
                        int a = 10;
                        double b = 20.2;
                        b = a;
                强制类型转换
                    大范围数据类型 变量名 = (大范围数据类型)小范围数据类型数值;
        */
    }
}
