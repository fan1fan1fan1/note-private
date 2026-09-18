package Generics4;

import java.util.ArrayList;

public class test2 {
    public static void main(String[] args){
        /* 泛型方法
            方法中形参类型不确定时 可以使用类名后面定义泛型<E>

            两种使用方法
            1.使用类名后面定义的泛型 (所有方法都能用)
            2.在方法申明上定义自己的泛型 (只有本方法可用)
         */

        // 案例 定义一个工具类ListUtil
        ArrayList<String> list = new ArrayList<>();

        ListUtil2.addAll(list, "a","b","c","d");

        System.out.println(list);


    }

    // 方法
    Object[] obj1 = new Object[10];
    int size1;

    public<E> boolean add(E e){
        // 调用该方法时 E就确定类型

        obj1[size1] = e;
        size1++;
        return true;
    }
}
