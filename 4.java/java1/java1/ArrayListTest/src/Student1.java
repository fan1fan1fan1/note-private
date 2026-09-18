package ArrayListTest.src;

public class Student1 {
    // 自定义一个类 用于存放学生信息
    // 标准javabean类

    // 1.成员变量
    private String name;
    private int age;

    // 2.空参
    public Student1() {

    }

    // 3.全参
    public Student1(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // 4.get/set
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


}
