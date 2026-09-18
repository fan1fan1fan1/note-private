package com.mystatic.a03;

import java.util.ArrayList;

public class Test {
    public static void main(String[] args) {
        // 定义集合
        ArrayList<Student> list = new ArrayList<>();

        // 创建对象
        Student s1 = new Student("zhangsan", 20, "男");
        Student s2 = new Student("lisi", 21, "女");
        Student s3 = new Student("wangwu", 22, "男");

        // 添加到集合
        list.add(s1);
        list.add(s2);
        list.add(s3);

        // 调用工具类
        int max = StudentUtil.getMaxAge(list);
        System.out.println(max);

    }
}
