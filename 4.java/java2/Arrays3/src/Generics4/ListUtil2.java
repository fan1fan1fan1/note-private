package Generics4;

import java.util.ArrayList;

public class ListUtil2 {
    // private关键字后可以时修饰方法的 用于将该方法声明为私有方法
    private ListUtil2(){}


    // 类中定义一个静态方法addAll 用来添加多个集合元素
    // 参数一 集合   参数二 要添加的元素
    public static<E> void addAll(ArrayList<E> list, E e1, E e2, E e3, E e4){
        // e1 e2 e3 e4是需要被添加的元素

        list.add(e1);
        list.add(e2);
        list.add(e3);
        list.add(e4);
    }



    // 上述方法缺陷 需要在class中指定需要添加的元素个数

    // 不需要确定元素个数方法 "..."
    public static<E> void addAll(ArrayList<E> list, E...e){
        // "..."可变参数 不需要提前确定要添加的元素个数

        for(E element : e){
            list.add(element);
        }
    }




    public void show(){ System.out.println("a");}
}
