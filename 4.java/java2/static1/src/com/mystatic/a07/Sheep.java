package com.mystatic.a07;

public class Sheep extends Animal{
    // 羊类 不会游泳 不用使用swim接口

    public Sheep() {}
    public Sheep(String name, int age) {
        super(name, age);
    }

    @Override
    public void eat(){
        System.out.println("山羊吃草");
    }
}
