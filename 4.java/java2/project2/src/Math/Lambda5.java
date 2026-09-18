package Math;

import java.util.Arrays;
import java.util.Comparator;

public class Lambda5 {
    public static void main(String[] args) {
        /* Lambda表达式 简化函数式接口的匿名内部类书写

            ()-> {

             }

           ()里面是形参  {}方法体
         */


        /* 函数式编程 Functional Programming
            1.将计算视为数学函数的求值，忽略面向对象的复杂语法，强调做什么而不是谁去做，避免使用可变状态和可变数据。
            2.将计算过程分解为一系列简单的函数，每个函数都有一个明确的输入和输出，并且不依赖于外部状态。
            3.可以将函数作为参数传递给其他函数，也可以将函数作为返回值。
            4.使代码更加简洁、易读、易维护，更好利用多核处理器的并行计算能力。

            函数式接口: 有且只有一个抽象方法的接口 用@Functionallnterface注解
         */



        Integer[] arr4 = {26, 45, 61, 52, 38, 95, 81};

        Arrays.sort(arr4, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1 - o2;
            }
        });

        // 使用Lambda表达式
        Arrays.sort(arr4, (o1, o2) -> {
            return o1 - o2;
        });
        System.out.println(Arrays.toString(arr4));



        // 利用内部类调用swin方法
        /* 调用一个方法的时候 如果方法的形参是一个接口 那么我们要传递这个接口的实现类对象
            如果实现类对象只用到一次 可以时用匿名内部类书写 Lambda
         */
        method1(new Swim() {
            @Override
            public void swim() {
                System.out.println("swim");
            }
        });

        // 利用Lambda表达式调用swin方法
        // 要求method1传递的必须是一个接口interface 不能是一个抽象类
        method1(() -> {
            System.out.println("swim");
        });



        /* Lambda的进一步省略
            可推导可省略
            要求接口中有且只有一个函数体
            1.() 可以省略
            2.{} 可以省略
            3.如果只有一个参数 那么() 可以省略
            4.如果只有一个语句 那么{} 可以省略
            5.参数类型可以不写
            6.如果Lambda表达式的方法体只有一行 () ; return 可以省略不写 且需要同时省略

            名字.方法(对象, 形参) -> 函数体
         */
        method1(() -> System.out.println("swim"));



        /* 练习 定义一个数组存储字符串 用Arrays的sort方法进行排序
            要求 按照字符串的长度进行排序 短的在前面 长的在后面
         */
        String[] arr = {"a", "aa", "aaa", "aaaa"};

        Arrays.sort(arr, (o1, o2) -> o1.length() - o2.length());

        System.out.println(Arrays.toString(arr));


    }
    // 方法
    public static void method1(Swim s){
        s.swim();
    }

}

// 接口
// 函数式接口 使用注解
@FunctionalInterface
interface Swim{
    public abstract void swim();
}



