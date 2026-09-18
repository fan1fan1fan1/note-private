package com.mystatic.a04;

public class test_extends {
    public static void main(String[] args) {
    // 面向对象三大特征 封装继承多态
    /* 封装: 对象代表什么 就得封装对应的数据 并提供数据对应的行为
        创建一个对象 对象包括属性和行为 我们可以直接引用对象(封装) 节省空间时间
        当两个封装的对象属性和方法相同时 我们不需要再写一遍属性和行为 引用上一个封装内数据(继承)  节省空间时间
        当有某些数据需要改变某属性行为时 多态

        继承 extends 当类与类之间存在共性内容 并满足子类是父类中的一种 就可以考虑使用继承来优化代码

        java只支持单继承 不支持多继承 但支持多层继承
        (一个儿子只能有一个父亲 但一个父亲可以有多个儿子
        父亲可以当儿子 但是不能当儿子的儿子
        父亲(直接父类)的父亲(间接父类)可以给儿子调用 跨级调用)

        最大的祖宗类Object
        每一个类都可以直接或间接的继承于Object类

        public class A {}
        没指示A继承什么类 那么A会默认继承object类
    */



    // 继承
    // 子类 extends 父类  public class Student extends Person {}

    /* 成员变量 成员方法 构造方法
        子类不能继承父类的构造方法
        子类可以继承父类的成员变量和成员方法
        子类不能继承父类的私有成员变量和成员方法
     */


    /* 虚方法表
        当子类的某对象在所有类中寻找方法时使用
        从最高一级父类开始寻找
        并递交给自己的子类 子类可以添加新的虚方法 然后再递交给子类
        只有虚方法可以继承

        包括一些经常需要的方法:
            非private 非私有    public可以继承
            非static 非静态
            非final
     */



    /* 继承特点
        1.成员变量的访问特点: 就近原则 谁近用谁: 输出语句System出现时 输出内容为从该句向上最近的语句
        public class Fu{
            String name = "Fu";
        }
        public class Zi extends Fu{
            String name = "Zi";
            public void ziShow(){
                String name = "ziShow";
                System.out.println(name);        -> ziShow 最近的
                System.out.println(this.name);   -> Zi     最近的本位上
                System.out.println(super.name);  -> Fu     super调用父类
            }
        }
        */


        // 2.成员方法的访问特点: 就近原则 谁近用谁 用法同上

        // 父类
        class Person{
            public void eat(){
                System.out.println("吃米饭，吃菜");
            }
            public void drink(){
                System.out.println("喝开水");
            }
        }

        // 子类
        class OverseasStudent extends Person{
            public void lunch(){
                this.eat();   // 吃意大利面 喝凉水 就近原则 子类本身的语句更近
                this.drink();

                super.eat();  // 吃米饭吃菜 喝开水 父类
                super.drink();
            }

            // 方法重写 当子类的方法不能满足子类现在的需求时 需要进行方法重写
            @Override
            public void eat(){
                System.out.println("吃意大利面");
            }
            @Override
            public void drink(){
                System.out.println("喝凉水");
            }
        }

        // 子类
        class Student extends Person{            // 子类
            public void lunch(){
                this.eat();      // super.eat();
                this.drink();    // super.drink();
            }
        }
        Student s = new Student();
        s.lunch();
        OverseasStudent os = new OverseasStudent();
        os.lunch();   // 重写


        /* 方法重写
            当父类的方法不能满足子类现在的需求时 需要进行方法重写
            书写格式: 在继承体系中 子类出现了和父类中一模一样的方法声明 重写
            @Override 注解  可以检测是否为重写 写在重写后的方法上

            解释:
            父类方法添加到虚方法表中
            子类重写后的方法添加到虚方法表中 修改了父类方法 进行覆盖
            子类调用时 没有调用原虚方法表中方法 调用了覆盖后的方法 即重写方法

            注意事项: 重写的方法尽量和父类保持一致
            1.重写方法的名称、形参列表必须与父类中的一致
            2.子类重写的方法的权限修饰符必须大于或等于父类中的权限修饰符
            3.子类重写的方法的返回值类型必须是父类中的返回值类型或其子类型
            4.私有方法不能重写 静态方法不能重写 构造方法不能重写
            5.只有被添加到虚方法表中的方法才能被重写*****
        */



        // 3.构造方法的访问特点
        /* 子类构造方法的访问特点:
            父类的构造方法不会继承给子类 但会被调用
            子类所有的构造方法默认都会访问父类中无参构造方法
            子类构造方法的第一行默认都是super() 不写也存在
            子类构造可以通过super关键字来调用父类重载构造
            子类在初始化时 一定会先初始化父类
         */

        /* 1.父类
            class Person{
                String name;    属性
                int age;

                public Person(){
                    System.out.println("父类的无参构造");
                }
            }

            2.子类
            class Student extends Person{
                public Student(){
                    super();
                    System.out.println("子类的无参构造");
                }

                public Student(String name, int age){
                    super(name,age);  调用父类带参构造
                    System.out.println("子类的有参构造");
            }

            3.测试类
            Student s = new Student(name,age);
            先调用父类的无参构造
            再调用子类的无参构造
         */



        /* 标准javabean
            1.所有的成员变量都要使用private关键字修饰
            2.为每一个成员变量编写一对getter和setter方法
            3.编写一个无参构造方法
            4.编写一个全参构造方法
            5.类名见字如意

            继承父类javabean时 需要在子类中写父类的无参构造方法
         */
    }
}

