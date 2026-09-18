package com.mystatic.a01;

public class StudentTest_static {
    public static void main(String[] args) {
        // 快捷键 psvm

        // static静态 java中的修饰符 可以修饰成员方法 成员变量 -> 静态变量 静态方法
        // 一旦使用static修饰成员方法 那么这就成为了静态方法 静态方法不属于对象 而是属于类的


        /* 静态变量特点
            被所有类对象共享 调用方法两种
             1.类名调用 推荐使用 类名(Student).静态变量名
             2.对象名调用 对象名(s1).静态变量名

            静态方法特点
            用在测试类 工具类中
            工具类 帮我们做一些事 但不描述任何事物的类
        */



        // JavaBean类 用于描述一类事物Student
        // 测试类 用于检查其他类是否书写正确 带有main方法的类 程序入口 在此创建javabean对象
        // 工具类 不是描述事物 而是做事情的类



        /* 静态方法只能访问静态变量和静态方法 不能访问非静态的成员变量和非静态的成员方法 (实例变量)
            非静态方法可以访问静态变量和静态方法，也可以访问非静态的成员变量和非静态的成员方法
            静态方法中是没有this关键字的

            this表示当前方法调用者的地址值
            这个this 是由虚拟机赋值的
        */




        // static静态变量赋值
        // 静态变量优先于对象存在 此时对象还未创建
        Student.teacherName = "a";

        // 创建类对象
        Student s1 = new Student();
        Student s2 = new Student();

        // 添加信息
        s1.setName("li");
        s1.setAge(18);
        s1.setGender("男");
        // s1.teacherName = "a"; 此处设置static静态 使老师变量赋值给所有成员 不用依次赋值

        s2.setName("si");
        s2.setAge(19);
        s2.setGender("女");

        // 调用方法
        s1.study();
        s1.show();

        s2.study();
        s2.show();




    }
}
