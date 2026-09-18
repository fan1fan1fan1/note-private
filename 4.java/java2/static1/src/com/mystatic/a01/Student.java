package com.mystatic.a01;

public class Student {
    // 引入static
    // 现在要写一个student类 包含学生信息 行为为学习


    // 写完了上述要求后 现在我需要新增一个属性 表示老师的名称
    public static String teacherName;
    // static 静态 可以直接赋值给所有成员 不用依次赋值 表示所有学生共享这个变量


    // 属性
    private String name;
    private int age;
    private String gender;

    // 空参
    public Student(){

    }

    // 全参
    public Student(String name, int age, String gender){
        this.name = name;
        this.age = age;
        this.gender = gender;
    }

    // get set
    public String getName(){
        return name;
    }
    public int getAge(){
        return age;
    }
    public String getGender(){
        return gender;
    }

    public void setName(String name){
        this.name = name;
    }
    public void setAge(int age){
        this.age = age;
    }
    public void setGender(String gender){
        this.gender = gender;
    }

    // 行为
    public void study(){
        System.out.println(name + "正在学习");
    }

    public void show(){
            System.out.println(name + ", " + age + ", " + gender + ", " + teacherName);
    }
}
