package com.mystatic.a04;


public class override {
    public static void main(String[] args) {
        /* 利用方法重写设计继承结构
            现在有三种动物 哈士奇、沙皮狗、中华田园犬
            哈士奇    吃饭(吃狗粮)      喝水 看家 拆家
            沙皮狗    吃饭(吃狗粮、骨头) 喝水 看家
            中华田园犬 吃饭(吃剩饭)      喝水 看家

            父类: 吃饭(吃狗粮) 喝水 看家
            子类: 哈士奇 加一个拆家
                 沙皮狗 重写吃饭
                 中华田园犬 重写吃饭
         */

        // 父类
        class Dog {
            public void eat() {
                System.out.println("吃狗粮");
            }
            public void drink() {
                System.out.println("喝水");
            }
            public void lookHome() {
                System.out.println("看家");
            }
        }

        // 哈士奇
        class Husky extends Dog {
            public void breakHome() {
                System.out.println("拆家");
            }
        }

        // 沙皮狗
        class ShibaInu extends Dog {
            @Override
            public void eat() {
                // 吃饭 两种写法
                // 1. System.out.println("吃狗粮");
                super.eat();   // 吃狗粮

                System.out.println("吃骨头");
            }
        }

        // 中华田园犬
        class ChineseDog extends Dog {
            @Override
            public void eat() {
                System.out.println("吃剩饭");
            }
        }

        // 测试
        Husky h = new Husky();
        h.eat();
        h.drink();
        h.lookHome();
        h.breakHome();

        ShibaInu s = new ShibaInu();
        s.eat();
        s.drink();
        s.lookHome();
    }
}
