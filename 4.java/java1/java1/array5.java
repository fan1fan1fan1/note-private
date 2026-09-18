import java.util.Random;

public class array5 {
    public static void main(String[] args) {
        // 数组静态初始化完整格式
        int[] arr = new int[]{1, 2, 3, 4, 5};
        double[] arr2 = new double[]{1.1, 2.2, 3.3, 4.4, 5.5};

        // 1.数组简写格式
        int[] arr3 = {1, 2, 3, 4, 5};
        String[] arr4 = {"a", "b", "c", "d", "e"};
        double[] arr5 = {1.1, 2.2, 3.3, 4.4, 5.5};


        // 2.输出数组
        System.out.println(arr5); // [D@1b6d3586 地址值
        /*
         [        数组的开始 当前是一个数组
         D        数组类型 double int char boolean float short long byte
         @        分隔符 间隔符号 没有意义
         1b6d3586 十六进制 地址值
         ]        数组的结束
         */


        // 3.数组访问获取
        System.out.println(arr3[0]); // 1 数组的索引从0开始 下标数字


        // 4.数组访问修改
        arr2[0] = 1.0;
        System.out.println(arr2[0]); // 10 数据覆盖之后原来的数据就不在了


        // 5.数组的长度 arr.length
        System.out.println(arr.length);


        // 6.数组遍历
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
        /* idea提供的快速生成数组遍历过程
            arr.fori
            快捷键：ctrl + j
         */


        // 7.数组动态初始化
        // 数据类型[] 数组名 = new 数据类型[数组长度];
        int[] arr6 = new int[5];
        System.out.println(arr6); // [I@1b6d3586
        System.out.println(arr6[0]); // 0 数组的默认值


        // 案例 添加50个学生信息
        String[] arr7 = new String[50];
        arr7[0] = "张三";
        System.out.println(arr7[0]); // 张三
        // 如果数组内不添加数据 则输出默认初始值 null 0 0.0 false /u0000


        // 索引越界异常 数组索引超出范围
        System.out.println(arr7[50]); // 报错 索引越界异常
        // 解决方法：在访问数组之前 先判断索引是否越界
        if (arr7.length > 50) {
            System.out.println(arr7[50]);
        }


        // 8.数组的内存图
        /*
         栈：存放局部变量 比如main

         堆：存放new出来的内容（实体，对象，数组）
            数组创建的完整格式中就有new关键字 new关键字就是在堆内存中开辟空间
             数组在初始化时，会为存储空间添加默认值 有地址值
             整数：0
             浮点数：0.0
             字符：\u0000
             布尔：false
             引用数据类型：null

         方法区：存储.class文件相关信息，包含方法的信息

         本地方法栈：与操作系统相关

         寄存器：与CPU相关
         */


        // 栈
        int a = 10;
        int b = 10;
        int c = a + b;
        System.out.println(c); // 20
        /*
         栈：先进入main
         然后依次将每一行输入
         定义一个栈存储a 为int类型 然后把10放在a里面
         定义一个栈存储b 为int类型 然后把10放在b里面
         定义一个栈存储c 然后将a和b中的值相加 然后把结果放在c里面
         最后输出c的值
         */


        // 当两个数组指向同一个小空间时，其中一个数组对小空间的值发生了改变，
        // 那么其他数组再次访问的时候都是修改之后的姐贵哦来



        // 数组求最值
        int[] arr8 = {1, 2, 3, 4, 5};
        int max = arr8[0];  // 假设第一个元素为最大值
        for (int i = 1; i < arr8.length; i++) {
            if (arr8[i] > max) {
                max = arr8[i];
            }
        }
        System.out.println("最大值为：" + max);  // 输出最大值


        // 数组求和并统计个数
        int[] arr9 = {1, 2, 3, 4, 5};
        int sum = 0;
        int count = 0;
        for (int i = 0; i < arr9.length; i++) {
            sum += arr9[i];
            count++;
        }
        System.out.println("数组元素的和为：" + sum);
        System.out.println("数组元素的个数为：" + count);


        // 数组交换位置
        int[] arr10 = {1, 2, 3, 4, 5};
        int temp = arr10[0];
        arr10[0] = arr10[4];
        arr10[4] = temp;
        System.out.println("交换后的数组为：");
        for (int i = 0; i < arr10.length; i++) {
            System.out.print(arr10[i] + " ");
        }


        // 数组打乱顺序
        int[] arr11 = {1, 2, 3, 4, 5};

        /* 打乱单个数据方法 -> for循环该过程即可
        Random random = new Random();  // 创建Random对象 用于生成随机 数
        int randomIndex = random.nextInt(arr11.length);  // 生成随机 索引
        System.out.println(randomIndex);
        */

        Random r = new Random();

        for (int i = 0; i < arr11.length; i++) {
            int randomIndex = r.nextInt(arr11.length);  // 生成随机索引
            //int randomIndex = (int) (Math.random() * arr11.length);  // 生成随机索引

            int temp1 = arr11[i];
            arr11[i] = arr11[randomIndex];
            arr11[randomIndex] = temp1;                              // 交换元素位置
        }
        System.out.println("打乱后的数组为：");

    }
}
