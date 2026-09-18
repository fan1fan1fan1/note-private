package com.mystatic.a03;

public class Student {
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
    public void setName(String name){
        this.name = name;
    }
    public int getAge(){
        return age;
    }
    public void setAge(int age){
        this.age = age;
    }
    public String getGender(){
        return gender;
    }
    public void setGender(String gender){
        this.gender = gender;
    }


}
