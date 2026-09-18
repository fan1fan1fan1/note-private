package com.mystatic.a05;

public class test_duotai {
    public static void main(String[] args) {
        // 多态 同类型对象表现出的不同形态 对象的多种形态

        /* 简单介绍
            同一个父类 不同的子类 产生不同的对象

            Person p = new Person();

            Person p = new Student(); 多态
            父类 变量名 = new 子类;
        */


        /* 包含要素
            1.有继承 实现关系
            2.有父类 指向子类  fu f = new zi();
            3.有方法重写
         */


        /* 运行特点
            多态调用成员变量: 编译看左边 运行看左边
            多态调用成员方法: 编译看左边 运行看右边

            父类
            class Animal{}

            子类
            class dog extends Animal{}

            测试类
            Animal a = new dog()
            System.out.println(a.name);

            此处打印时
            成员变量调用等号左边 输出animal中成员变量
            成员方法调用等号右边 输出dog中成员方法 但编译看左边 即如果Animal中没有这个方法 不能输出

            在子类的对象中 会把父类的成员变量和成员方法继承过来
            先加载父类文件 再加载子类文件

            父类 a = new 子类()
            先加载父类文件 后加载子类文件 编译时先考虑父类文件

            子类 b = new 子类()
            先加载子类文件 如果子类文件中没有 再考虑父类文件 至Object

         */


        /* 多态优势
            优势 1.在多态形式下，右边对象可以实现解耦合，便于扩展和维护
                    Person p = new Student();
                    p.work();    当业务逻辑发生改变时 后续代码无需修改

                2.定义方法时，使用父类型作为参数，该方法就可以接收这父类的一切子类对象，体现出多态的扩展性与便利
         */


         /* 劣势 1.不能使用子类的特有成员
                2.不能使用子类的特有方法

                再运行某方法时会查看父类中是否有该方法 没有直接报错

            解决方法 1.向下转型 强转
                      子类 变量名 = (子类) 父类变量;
                      变量名.子类方法();

                      特殊情况 类型转换异常 需要转换的类型与变量的真实类型不一致
                              if(变量名 是不是 类名){
                                  子类 a = (子类) b;
                                  a.子类方法();
                                  变量名.子类方法();
                              }
                                       ⬇
                    2.使用instanceof关键字 判断对象是否是某个类的实例
                       格式: 对象 instanceof 类名
                       结果: 是 true  不是 false

                   新特性 对象 instanceof 类名 对象名
                          a  instanceof cat c
                         先判断a是否为cat类型 是就转换为c
         */



        // 综合练习
        /*
            定义狗类 包括年龄、颜色、行为(吃、看家)

            定义猫类 包括年龄、颜色、行为(吃、抓老鼠)

            定义饲养员 包括姓名、年龄(饲养狗、东西、饲养猫、东西)

            测试类
                打印:
                    年龄为30岁的老王养了一只黑颜色的2岁的狗
                    2岁的黑颜色的狗两只前腿死死的抱住骨头猛吃

                    年龄为25岁的老李养了一只灰颜色的3岁的猫
                    3岁的灰颜色的猫眯着眼睛侧着头吃鱼

           大类Animal 小类Dog Cat
           类person
         */



        /*
         定义狗类 包括年龄、颜色、行为(吃、看家)
        Dog d = new Dog("2","黑");
        System.out.println("年龄为30岁的老王养了一只" + d.getColor() + "颜色的" + d.getAge() + "岁的狗");
        d.eat("骨头");

         定义猫类 包括年龄、颜色、行为(吃、抓老鼠)
        Cat c = new Cat("3","灰");
        System.out.println("年龄为25岁的老李养了一只" + c.getColor() + "颜色的" + c.getAge() + "岁的猫");
        c.eat("鱼");

         定义饲养员 包括姓名、年龄(饲养狗、东西、饲养猫、东西)
        Person p = new Person("老王",30);
        p.keepPet(d,"骨头");
        p.keepPet(c,"鱼");
         */

        Person p = new Person("老王",30);
        Dog d = new Dog("2","黑");
        p.keepPet(d,"骨头");

        Person p2 = new Person("老李",25);
        Cat c = new Cat("3","灰");
        p2.keepPet(c,"鱼");



        // 通过多态优化
        Person p3 = new Person("老王",30);
        Dog d1 = new Dog("2","黑");
        p3.KeepPet(d1,"骨头");
    }
}
