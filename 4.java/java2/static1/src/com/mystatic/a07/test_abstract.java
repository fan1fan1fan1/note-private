package com.mystatic.a07;

public class test_abstract {
    public static void main(String[] args) {
        /* 抽象类
            学习面向对象中 我们继承后通过多态修改内容 在此之前父类首先有一个默认值
            但是这个默认值没有意义 我们可以把这个类变成抽象类 强制重写

            public abstract class Person{
                public abstract void eat();  # 在创建对象后 需要添加这个eat的内容
            }

            只要有一个抽象方法 这个类就必须是抽象类 类名前加abstract
            抽象类中不一定有抽象方法 但是有抽象方法的类一定是抽象类
            抽象类可以有构造方法 可以有普通方法
            抽象类不能实例化(不能创建对象) 只能用于继承 通过子类继承后重写抽象方法
            抽象类的子类要么是抽象类 要么重写抽象类中的所有抽象方法

            所有的项目不是只一个人写出来的 因此需要这种方法 强制子类必须按照这种流程书写
         */



        /* 1.抽象类父类
            public abstract class 父类{
                public abstract void eat();
                public abstract void sleep();

                可以有一般构造方法
            }

            2.子类
            public class 子类 extends 父类{
                子类自己的东西

                @Override 重写父类的东西
                public void eat(){
                    System.out.println("子类重写了父类的eat方法");
                }
                public void sleep(){
                    System.out.println("子类重写了父类的sleep方法");
                }
            }

            抽象类子类
            public abstract class 子类 extends 父类{
                子类自己的东西

                @Override 重写父类的东西 可以不重写 但是不能创建对象
                public void eat(){
                    System.out.println("子类重写了父类的eat方法");
                }
                public void sleep(){
                    System.out.println("子类重写了父类的sleep方法");
                }
            }

            3.测试类
            子类 子类对象 = new 子类();
            输出
         */



        /* 案例
            三种动物 都有吃的方法 但是吃的东西不一样
         */
        Frog frog = new Frog("小绿", 1);
        System.out.println(frog.getName() + " " + frog.getAge());
        frog.drink();
        frog.eat();
    }
}
