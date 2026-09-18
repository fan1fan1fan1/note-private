import java.io.Serial;
import java.io.Serializable;

public class Student2 implements Serializable {
    // 供 Methods2和IO5 相关使用

    // 此处实现了Serializabale接口 我们在此处固定一个版本号
    // private static final long seriaLVersionUID = 1L;
    @Serial
    private static final long serialVersionUID = 5684331859037303898L;

    // 不参与序列化的变量
    public transient String address;

    private String name;
    private int age;

    public Student2(){};

    public Student2(String name, int age) {
        this.name = name;
        this.age = age;
    }


    // 关键：接收String参数，解析“姓名,年龄”
    public Student2(String info) {
        String[] parts = info.split(",");
        // 关键：检查数组长度，确保至少有2个元素（姓名、年龄）
        if (parts.length >= 2) {
            this.name = parts[0];
            this.age = Integer.parseInt(parts[1]);
        } else {
            // 处理格式错误的情况（如默认值、抛异常等）
            this.name = parts[0]; // 至少有姓名
            this.age = 0; // 年龄设为默认值
            // 或抛异常：throw new IllegalArgumentException("格式错误：" + info);
        }
    }


    // 可选：getter/setter，方便后续操作
    public String getName() { return name; }
    public int getAge() { return age; }


    // setter 异常方法使用
    public void setAge(int age){
        if(age < 18 || age > 40){  // 报错 使用了抛出
            throw new NameFormatException3("年龄必须在 18 到 40 之间，当前年龄为：" + age);
            // throw new RuntimeException("年龄必须在 18 到 40 之间，当前年龄为：" + age); // 抛出
        }
        else{
            this.age = age;
        }
    }

    // setter 异常方法使用
    public void setName(String name) throws RuntimeException{
        int len = name.length();
        if(len < 3 || len > 10){ // 判断年龄长度是否超出
            throw new RuntimeException("姓名范围超出，当前姓名为"+name);
        }
        this.name = name;
    }

    @Override
    public String toString() {
        return "Student{name='" + name + "', age=" + age + "}";
    }
}

