package ArrayListTest.src;

import java.util.ArrayList;

public class ArrayListTest1 {
    public static void main(String[] args) {
        // 练习一 定义一个集合 添加字符串 并进行遍历 遍历格式[元素1, 元素2, 元素3, ...]
        // 1.创建集合对象
        ArrayList<String> list1 = new ArrayList<>();
        // 2.添加元素
        list1.add("aaa");
        list1.add("bbb");

        // 3.遍历集合
        System.out.print("[");
        for (int i = 0; i < list1.size(); i++) {
            if (i == list1.size() - 1) {
                System.out.println(list1.get(i) + "]");
            } else {
                System.out.print(list1.get(i) + ", ");
            }
        }



        // 练习二 定义一个集合 添加数字 并进行遍历 遍历格式[元素1, 元素2, 元素3,...]
        // 1.创建集合对象
        ArrayList<Integer> list2 = new ArrayList<>();

        /* 基本数据类型包装类
            byte Byte
            short Short
            int Integer **
            long Long
            float Float
            double Double
            char Character **
            boolean Boolean
         */

        // 2.添加元素
        list2.add(1);
        list2.add(2);
        list2.add(3);

        // 3.遍历集合
        System.out.print("[");
        for (int i = 0; i < list2.size(); i++) {
            if (i == list2.size() - 1) {
                System.out.println(list2.get(i) + "]");
            } else {
                System.out.print(list2.get(i) + ", ");
            }
        }



        // 练习三 定义一个集合 添加学生对象 并进行遍历 遍历格式[元素1, 元素2, 元素3,...]
        // 1.创建集合对象
        ArrayList<Student1> list3 = new ArrayList<>();

        // 2.创建学生对象
        Student1 s1 = new Student1("张三", 18);
        Student1 s2 = new Student1("李四", 19);

        // 3.添加元素
        list3.add(s1);
        list3.add(s2);

        // 4.遍历集合
        System.out.print("[");
        for (int i = 0; i < list3.size(); i++) {
            Student1 stu = list3.get(i);
            System.out.print(stu.getName() + ", " + stu.getAge());
        }
        System.out.println("]");
    }
}
