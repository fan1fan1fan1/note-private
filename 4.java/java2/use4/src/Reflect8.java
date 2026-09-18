import java.lang.reflect.*;

public class Reflect8 {
    public static void main(String[] args) throws ClassNotFoundException, NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException, NoSuchFieldException {
        /* 反射
            允许对成员变量、成员方法、构造方法 的信息进行编程访问
            说白了 从类里拿东西 标注信息 获取信息

            eg. java的自动提示 方法的形参写完后的灰色提示

            要学习:获取对象、解剖对象

            第一步 获取对象 信息
            第二步 获取方法
            第三步 解剖所有信息

            获取对象 通过class字节码
            方法 1.Class.forName("全类名")； 最常用   全类名:包名+类名
                 2.类名.class               常用作参数
                 3.对象.getClass()；
         */

        // 获取Student2 类的对象
        // 方法1  Class.forName("全类名")；
        Class<?> cla = Class.forName("Student2");// 右键类名 复制引用 如果是src下的类 全包名就是类名

        // 方法2 类名.class
        Class cla1 = Student2.class;

        // 方法3 对象.getClass()；
        Student2 s = new Student2();
        Class<? extends Student2> cla2 = s.getClass();

        System.out.println(cla==cla1);
        System.out.println(cla2==cla1); // 证明对象相同


        System.out.println("---------------------------------------------------------------------------");


        /* 获取方法
            构造方法        通过Constructor
            字段(成员变量)   通过Field
            成员方法        通过Method

            1.利用反射获取构造方法
                Class类中用于获取构造方法的方法
                    Constructor<?>[] getConstructors();                                 返回所有公共构造方法对象的数组  public
                    Constructor<?>[] getDeclaredConstructors();                         返回所有构造方法对象的数组     所有
                    Constructor<T>getConstructor(Class<?>... parameterTypes);           返回单个公共构造方法对象       单个 public
                    Constructor<T>getDeclaredConstructor(Class<?>... parameterTypes);   返回单个构造方法对象          单个 所有
                Constructor类中用于创建对象的方法
                    T newInstance(Object...initargs);   根据指定的构造方法创建对象
                    setAccessible(booleanflag);         设置为true，表示取消访问检查
         */
        Constructor[] cons = cla.getConstructors();
        for (Constructor con : cons) {
            System.out.println(con);
        }

        Constructor[] cons1 = cla.getDeclaredConstructors();
        for (Constructor con : cons1) {
            System.out.println(con);
        }

        Constructor<?> con = cla.getDeclaredConstructor();
        System.out.println(con);

        Constructor<?> con1 = cla.getDeclaredConstructor(String.class);  // 形参可添加
        System.out.println(con1);
        int m = con1.getModifiers();
        System.out.println(m);   // 返回权限修饰符 不返回返回值名字 返回编号
        /* ABSTRACT      1024
            FINAL        16
            INTERFACE    512
            NATIVE       256
            PRIVATE      2
            PROTECTED    4
            PUBLIC       1
            STATIC       8
            STRICT       2048
            SYNCHRONIZED 32
            TRANSIENT    128
            VOLATILE     64
         */

        /*
        Constructor<?> con2 = cla.getDeclaredConstructor(int.class);
        System.out.println(con2);
         */

        // 返回构造参数
        Parameter[] p = con1.getParameters();
        for (Parameter parameter : p) {
            System.out.println(parameter);
        }

        // 创建对象
        con1.setAccessible(true); // 临时取消权限校验 暴力反射
        Student2 stu = (Student2) con1.newInstance("a");
        System.out.println(stu);


        System.out.println("---------------------------------------------------------------------------");

        /* 2.反射获取成员变量
            Class类中用于获取成员变量的方法
                Field[]getFields()：返回所有公共成员变量对象的数组
                Field[]getDeclaredFields()：返回所有成员变量对象的数组
                Field getField(String name)：返回单个公共成员变量对象
                Field getDeclaredField(String name)：返回单个成员变量对象
            Field类中用于创建对象的方法
                void set(Object obj, Object value)：赋值
                Object get(Object obj)获取值。
         */
        //获取所有的成员变量
        Field[] fields = cla1.getDeclaredFields( );
        for (Field field : fields) {
            System.out.println(field);
        }
        //获取单个的成员变量
        Field name = cla1.getDeclaredField("name");
        System.out.println(name);
        //获取权限修饰符
        int modifiers = name.getModifiers();
        System.out.println(modifiers);
        //获取成员变量的名字
        String n = name.getName();
        System.out.println(n);
        //获取成员变量的数据类型
        Class<?> type = name.getType();
        System.out.println(type);
        //获取成员变量记录的值
        Student2 st = new Student2("zhangsan",23);
        name.setAccessible(true) ;
        Object value = name.get(st);
        System.out.println(value);
        //修改对象里面记录的值
        name.set(s, "lisi");
        System.out .println(s);


        System.out.println("---------------------------------------------------------------------------");

        /* 3.反射获取成员方法
            Class类中用于获取成员方法的方法
                Method[] getMethods()：返回所有公共成员方法对象的数组，包括继承的
                Method[]getDeclaredMethods()：返回所有成员方法对象的数组，不包括继承的
                Method getMethod(String name, Class<?>... parameterTypes)：返回单个公共成员方法对象
                Method getDeclaredMethod(String name, Class<?>... parameterTypes)：返回单个成员方法对象
            Method类中用于创建对象的方法
                Object invoke(Object obj, Object... args)：运行方法
                参数一：用obj对象调用该方法
                参数二：调用方法的传递的参数（如果没有就不写）
                返回值：方法的返回值（如果没有就不写）
         */
        //2.获取里面所有的方法对象（包含父类中所有的公共方法）
        Method[] methods = cla1.getMethods();
        for (Method method : methods){
            System.out.println(method);
        }
        //获取里面所有的方法对象（不能获取父类的，但是可以获取本类中私有
        Method[] methods1 = cla1.getDeclaredMethods();
        for (Method method : methods1) {
            System.out.println(method);
        }


        /* 获取指定的单一方法
        Method m1 = cla1.getDeclaredMethod("方法名", String.class);
        System.out.println(m1);

        方法的修饰符
        int modifiers1 = m1.getModifiers();
        System.out.println(modifiers1) ;

        获取方法的名字
        String name = m.getName();
        System.out.println(name);

        获取方法的形参
        Parameter[] parameters = m.getParameters();
        for (Parameter parameter : parameters) {
        System.out.println(parameter);

        获取方法的抛出的异常
        Class[] exceptionTypes = m.getExceptionTypes()
        for (Class exceptionType : exceptionTypes) {
        System.out.println(exceptionType);

        方法运行
            Method类中用于创建对象的方法
            Object invoke(Object obj, Object... args):运行方法
            参数一：用obj对象调用该方法
            参数二：调用方法的传递的参数（如果没有就不写）
            返回值：方法的返回值（如果没有就不写）
        Student s = new Student();
        m.setAccessible(true);

            参数一s：表示方法的调用者
            参数二"汉堡包"：表示在调用方法的时候传递的实际参数
        String result =(String) m.invoke(s,..args:"汉堡包")；
        System.out.println(result);
        */

    }
}
