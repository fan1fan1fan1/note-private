package com.mystatic.a07;

public class Dog extends Animal implements swim{
    // 狗类 会游泳 实现swim接口 定义时写上implements swim

    public Dog() {}
    public Dog(String name, int age) {
        super(name, age);
    }

    @Override
    public void swim(){
        System.out.println("狗会游泳");
    }


    @Override
    public void eat(){
        System.out.println("狗吃骨头");
    }
}
