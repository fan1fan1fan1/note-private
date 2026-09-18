package Generics4;

import java.util.ArrayList;
import java.util.Iterator;

public class Generics4 {
    public static void main(String[] args) {
        /* 泛型
            是一种参数化类型 可以在定义类、接口、方法时使用
            在编译阶段约束操作的数据类型 并进行检查

            格式: <类型>
            类型可以是类 接口 枚举 基本数据类型
            只能使用引用数据类型 基本类型包装类

            作用: 1.提高代码的安全性
                 2.避免类型转换异常

            分类: 1.泛型类
                 2.泛型接口
                 3.泛型方法

            java中的泛型是伪泛型 只在编译时期有效
            泛型的擦除: 在java文件中存在 class文件中不存在

            泛型不能写基本类型 泛型可以写某类型的子类 不写泛型默认Object类
         */



        // 1.创建对象 此处不指定类型
        ArrayList list = new ArrayList<>();

        // 2.添加元素
        list.add("a");
        list.add("b");
        list.add(new Student("c", 1));

        // 3.遍历集合 获取每一个元素
        Iterator it = list.iterator();
        while(it.hasNext()){
            /*
            str.length();   此处string强转数据类型会报错 因为arraylist里有数据 有自己的类型
            System.out.println(str);
             */
        }

        /* 如果我们没有给集合指定类型 默认为Object类型
           此时可以添加任意数据类型 但无法使用其行为
            因此推出了泛型 添加数据时把类型进行统一
         */
        ArrayList<String> list1 = new ArrayList<>();
        list.add("aaa");

        Iterator<String> it1 = list.iterator();
        while(it.hasNext()){
            String str = it1.next();
            System.out.println(str);
        }



    }

    // 方法
    static class Student{
        private String name;
        private int age;

        public Student() {
        }

        public Student(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public String getName() {
            return name;
        }

        public int getAge() {
            return age;
        }

        public void setName(String name) {
            this.name = name;
        }

        public void setAge(int age) {
            this.age = age;
        }
    }
}
