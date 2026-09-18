import java.util.ArrayList;
import java.util.Scanner;

public class studentSystem1 {
    public static void main(String[] args) {
        ArrayList<student1> list = new ArrayList<>();

        while (true) {
        System.out.println("-------欢迎来到学生管理系统-------");
        System.out.println("1.添加学生");
        System.out.println("2.删除学生");
        System.out.println("3.修改学生");
        System.out.println("4.查看所有学生");
        System.out.println("5.退出");
        System.out.println("请输入你的选择：");

        Scanner sc = new Scanner(System.in);
        String choice = sc.next();


        switch (choice) {
            case "1":
                addStudent(list);
                break;
            case "2":
                deleteStudent(list);
                break;
            case "3":
                updateStudent(list);
                break;
            case "4":
                queryStudent(list);
                break;
            case "5":
                System.out.println("退出");
                System.exit(0);  // 退出程序
            default:
                System.out.println("输入有误，请重新输入");
                break;
        }
        }

    }

    // 方法1 添加学生
    public static void addStudent(ArrayList<student1> list) {
        // 1.先创建一个空参构造
        student1 s = new student1();

        // 2.键盘录入学生信息
        Scanner sc = new Scanner(System.in);

        // 3.判断id是否唯一 如果已存在则不能输入 不存在则录入
        while (true) {
            System.out.println("请输入学生id：");
            String id = sc.next();
            boolean flag = contains(list, id); // 判断id是否存在
            if(flag){
                System.out.println("id已存在，请重新输入：");
                return;  // 结束方法
            }
            else{
                s.setId(id);
                break;
            }
        }

        // 4.录入学生其他信息
        System.out.println("请输入学生姓名：");
        String name = sc.next();
        s.setName(name);

        System.out.println("请输入学生年龄：");
        int age = sc.nextInt();
        s.setAge(age);

        System.out.println("请输入学生家庭住址：");
        String address = sc.next();
        s.setAddress(address);

        // 5.把学生对象添加到集合中
        list.add(s);

        System.out.println("添加学生成功");
    }



    // 方法2 删除学生
    public static void deleteStudent(ArrayList<student1> list){
        // 1.输入这个要删除的学生id
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入要删除的学生id：");
        String id = sc.next();

        // 2.判断id是否存在 通过id获取索引的方法
        int index = getIndex(list, id);
        if(index == -1){
            System.out.println("id不存在，请重新输入：");
            return;  // 结束方法
        }
        else{
            list.remove(index);
            System.out.println("删除学生成功");
        }
    }



    // 方法3 修改学生
    public static void updateStudent(ArrayList<student1> list){
        // 1.输入这个要修改的学生id
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入要修改的学生id：");
        String id = sc.next();

        // 2.判断id是否存在 通过id获取索引的方法
        int index = getIndex(list, id);
        if(index == -1){
            System.out.println("id不存在，请重新输入：");
            return;  // 结束方法
        }
        else{
            student1 s = list.get(index);

            // 3.修改学生信息
            System.out.println("请输入学生姓名：");
            String name = sc.next();
            s.setName(name);
            System.out.println("请输入学生年龄：");
            int age = sc.nextInt();
            s.setAge(age);
            System.out.println("请输入学生家庭住址：");
            String address = sc.next();
            s.setAddress(address);

            System.out.println("修改学生成功");
        }
    }



    // 方法4 查看所有学生
    public static void queryStudent(ArrayList<student1> list){
        if(list.size() == 0){
            System.out.println("无信息，请先添加信息再查询");
            return;  // 结束方法
        }
        else{
            System.out.println("学号\t\t姓名\t年龄\t家庭住址");
            for(int i = 0; i < list.size(); i++){
                student1 s = list.get(i);
                System.out.println(s.getId() + "\t" + s.getName() + "\t" + s.getAge() + "\t" + s.getAddress());
            }
        }
    }



    // 方法5 (用于方法1) 判断id是否存在 即判断添加的id是否唯一 如果已经存在则不能添加新学生id
    public static boolean contains(ArrayList<student1> list, String id){
        boolean flag = false;
        for(int i = 0; i < list.size(); i++){
            student1 s = list.get(i);
            if(s.getId().equals(id)){
                flag = true;  // 代表已经存在该id学生
                break;
            }
        }
        return flag;  // 不存在
    }



    // 方法6 (用于方法2) 通过id查找学生在集合中的索引
    public static int getIndex(ArrayList<student1> list, String id){
        int index = -1;  // 代表不存在

        for(int i = 0; i < list.size(); i++){
            student1 s = list.get(i);  // 获取到每一个学生对象
            if(s.getId().equals(id)){
                index = i;  // 代表这个要删除的数据存在 得到每一个学生对象的id
                break;
            }
        }
        return index;
    }
}
