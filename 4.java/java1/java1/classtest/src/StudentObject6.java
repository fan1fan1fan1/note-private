public class StudentObject6 {
    // 属性
    private int id;
    private String name;
    private int age;

    // 空参
    public StudentObject6(){}

    // 全参
    public StudentObject6(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    // get
    public int getId() {
        return id;
    }
    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }

    // set
    public void setId(int id) {
        this.id = id;
    }
    public void setName(String name) {
        this.name = name;
    }
    public void setAge(int age) {
        this.age = age;
    }

    // 方法
}
