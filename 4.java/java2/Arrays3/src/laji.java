import java.io.*;
import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

public class laji {
    public static void main(String[] args) throws IOException {
        // 1.创建学生对象
        Student2 stu = new Student2("z",23);

        // 2.创建序列化流的对象/对象操作输出流
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("D:\\22820\\Desktop\\code\\java\\a.txt"));

        // 3.写出数据 此处需要实现Serializable接口
        // Serializable接口里没有抽象方法 标记接口 一但实现了这个接口 就代表Student2类可以被序列化
        oos.writeObject(stu);

        // 4.释放
        oos.close();

        // 1.创建反序列化流对象
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("D:\\22820\\Desktop\\code\\java\\a.txt"));

        // 2.读取数据 此处需要抛出异常 强转

        Student2 o = (Student2)ois.readObject();

        // 3.打印对象
        System.out.println(o);

        // 4.释放资源
        ois.close();

    }

    }
