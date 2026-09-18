package com.mystatic.a07;

public class Frog extends Animal implements swim{
    // 青蛙类 会游泳 实现swim接口 定义时写上implements swim

    public Frog() {}
    public Frog(String name, int age) {
        super(name, age);
    }

    // 接口
    @Override
    public void swim(){
        System.out.println("青蛙会游泳");
    }

    @Override
    public void eat(){
        System.out.println("青蛙吃虫子");
    }
}
