package practice;

public class test2 {
    public static void main(String[] args) {
        /* 不死神兔
            有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后
            每个月又生一对兔子，假如兔子都不死，问第十二个月的兔子对数为多少？

            递归
            斐波那契数列：1、1、2、3、5、8、13、21、34、55、89、144...
            这个数列从第3项开始，每一项都等于前两项之和。
         */

        // 方法一
        // 1.创建一个长度为12的数组
        int[] arr = new int[12];

        // 2.给索引0和1赋值1
        arr[0] = 1;
        arr[1] = 1;

        // 3.for循环给数组赋值
        for (int i = 2; i < arr.length; i++) {
            arr[i] = arr[i-1] + arr[i-2];
        }

        // 4.打印第12组
            System.out.println(arr[11]);



        // 方法二 递归函数
        System.out.println(f(12));


    }
    public static int f(int n){
        if(n == 1 || n == 2){
            return 1;
        }
        return f(n-1) + f(n-2);
    }
}
