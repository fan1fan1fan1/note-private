package practice;

public class Person1 {
    // 属性
    String name;
    int age;
    double height;

    // 构造方法
    public Person1() {
    }
    // 有参构造
    public Person1(String name, int age, double height) {
        this.name = name;
        this.age = age;
        this.height = height;
    }
    // 方法
    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }
    public double getHeight() {
        return height;
    }
    public void setName(String name) {
        this.name = name;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public void setHeight(double height) {
        this.height = height;
    }

}
