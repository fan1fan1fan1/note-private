package com.mystatic.a07;

public class interface_implements {
    public static void main(String[] args) {
        /* 接口interface
            在父类写出一种方法后 有的子类不需要这个方法 有的子类需要这个方法 有的子类需要这个方法的一部分
            因此我们可以把这个方法变成接口 让子类实现这个接口 实现这个接口后 必须重写这个方法

            不是一种事物 是一种规则

            与抽象类不同
            接口是对行为的抽象

            public interface 接口名{
                抽象方法
            }

            接口不能实例化 不能创建对象

            接口和类是实现关系 通过implements关键字来实现 可以多个接口实现
            public class 类名 implements 接口名1,接口名2...{
                重写接口中的抽象方法
            }

            接口的子类(实现类) 要么重写接口中的所有抽象方法 要么是抽象类

            可以在继承的同时实现多个接口
            public class 类名 extends 父类名 implements 接口名1,接口名2...{
                重写接口中的抽象方法
            }
         */



        // 实例
        // 创建接口类时 不选择类 选择接口
        Frog frog = new Frog("小绿", 1);
        System.out.println(frog.getName() + " " + frog.getAge());
        frog.swim(); // 有接口的
        frog.eat();

        Sheep sheep = new Sheep("小蓝", 2);
        System.out.println(sheep.getName() + " " + sheep.getAge());
        sheep.eat(); // 没有接口的



        /* 接口中成员的特点
            成员变量
                只能是常量 且默认修饰符是public static final
                可以省略public static final
                常量名建议大写
            构造方法
                没有构造方法
            成员方法
                只能是抽象方法 且默认修饰符是public abstract
                可以省略public abstract
                方法名建议小写
            注意事项
                接口中没有静态代码块和构造代码块

            类和类是继承关系
            接口和类是实现关系 通过implements关键字来实现 可以多个接口实现
            接口和接口是继承关系 通过extends关键字来继承 可以多个接口继承
         */



        /* jdk8之后
            接口中可以有默认方法和静态方法
            默认方法
                public default 返回值类型 方法名(参数列表){
                    方法体
                }

                public default void eat(){
                    System.out.println("接口中的默认方法");
                }

                可以省略public 但defaultbushenglve
                    默认方法不需要重写 如果重写 重写时去掉default
                    如果实现了多个接口 有相同名字的默认方法 必须重写

            静态方法
                static修饰
                public static 返回值类型 方法名(参数列表){
                    方法体
                }

                public static void eat(){
                    System.out.println("接口中的静态方法");
                }

                可以省略public 但static不省略
                静态方法只能通过接口名调用 不能通过实现类对象调用
         */



        /* jdk9之后
            接口中可以有私有方法和私有静态方法
            私有方法
                private 返回值类型 方法名(参数列表){
                    方法体
                }
                private void eat(){
                    System.out.println("接口中的私有方法");
                }
                可以省略public 但private不省略
                私有方法只能在接口中调用 不能在实现类中调用
                私有方法可以被默认方法和静态方法调用

            私有静态方法
                private static 返回值类型 方法名(参数列表){
                    方法体
                }
                private static void eat(){
                    System.out.println("接口中的私有静态方法");
                }
                可以省略public 但private不省略
                私有静态方法只能在接口中调用 不能在实现类中调用
                私有静态方法可以被默认方法和静态方法调用
         */



        /* 接口的应用
            接口代表规则 是行为的抽象
            当一个方法的参数是接口类型时 可以传入接口的实现类对象 称为接口多态
         */


        /* 适配器模式
            当一个类实现了一个接口 但是这个类只需要使用接口中的一部分方法 可以使用适配器模式
            适配器模式是一种设计模式 用于解决接口的不兼容性问题

            举例
            包interAdapter interImpl
         */
    }
}
