package com.mystatic.a06;   // 包 com.mystatic.a06

public class test_bao {
    public static void main(String[] args) {
        // 包 文件夹 用来管理不同功能的java类 方便后期代码维护
        /* 创建规则
            1.包名  公司域名反写+包的作用  所有字母小写

                   package com.mystatic.a06;

            2.需要使用其他类时 使用全类名

                public static void main(String[] args) {
                    com.mystatic.a05.test_duotai t = new com.mystatic.a05.test_duotai();
                             包名       +     变量名 = new 类名();
                }

                import关键字   导包  导入其他包的类
                    import com.mystatic.a05.test_duotai;

                    public static void main(String[] args) {
                        test_duotai t = new test_duotai();
                            类名 变量名 = new 类名();
                    }


                    1.使用同包下的类 不需要导包
                    2.使用java.lang(核心包)包下的类 不需要导包
                    3.使用其他包下的类 需要导包
                    4.同时使用不同包下的同名类 需要导包  且使用全类名
         */



        // final 最终包 不能被继承  最终的 -> 不能被改变
        /* 1.修饰变量
                常量 只能被赋值一次
            2.修饰方法
                表明该方法是最终方法 方法不能被重写
                只能给子类继承 不能改变
            3.修饰类
                表明该类是最终类 类不能被继承
         */

        // final修饰变量 -> 常量  必须赋值
        final int num = 10;

        // final修饰类
        final class Person{
            String name = "person";
            // final修饰方法
            public final void eat(){
                System.out.println("人吃饭");
            }
        }



        /* 常量
            单个单词全部大写 多个单词用下划线连接

            final修饰变量是基本类型 变量的值不能发生改变
                final PI = 3.14
                PI = 2     报错

            final修饰变量是引用类型 变量的地址值不能发生改变 但是地址里面的内容可以发生改变
                final Student S = new Person("张三",18);
                S.setName("李四");
                S.setAge(20);     可以改变 不报错

                final int[] ARR = {1,2,3};
                ARR[0] = 4;       可以改变 不报错
                arr里记录的是地址值

            字符串是不可变的    字符串常量池
                final String str = "hello";
                str = "world";     报错
         */

        // private static final String xxx = "xxx";



        // 权限修饰符
        /* 1.修饰成员变量
                private 私有的 只能在本类中访问
                public 公共的 可以在任何地方访问
                protected 受保护的 可以在本类中访问 子类中访问 同一个包中访问
                默认的 可以在本类中访问 同一个包中访问
            2.修饰成员方法
                private 私有的 只能在本类中访问
                public 公共的 可以在任何地方访问
                protected 受保护的 可以在本类中访问 子类中访问 同一个包中访问
                默认的 可以在本类中访问 同一个包中访问
            3.修饰构造方法
                private 私有的 只能在本类中访问
                public 公共的 可以在任何地方访问
                protected 受保护的 可以在本类中访问 子类中访问 同一个包中访问
                默认的 可以在本类中访问 同一个包中访问
            4.修饰类
                public 公共的 可以在任何地方访问
                默认的 可以在本类中访问 同一个包中访问


            private < 默认的(空) < protected < public
            实际开发中 用public private 最多
        */



        /* 举例解释
            private   同一个类中 (同一个家庭中 小)
            空        同一个包中 (同一个所属类别中 大 eg.人类)
            protected 同一个类 不同包中 子类中 (受保护的 eg.非同一个家庭私生子)
            public    任何地方

            class 大{
                private 方法1
                直接写   方法2
                protected 方法3
                public 方法4

            }
            class 小{
                方法1 报错
                如果想要引用方法1 需要在大类中提供一个公共的方法1的get

                方法2 报错

                方法3 如果小类是大类的子类 即extends可以引用 如果无关不能应用

                方法4 任何类可以直接引用
             }

             特例: 如果方法中的代码是抽取其他方法种共性代码 这个方法一般私有
         */



        /* 代码块
            1.局部代码块
                位置: 方法中
                作用: 限定变量的生命周期 及早释放 提高内存利用率 节省空间
                格式: {
                        变量的声明和初始化
                    }
            2.构造代码块
                位置: 类中 方法外 成员位置
                作用: 可以把多个构造方法中的共性(重复)代码抽取到构造代码块中
                格式: {
                        构造代码块中的代码
                    }
                执行顺序: 先执行构造代码块 再执行构造方法
            3.静态代码块
                位置: 类中 方法外
                作用: 可以把多个静态方法中的共性代码抽取到静态代码块中
                格式: static{
                        静态代码块中的代码
                    }
                执行顺序: 先执行静态代码块 再执行构造代码块 再执行构造方法
                注意: 静态代码块只执行一次
         */
    }
}
