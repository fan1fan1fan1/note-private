package com.mystatic.a08;

import com.mystatic.a05.Person;

public class test_innerclass {
    public static void main(String[] args) {
        /* 内部类
            类的五大成员: 属性(成员方法) 方法(行为) 构造方法(创建对象) 代码块 内部类

            内部类
                定义在一个类的内部 称为内部类
                class 外{
                    class 内{
                        可以使用外部类的所有成员 包括私有成员
                    }

                    不能在外部使用内部类的成员 必须创建对象
                }

            内部类表示的事物是外部类的一部分
            内部类单独存在时 没有意义

            内部类可以访问外部类的成员 包括私有成员
            外部类访问内部类的成员 必须创建内部类对象
         */



        /* 内部类的分类
            1. 成员内部类

            2. 静态内部类

            3. 局部内部类

            4. 匿名内部类***
         */



        /* 成员内部类
              外部类的成员 没有static修饰
                可以直接访问外部类的所有成员 包括私有成员
                外部类访问内部类的成员 必须创建内部类对象
                class Person{
                    ***

                    修饰词 class Student{
                        成员内部类
                    }
                }

               创建对象
                1. 在外部类中创建内部类对象
                    Person p = new Person();
                    Student s = p.new Student();

                2. 外部类名.内部类名 对象名 = new 外部类名().new 内部类名();
                Person.Student s = new Person().new Student();
                                   先创建外部对象  创建内部对象
         */

        // 成员内部类获取对象
        class Outer{
            private int num = 10;
            class Inner{
                private int num = 20;
                public void show(){
                    int num = 30;
                    System.out.println(num); // 30 就近原则
                    System.out.println(this.num); // 20
                    System.out.println(Outer.this.num); // 10
                }
            }
        }



        /* 静态内部类
             成员内部类的一种特殊情况

             外部类的成员 有static修饰

             只能访问外部类的静态成员、静态方法 包括私有静态成员
             访问非静态需要创建对象
             外部类访问内部类的成员 必须创建内部类对象

             class Person{
                 static class{
                     静态内部类

                     如果要引用外部类的非静态成员 必须创建外部类对象
                     Person p = new Person();
                 }
             }

             创建对象
              外部类名.内部类名 对象名 = new 外部类名.内部类名();
              Person.Student s = new Person.Student(); 此处new的是inner的静态对象(Student)

             调用
              外部类名.内部类名.方法名();
              Person.Student.show();
         */



        /* 局部内部类
            在外部类的方法中 没有static修饰 类似于方法里的局部变量
            可以直接访问外部类的所有成员 包括私有成员
            外部类访问内部类的成员 不能直接使用 必须在方法中创建内部类对象

            局部变量不能使用public private protected static修饰

            class Person大类{

                public void 方法(){
                    class Student{
                        局部内部类
                        可以直接使用外部类的所有成员 包括私有成员
                    }

                    创建对象
                    Student s = new Student();
                    s.局部内部类方法
                }

            }
         */



        /* 匿名内部类 (对象)
            没有名字的内部类

            适合创建对象 调用方法 重写方法 实现接口(继承)

            格式
                new 类名或接口名(参数列表){
                    重写方法
                }

                new:        创建一个对象 没有名字的对象
                类名或接口名: 实现了接口或继承
                {}:         匿名内部类中实际内容


            定义在外部类的方法中 没有static修饰
            可以直接访问外部类的所有成员 包括私有成员
            外部类访问内部类的成员 必须在方法中创建内部类对象
            匿名内部类只能使用一次
            匿名内部类的本质是一个继承了该类或者实现了该接口的子类匿名对象

         */

        // 接口多态
        Swim s = new Swim() {
            // 创建了一个没有名字的类 这个类把已有的Swim接口给实现了

            // ⬇ 这个类自身的内容 + Swim接口
            @Override
            public void swim() {
                System.out.println("重写了Swim的方法");
            }
        };
        s.swim(); // 编译看左边 运行看右边

        new Swim() {
            @Override
            public void swim() {
                System.out.println("重写了Swim的方法");
            }
        }.swim();

    }
    // public static void method(){}

}
