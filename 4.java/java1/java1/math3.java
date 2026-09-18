import java.util.Scanner;

public class math3 {
    public static void main(String[] args) {
        // 1.使用MarsCode 编写代码

        // 定义一个数组 存储10个学生的成绩
        int[] scores = {80, 90, 70, 60, 85, 95, 75, 65, 82, 92};

        // 2.使用MarsCode 修改bug 下方# 选择文件


        // 新建一个模块   文件->项目结构-> + ->新建模块

        // 文件中关闭项目 打开新的项目 否则每一次打开idea默认进入上一次的项目


        // 键盘输入一个三位数 获取个位 十位 百位上数字
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个三位数：");
        int num = sc.nextInt();

        int ge = num % 10;
        int shi = num / 10 % 10;
        int bai = num / 100 % 10;

        System.out.println("个位：" + ge);
        System.out.println("十位：" + shi);
        System.out.println("百位：" + bai);



        // 1.数据类型隐式转化 取值范围小的变成取值范围大的
        // 2.数据类型强制转化 取值范围大的变成取值范围小的


        // 1.隐式转换 自动类型提升
        int a = 10;
        double b = a;   // b=10.0

        // byte short char三种类型在运算时会提升为int
        // byte < short < int < long < float < double



        // 2.显示转化 有可能导致数据发生错误
        double A = 12.3;
        int B = (int) A;
        System.out.println(B);

        byte b1 = 10;
        byte b2 = 20;
        byte result = (byte)(b1 + b2);
        System.out.println(result);  // 30


        // 字符串相加  "+"字符串拼接符
        System.out.println("123" + 123); // 123123

        int age = 18;
        System.out.println("我的年龄是" + age + "岁");   // √
        System.out.println("我的年龄是" + "age" + "岁");

        System.out.println(1 + 2 + "abc" + 1 + 2); // 3abc12



        // char类型在计算时会转成int    将字母转换成ASCII表
        char c = 'a';
        int result1 = c + 0;
        System.out.println(result1);  // 97

        System.out.println(1 + 'a');  // 98
        System.out.println('a' + "abc");    // aabc



        // 自增
        int x = 10;
        int y = x++;
        int z = ++x;
        System.out.println(x);  // 12
        System.out.println(y);  // 10
        System.out.println(z);  // 12


        // 赋值运算符 += -= *= /= %=

        // 关系运算符 == != > < >= <=

        // 逻辑运算符 &  | 无论左边是否成立 右边都会再执行一次
                 // ^异或(相同true 不同false)   !非(取反)

        // 短路逻辑运算符 &&  ||  当左边的表达式能确定结果时 不再执行右边表达式

        // 三元运算符  条件表达式(判断) ? 表达式1 : 表达式2
        int i=1,j=2;
        int max = i > j ? i : j;
        System.out.println(max);   // 三元运算符的结果一定要被使用



        // 原码 反码 补码    最左边是符号位 0为正 1为负

        /* 原码: 已知一个数字 将它变成二进制 最左边的一个个位数变成正负号 就是原码
             原码的范围: 1个bit b个字节
               最大值: 01111111  127
               最小值: 11111111  -127
             为了解决原码计算负值的结果与实际结果相反 -> 反码
        */



        /* 反码: 已知一个数字变成二进制后 符号位(第一位)不变 数值取反
             已知-55  二进制10011011(原码)
                     反码  11100100
             这样将二进制结果加减数的时候 得到的就是十进制加减数后的结果
             反码的0有两种表现形式 00000000  10000000 结果跨0会出现错误 不跨零则没有错误可以使用
             为了解决反码计算跨0的结果与实际结果相反 -> 补码
        */



        /* 补码: 已知二进制后 符号位(第一位)不变 数值取反 然后+1
             这样把一个0的表现形式去掉了 而在最末端多了一位  10000000 令为-128 只有补码
             在计算机中 都是以补码的形式存储的
        */


        // 三个码解释了隐式转换的流程 就是在二进制前面补0 强制转化就是在前面补1

        // 其他的运算符  <<左移(低位补0)    >>右移(高位补0 1)   >>>无符号右移(高位补0)
        int n = 200;
        int m = 10;
        System.out.println(n & m);   // n m转换成二进制 依次位比较 相同输出1 不同输出0
        System.out.println(n | m);   // 只要有1位是1就输出1 都是0就输出0
        System.out.println(a << 2);  // 得到200的二进制补码 把最左边的两个数删除 在最末尾补两个0  -> 800
        System.out.println(a >> 2);  // 最左侧左移 正数就补两个0 负数就补两个1 删除最后两位 -> 50
        System.out.println(a >>> 2); // 无符号右移 补0

    }
}
