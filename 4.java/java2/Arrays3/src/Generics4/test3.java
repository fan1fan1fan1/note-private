package Generics4;

import java.util.ArrayList;

public class test3 {
    public static void main(String[] args){
        /* 泛型接口
            如何使用一个泛型接口
            1.实现类给出集体类型
            2.实现类延续泛型 创建对象时再确定
         */

        MyArrayList3 list = new MyArrayList3();
        // 此处接口里已经指定了String类型 因此测试类中不用再写



        /* 泛型不具备继承性 但是数据具备继承性

         */
        ArrayList<Ye> list1 = new ArrayList<>();
        ArrayList<Fu> list2 = new ArrayList<>();
        ArrayList<Zi> list3 = new ArrayList<>();

        list1.add(new Ye());
        list1.add(new Fu());
        list1.add(new Zi());

        method(list1);
        method(list2);
        method(list3);



        /* 泛型的通配符
            如果我们在定义类 方法 接口的时候 类型不确定 就可以定义泛型类 泛型方法 泛型接口
            如狗类型不确定 但是能知道以后只能拆掉你某个继承体系中的 就可以使用泛型通配符
                可以限定数据范围

         */


    }
    // 方法 接口

    /* 此时 泛型重写里面写的是什么类型 那么只能传递什么类型的数据
       弊端 利用泛型方法此时它可以接受任意数据类型 Ye Fu Zi Student

       如果我们希望这个方法只能被Ye Fu Zi使用
       引入泛型的通配符:
            ?: 表示不确定的类型 它可以进行类型的限定
            ? extends E: 表示可以传递E或E的子类
            ? super E:   表示可以传递E或E的父类
      */
    public static<E> void method(ArrayList<E> list){
    }

    // 加入通配符后
    public static void method1(ArrayList<? extends Ye> list1){}

    static class Ye {}
    static class Fu extends Ye {}
    static class Zi extends Fu {}


    public interface MyInterfacet<E>{

        int size();
    }

}

