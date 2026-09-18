package com.mystatic.a04;

public class Extends {
    public static void main(String[] args) {
        /* 继承练习
            现在有四种动物
            布偶猫：吃饭、喝水、抓老鼠
            中国狸花猫：吃饭、喝水、抓老鼠
            哈士奇：吃饭、喝水、看家、  拆家
            泰迪：吃饭、喝水、看家、  蹭一蹭

            请用继承的思想，设计出四个类，并给出测试类，进行测试。
         */

        // 最大类
        class Animal{
            // 在类中写private 那么在其他类中则无法调用
            public void eat(){
                System.out.println("吃东西");
            }
            public void drink(){
                System.out.println("喝水");
            }
        }

        // 子类 猫类
        class cat extends Animal{
            public void catchMouse(){
                System.out.println("抓老鼠");
            }
        }

        // 子类 狗类
        class dog extends Animal{
            public void watchHouse(){
                System.out.println("看家");
            }
        }

        // 布偶猫
        class Buou extends cat{

        }
        // 中国狸花猫
        class ChineseCat extends cat{

        }
        // 哈士奇
        class Husky extends dog{
            public void breakHouse(){
                System.out.println("拆家");
            }
        }
        // 泰迪
        class Teddy extends dog{
            public void doDo(){
                System.out.println("蹭一蹭");
            }
        }

        // 测试类 创建对象
        Buou buou = new Buou();
        buou.eat();
        buou.drink();
        buou.catchMouse();
        System.out.println("----------------");
        // 此处还可以添加object类的方法

        ChineseCat chineseCat = new ChineseCat();
        chineseCat.eat();
        chineseCat.drink();
        chineseCat.catchMouse();
        System.out.println("----------------");

        Husky husky = new Husky();
        husky.eat();
        husky.drink();
        husky.watchHouse();
        husky.breakHouse();
        System.out.println("----------------");

        Teddy teddy = new Teddy();
        teddy.eat();
        teddy.drink();
        teddy.watchHouse();
        teddy.doDo();
        System.out.println("----------------");
    }
}
