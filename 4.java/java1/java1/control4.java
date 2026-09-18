import java.util.Scanner;

public class control4 {
    public static void main(String[] args){
        boolean flag = true;
        if(flag){
            System.out.println(1);
        }
        else{
            System.out.println(0);
        }



        /* if else if案例
            电影院选票 票数1-100 奇数票坐左边 偶数票坐右边
            要求输入一个票数 查看坐的位置
         */
        Scanner sc = new Scanner(System.in);
        System.out.println("请录入一个票号");
        int ticket = sc.nextInt();


        if(ticket < 0 || ticket > 100){
            System.out.println("非法数据");
        }
        else if(ticket % 2 == 0){
            System.out.println("坐左边");
        }
        else{
            System.out.println("坐右边");
        }



        /* switch语句
            switch(表达式){
                case 常量1:
                    语句1;
                    break;

                case 常量2:
                    语句2;
                    break;

                case 常量3:
                    语句3;
                    break;
                default:
                    语句4;
                    break;
            }
         */
        String noodles = "兰州拉面";
        switch (noodles){
            case "兰州拉面":
                System.out.println("吃兰州拉面");
                break;
            case "武汉热干面":
                System.out.println("吃武汉热干面");
                break;
            case "北京炸酱面":
                System.out.println("吃北京炸酱面");
                break;
            case "陕西油泼面":
                System.out.println("吃陕西油泼面");
                break;
            default:
                System.out.println("吃泡面");
                break;
        }
        // 如果多个case穿透 可以不写break简化代码


        int numbers = 1;
        switch(numbers) {
            case 1 -> {
                System.out.println("一");  // 只有一行 {}可以省略
            }
            case 2 -> System.out.println("二");
            default -> System.out.println("没有这种选项");
        }


        // for循环
        for(int i = 1; i <= 5; i++){
            System.out.println(i);
        }


        int sum = 0;
        for(int i=1; i <= 5; i++){
            System.out.println(i);
            sum += i;  //求和
        }
        // System.out.println(sum);



        // while循环
        int i = 1;
        while(i <= 5){
            System.out.println(i);
            i++;
        }



        // 案例一 数字交换位置 判断回文数121
        int x = 121;         // 用于最后的比较
        int temp = x;        // 用于记录比较时最后得到的交换数字
        int num = 0;         // 交换后的数字
        while(x != 0){
            int ge = x % 10; // 取个位数
            x = x / 10;      // 改变原来的数
            num = num * 10 + ge; // 个位上数放到新的num里
        }
        System.out.println(num);
        System.out.println(x);
        System.out.println(num == temp);  // 判断是否为回文数



        // 案例二 两数相减 不能用乘法 除法 取模
        int a = 100; // 被除数
        int b = 10;  // 除数
        int count = 0; // 记录相减的次数
        while(a >= b){
            a -= b;
            count++;
        }
        System.out.println(a);



        /* 无限循环
        for(;;){
            System.out.println("无限循环");
        }

        while(true){
            System.out.println("无限循环");
        }

        do {
            System.out.println("无限循环");
        }while(true);

        跳转控制循环 continue break
        1. continue 跳过本次循环 继续下次循环
        2. break 终止循环
        */



        /* 增强for循环
            格式
            for(元素类型 元素变量 : 数组或集合){
                循环体语句;
            }
         */
        int[] arr = {1,2,3,4,5};
        for(int I : arr){
            System.out.println(I);
        }
    }
}
