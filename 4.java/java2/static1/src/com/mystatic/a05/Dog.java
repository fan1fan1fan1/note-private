package com.mystatic.a05;

public class Dog extends Animal{
    // 继承过父类的成员变量和成员方法 无需再次定义

    // 空参
    public Dog(){}

    // 全参
    public Dog(String age, String color){
        super(age, color);
    }

    // 重写父类的eat方法
    @Override
    public void eat(String something){
        // System.out.println("2岁的黑颜色的狗两只前腿死死的抱住骨头猛吃");
        System.out.println(getAge() + "岁的" + getColor() + "颜色的狗两只前腿死死的抱住" + something + "猛吃");
    }

    public void lookHome(){
        System.out.println("狗在看家");
    }
}
