package com.mystatic.a05;

public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }



    public void keepPet(Dog dog, String something) {
        System.out.println("年龄为" + age + "岁的" + name + "养了一只" + dog.getColor() + "岁的" + dog.getColor() + "颜色的狗");

        // 2岁的黑颜色的狗两只前腿死死的抱住骨头猛吃 调用Dog类中的eat方法
        dog.eat(something);
    }

    public void keepPet(Cat cat, String something) {
        System.out.println("年龄为" + age + "岁的" + name + "养了一只" + cat.getColor() + "岁的" + cat.getColor() + "颜色的猫");

        // 2岁的黑颜色的狗两只前腿死死的抱住骨头猛吃 调用Dog类中的eat方法
        cat.eat(something);
    }

    // 多态 优化 把猫和狗写在一起
    public void KeepPet(Animal a, String something) {
        // 判断a是猫还是狗

        if (a instanceof Cat c) {
            System.out.println("年龄为" + age + "岁的" + name + "养了一只" + c.getColor() + "岁的" + c.getColor() + "颜色的猫");

            // 2岁的黑颜色的狗两只前腿死死的抱住骨头猛吃 调用Dog类中的eat方法
            c.eat(something);
        }

        else if (a instanceof Dog d) {
            System.out.println("年龄为" + age + "岁的" + name + "养了一只" + d.getColor() + "岁的" + d.getColor() + "颜色的狗");

            // 2岁的黑颜色的狗两只前腿死死的抱住骨头猛吃 调用Dog类中的eat方法
            d.eat(something);
        }

        else {
            System.out.println("养的是其他动物");
        }


    }

}
