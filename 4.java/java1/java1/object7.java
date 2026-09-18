public class object7 {
    public static void main(String[] args) {
        // 先设计类 在创建对象
        /* 定义一个类
             public class 类名 {
             成员变量 属性 名词
             成员方法 行为 动词
             构造器   构造方法 构造器 一般是初始化
             代码块   一般是初始化
             内部类   一般是内部类 一般是内部类
            }

            用来描述一类事物的类 专业叫 javabean类 这种类不写main方法
            通常我们写的类 是编写main方法的类 叫测试类
            我们也可以在测试类中创建javabean类的对象

            类名首字母建议大写 驼峰命名法 见名知意
            一个java文件中 可以定义多个类 但是只能有一个public类 且public类的名称必须和java文件的名称相同
            建议在实际开发中之定义一个class类

            成员变量的完整格式: 修饰符 数据类型 变量名 = 初始化值;
            且一般不用给初始化值 因为有默认值
         */



        // 2.创建对象
        object7 gobject = new object7();
        Student s = gobject.new Student();

        object7 gobject2 = new object7();
        Student s2 = gobject2.new Student();

        object7 gobject3 = new object7();
        Student s3 = gobject3.new Student();

        /* 此处定义初始化对象有默认值
            byte short int long -> 0
            float double -> 0.0
            char -> '\u0000'
            boolean -> false
            引用类型(类 接口 数组 String) -> null
         */



        // 3.访问成员变量和成员方法
        s.name = "张三";
        System.out.println(s.name);
        s.study();



        /* 封装 private关键字
            对象代表什么 就封装对应的数据 并提供对应的方法
            比如人画圆 画圆这个操作就应该放在圆对象里 因为圆是自己画的 而人只是调用了画圆的方法

            比如人关门 关门这个操作就应该放在门对象里 因为门是自己关门的 而人只是调用了关门的方法
         */



        /* private 权限修饰符 可以用来修饰成员变量和成员方法
            被private修饰的成员只能在本类中访问 其他类中不能访问
            一般我们会把成员变量用private修饰 提供对应的get和set方法来访问
         */
        GirlFriend gf1 = gobject.new GirlFriend();
        gf1.age = 18;
        System.out.println(gf1.age);
        gf1.eat();



        // this关键字 就近原则 防止重定义
        /* this关键字 代表当前对象 可以用来访问成员变量和成员方法
            1.this.成员变量 访问成员变量
            2.this.成员方法 访问成员方法
            3.this() 访问构造方法
            4.this 代表当前对象 可以用来访问成员变量和成员方法

            this的作用: 区分局部变量和成员变量
            this的本质: 所在方法调用者的地址值
         */
        Person p = gobject.new Person();
        p.setAge();



        // 4.构造器
        /* 构造器 也叫构造方法 构造器 一般是初始化 初始化对象 给定初始值

            构造器的格式:
                修饰符 类名(参数列表) {
                    构造器体
                }

            构造器的修饰符可以省略 默认为public
            构造器的名称必须和类名相同
            构造器没有返回值 也不能写void 不能写return

            构造器可以重载
            带参构造方法 和无带参构造方法 两者方法名相同 但是参数不同 重载
            无论是否使用 尽可能都定义带参和不带参

            构造器可以在一个类中定义多个 但是只能有一个public构造器
            如果没有定义构造器 系统会提供一个无参构造器 但是如果定义了构造器 系统就不会提供无参构造器
            构造器的作用是初始化对象 给对象的成员变量赋初始值

            构造器不能手动调用 由虚拟机自动调用
         */
        Person2 p2 = gobject.new Person2();
        System.out.println(p2.name);
        System.out.println(p2.age);



        // 标准javabean类
        /*
            1.类名需要见名知意
            2.成员变量使用private修饰
            3.提供两种构造方式 无论是否使用都写上
            4.成员方法写 set get
         */



        /* java使用标准javabean的内存图流程
            1.加载class文件
            2.申明局部变量
            3.在堆内存中开辟一个空间
            4.默认初始化
            5.显式初始化
            6.构造方法初始化
            7.将堆内存中的地址值赋值给左边的局部变量
         */



        /* 引用数据类型
            1.定义一个类中 Student s = new Student()
                其中s为一个引用数据类型 我们会在这个类下定义name age等 而s只是引用了这些属性 记录了它们的地址 因此为引用类型

            2.定义一个数组  int[] arr = {1, 2, 3, 4}
                arr为一个数组 记录了数组里数据的地址值 通过索引获取数据 arr为引用数据类型

            基本数据类型 数据值存储在自己的空间中 赋值给其他变量 赋的是真实的值
            引用数据类型 数据值存储在其他空间 自己空间中只存储地址值

            Student s1 = new Student();
            Student s2 = s1;
            当改变s1或s2中的其中一个 另一个也随之改变
         */


        // 局部变量和成员变量 区别是写在某函数里或者在最外层 所有函数都能用

        // 占位符%s

    }



    // 1.定义一个类
    public class Student {

        String name; // 成员变量 定义需要的名称
        String id;
        char gender;
        int age;

        public void study() { // 成员方法
            System.out.println("studying...");
        }
    }



    // 人关门 门的类
    public class Door {
        boolean flag = true;  // 们的状态数据

        public void close() {
            System.out.println("关门");
        }

        public void open() {
            System.out.println("开门");
        }
    }



    // 使用了private关键字的例子
    public class GirlFriend {
        private String name;
        private int age;
        private char gender;


        // 由于定义了private关键字 所以只能在本类中访问
        // 对每一个private变量提供对应的get和set方法来访问

        // 1.set赋值
        public void setAge(int a) {
            if(a >=18 && a <= 50) {
                age = a;
            }
            else {
                System.out.println("年龄不合法");
            }
        }

        // 2.get获取
        public int getAge(){
            return age;
        }


        // 行为
        public void eat() {
            System.out.println("吃");
        }
    }



    // this关键字的例子
    public class Person {
        private int age;
        public void setAge() {
            int age = 10;   // this.age = 10;
            System.out.println(this.age);
        }

        /*
        public void method(){
            int age = 10;
            System.out.println(age);      // 10
            System.out.println(this.age); // 0
        }
         */
    }



    // 构造器的例子
    public class Person2 {
        String name;
        int age;


        // 构造
        public Person2() {
            System.out.println("无参构造器");
        }

        public Person2(String name, int age) {
            this.name = name;
            this.age = age;
            System.out.println("有参构造器");
        }
    }



    // 标准javabean案例
    public class User{
        // 属性
        private String username;
        private String password;
        private String email;

        // 空参
        public User(){}

        // 带有全部实参的构造
        public User(String username, String password, String email){
            this.username = username;
            this.password = password;
            this.email = email;
        }

        // set方法
        public void setUsername(String username){
            this.username = username;
        }

        // get方法
        public String getUsername(){
            return username;
        }


        /* 上述全部格式简便输出方法
            方法一 alt + insert
            1.选择构造函数 按住shift不松 点击最下方的f(全部选中) 然后ok
            2.选择Getter and Setter 同样全部选中 然后ok

            方法二 PTG 需要连接外网
            file setting plugins 安装ptg
            右键 选择 Ptg To JavaBean
         */
    }

}










