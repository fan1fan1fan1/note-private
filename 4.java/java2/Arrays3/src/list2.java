import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

public class list2 {
    public static void main(String[] args) {
        /* 集合体系结构: Collection、Map
            Collection: List、Set

            List: 有序可重复有索引
                ArrayList
                LinkedList
                Vector

            List: 有序 存和取的元素顺序一致
                  可重复 可以通过索引操作元素
                  有索引 存储的元素可以重复

            List继承了Collection的方法

            特有方法:
             void add(int index, E element)  在指定索引位置添加元素
             E remove(int index)  删除指定索引位置的元素
             E get(int index)  获取指定索引位置的元素
             E set(int index, E element)  修改指定索引位置的元素
        */



        // 1.add
        List<String> list = new ArrayList<>();
        list.add("aaa");
        list.add("bbb");

        System.out.println(list);

        list.add(1, "ccc");  // 原来的元素依次往后移动
        System.out.println(list);


        // 2.remove
        String remove = list.remove(1);  // 删除指定索引位置的元素
        System.out.println(list);
        System.out.println(remove); // 返回被删除的元素
        // 再删除元素的时候 会优先调用实参和形参一致的方法7


        List<Integer> list2 = new ArrayList<>();
        list2.add(1);
        list2.add(2);
        list2.add(3);

        // 手动装箱 直接删除指定数据
        Integer I = Integer.valueOf(1);
        list2.remove(I);
        System.out.println(list2);


        // 3.set 修改
        String result = list.set(1, "ddd");
        System.out.println(list);
        System.out.println(result); // 返回被修改的元素


        // 4.get 获取
        String str = list.get(1);
        System.out.println(str);



        /* List集合的遍历方式
            1.迭代器遍历
            2.增强for遍历
            3.Lambda表达式遍历
            4.普通for遍历
            5.列表迭代器遍历
         */


        // 1.迭代器遍历
        Iterator<String> it = list.iterator();  // 获取迭代器对象
        while(it.hasNext()){
            String str1 = it.next();  // 从第一个索引开始 指到最后一个索引
            System.out.println(str1);
        }

        // 2.增强for遍历
        for (String s : list) {  // s中间变量 依次表示集合中的每一个元素
            System.out.println(s);
        }

        // 3.Lambda表达式遍历
        list.forEach(s -> System.out.println(s));

        // 4.普通for遍历
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }

        // 5.列表迭代器遍历

        /* 在迭代器的基础上 额外添加了一个方法 在遍历的过程中可以添加元素
            void add(E e)  在迭代器指向的元素之前添加元素

            ListIterator 列表迭代器接口 只能用于List集合
         */

        ListIterator<String> It = list.listIterator();
        while(It.hasNext()){
            String str1 = It.next(); // 迭代器格式

            if (str1.equals("bbb")){ // 添加元素的方法
                It.add("eee"); // 用迭代器方法添加元素
            }
            System.out.println(str1);
        }



        /* 1.ArrayList集合
            底层是数组结构
            利用空参创建的集合 在底层会创建一个空数组 size为0
            添加第一个元素时 底层会创建一个新的长度为10的数组elementData  size变成1

            size在此处有两层含义 1.元素个数
                              2.下次存入的位置

            当这个数组elementData存满时 会扩容1.5倍

            如果是一次添加了多个数据 1.5倍扩容后仍然放不下 会根据实际情况扩容超过数量+10个
         */



        /* 2.LinkedList集合
            底层是双链表结构 查询慢 增删快

            特殊方法 作用于首尾元素
            void addFirst(E e)  在链表的头添加元素
            void addLast(E e)  在链表的尾添加元素
            E getFirst()  获取链表的头元素
            E getLast()  获取链表的尾元素
            E removeFirst()  删除链表的头元素
            E removeLast()  删除链表的尾元素

            利用空参创建的集合 在底层会创建一个空链表
            添加第一个元素时 底层会创建一个新的节点 节点中存储了元素和地址值
            地址值指向null
         */
    }
}