import java.util.ArrayList;
import java.util.Scanner;

public class ArrayListTest2 {
    public static void main(String[] args) {
        // 练习四 定义一个集合 键盘录入学生信息
        // 1.创建集合
        ArrayList<Student1> list1 = new ArrayList<>(); // 此时集合长度为0

        // 2.创建键盘录入对象
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 3; i++) {  // i<3表示我要在集合中录入三个元素
            Student1 s = new Student1();  // 不能放在循环外面

            System.out.println("请输入学生的姓名");
            String name = sc.next();
            s.setName(name);

            System.out.println("请输入学生的年龄");
            int age = sc.nextInt();
            s.setAge(age);

            // 把学生对象添加到集合中
            list1.add(s);
        }

        System.out.println(list1.size());   // 集合长度 元素个数 3

        // 3.遍历集合
        for (int i = 0; i < list1.size(); i++) {
            Student1 s = list1.get(i);
            System.out.println(s.getName() + "," + s.getAge());
        }



        // 练习五 添加用户对象 并判断是否存在
        /* 需求
            main定义一个集合 存入三个用户对象
            属性: id username password

            定义一个方法 根据id查找对应的用户信息

            如果存在 返回true
            如果不存在 返回false
         */

        // 1.创建集合
        ArrayList<User2> list2 = new ArrayList<>();

        // 2.创建对象
        User2 u1 = new User2("001", "zhangsan", "123456");
        User2 u2 = new User2("002", "lisi", "123456");
        User2 u3 = new User2("003", "wangwu", "123456");

        // 3.把对象添加到集合中
        list2.add(u1);
        list2.add(u2);
        list2.add(u3);

        // 4.调用方法
        boolean flag = getUer(list2, "001");
        System.out.println(flag);



        // 练习六 添加手机对象并返回要求的数据
        /* 需求
            定义javabean类 Phone
            属性: brand price

            main定义一个集合 存入三个手机对象
            分别为: 小米 1000 苹果 8000 锤子 2999

            定义方法 将价格低于3000的手机信息返回
         */

        // 1.创建集合
        ArrayList<Phone2> list3 = new ArrayList<>();

        // 2.创建对象
        Phone2 p1 = new Phone2("小米", 1000);
        Phone2 p2 = new Phone2("苹果", 8000);
        Phone2 p3 = new Phone2("锤子", 2999);

        // 3.把对象添加到集合中
        list3.add(p1);
        list3.add(p2);
        list3.add(p3);

        // 4.调用方法
        ArrayList<Phone2> phoneList = getPhone(list3);

        // 5.遍历集合
        for (int i = 0; i < phoneList.size(); i++) {
            Phone2 p = phoneList.get(i);
            System.out.println(p.getBrand() + "," + p.getPrice());
        }







    }

    // 定义方法 根据id查找对应的用户信息
    public static boolean getUer(ArrayList<User2> list, String id) {
        // 遍历集合
        for (int i = 0; i < list.size(); i++) {
            User2 u = list.get(i);
            if (u.getId().equals(id)) {  // 判断id是否相等
                return true;
            }
        }
        return false;
    }



    // 定义方法 将价格低于3000的手机信息返回
    public static ArrayList<Phone2> getPhone(ArrayList<Phone2> list) {
        ArrayList<Phone2> resultList= new ArrayList<>(); // 用于存储结果的集合

        // 遍历集合
        for (int i = 0; i < list.size(); i++) {
            Phone2 p = list.get(i);
            if (p.getPrice() < 3000) {
                // System.out.println(p.getBrand() + "," + p.getPrice());
                resultList.add(p);
            }
        }

        // 需要返回多个参数时 可以先把这些数据放在一个容器里 再把容器返回
        return resultList;
    }
}
