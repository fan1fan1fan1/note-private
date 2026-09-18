import java.util.ArrayList;

public class ArrayList10 {
    public static void main(String[] args) {
        // 长度可以发生变化 自动扩容
        // 集合可以存储基本数据类型和引用数据类型

        // 1.导包 import java.util.ArrayList;


        // 2.创建集合对象
        // 泛型：集合中存储的数据类型   <引用数据类型>
        ArrayList<String> list = new ArrayList<>();

        System.out.println(list);
        // 此处打印的是是属性值 不是地址值 结果输出时有[]


        // 3.添加元素
        boolean result = list.add("aaa");
        list.add("bbb");
        list.add("ccc");
        System.out.println(result);


        /* ArrayList集合常用方法 (增删改查)
            boolean add(E e) 将指定的元素添加到此列表的尾部。

            boolean remove(Object o) 从列表中移除指定元素的第一个出现（如果存在）。
            E remove(int index) 移除列表中指定位置的元素。

            E set(int index, E element) 用指定的元素替换列表中指定位置的元素。

            E get(int index) 返回列表中指定位置的元素。
            int size() 返回列表中的元素数。
         */


        // 4.删除元素一
        boolean result1 = list.remove("aaa");  // 如果要删除的元素不存在 就flase
        System.out.println(result1);


        // 5.删除元素二
        String remove = list.remove(1);
        System.out.println(remove);   // 删除0索引的数据 并返回该数据


        // 6.修改元素
        String set = list.set(0, "bbb");
        System.out.println(set);   // 修改0索引的数据


        // 7.查询元素
        String get = list.get(0);
        System.out.println(get);   // 查询0索引的数据


        // 8.获取集合长度
        int size = list.size();


        // 9.遍历集合
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }
    }
}