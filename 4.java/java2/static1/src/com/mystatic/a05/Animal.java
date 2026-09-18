package com.mystatic.a05;

public class Animal {
    private String age;
    private String color;

    public Animal(){}

    public Animal(String age, String color){
        this.age = age;
        this.color = color;
    }

    public String getAge(){
        return age;
    }
    public void setAge(String age){
        this.age = age;
    }
    public String getColor(){
        return color;
    }
    public void setColor(String color){
        this.color = color;
    }

    public void eat(String something){
        System.out.println("动物会吃" + something);
    }
}
