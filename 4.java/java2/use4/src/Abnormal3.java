import java.util.Scanner;

public class Abnormal3 {
    public static void main(String[] args) {
        /* Java.lang.Throwable
            1.Error 系统错误

            2.Exception 异常
                (1)RuntimeException 运行时异常： 编译阶段不会出现异常提醒(代码错误) 开始运行后显示报错（如：数组索引越界异常）
                (2)其他异常           编译时异常：编译阶段就会出现异常提醒(提醒)，标红。（如：日期解析异常）

            异常的作用:1.查询bug 2.方法内部的一种特殊返回值 以便通知调用者底层的执行情况
         */


        /* 写一个异常
            Student2[] arr = new Student2[3];  创建了数组对象 但是没创建属性
            String name = arr[0].getName();    直接调用数组[0]的name -> NULL 空指针异常
            System.out.println(name);
         */


        // 在成员方法中使用异常方法
        Student2 s1 = new Student2();
        // s1.setAge(50);   赋值失败 选择1:自己悄悄处理  选择2:打印在控制台(抛出给调用者)


        /* 自己处理 捕获异常
            try{
                可能会出现异常的代码
            }catch(异常类型 变量名){
                处理异常的代码
            }finally{
                无论是否出现异常 都会执行的代码
            }

            这样 如果出现了这种错误 不会影响结果运行 会提示这个警告
            可以让代码往下进行 不会停止
         */

        int[] arr = {1, 2, 3, 4, 5, 6};

        try{
            //可能出现异常的代码；
            System.out.println(arr[10]);
        }catch(ArrayIndexOutOfBoundsException e){
            //处理异常的代码
            System.out.println("数组索引越界异常");
        }

        System.out.println("看看我执行了吗?");

        /* try{
                此处出现了异常，程序就会在这里创建一个ArrayIndexOutOfBoundsException对象
                new ArrayIndexOutÖfBoundsException();
                拿着这个对象到catch的小括号中对比，看括号中的变量是否可以接收这个对象
                如果能被接收，就表示该异常就被捕获（抓住），执行catch里面对应的代码
                当catch里面所有的代码执行完毕，继续执行try...catch体系下面的其他代码
            }catch{
                如果出现了ArrayIndexOutÖfBoundsException异常 处理方法
            }

            相关问题:
                1.如果try中没有出现异常，catch就不会执行 相当于没有
                2.如果try中有多个异常 只要遇见第一个异常 就会进入catch 我们可以写多个catch来对应
                3.如果异常有父子关系 父异常一定要写在下面
                4.多种异常可以 |
                    catch(ArrayIndexOutOfBoundsException | ArithmeticException | NullPointerException e){
                        System.out.println("出现了异常");
                    }
                5.如果有异常 但是try没捕获(异常判断名写错了) 那么相当于这个try catch没写 错误会在终端出现 并停止程序运行
                6.如果try中遇到了问题 会停止try的其他程序运行 直接执行catch
         */

        int[] arr1 = {1, 2, 3, 4, 5, 6};
        try{
            System.out.println(arr[10]);//ArrayIndexOutOfBoundsException
            System.out.println(2/0);//ArithmeticException
            String s = null;
            System.out.println(s.equals("abc"));
        }catch(ArrayIndexOutOfBoundsException e) {
            System.out.println("索引越界了");
        /* 最大的父类异常 写上去会把后面所有的异常提示覆盖不执行 所有的异常都可以被Exception接收 全部吞下
          catch(Exception e){
            System.out.println("出现了异常");
          }
         */
        }catch(ArithmeticException e) {
            System.out.println("除数不能为0");
        }catch(NullPointerException e) {
            System.out.println("空指针异常");
        }
        System.out.println("看看我执行了吗?");



        /* Throwable 类的方法
            getMessage()  获取异常的信息 抛出简短描述
            toString()  获取异常的信息 抛出详细描述
            printStackTrace() 打印异常的栈轨迹 （出现异常的位置） 在控制台中输出错误信息

            printStackTrace() 的结果包括了getMessage()和toString()的结果 更常用
         */

        int[] arr2 = {1, 2, 3, 4, 5, 6};
        // System.out.println(arr2[10]);   选中可能出现异常的代码 ctrl+alt+t try/catch

        try{
            System.out.println(arr[10]);//ArrayIndexOutOfBoundsException
        }catch(ArrayIndexOutOfBoundsException e) {
            // System.out.println(e.getMessage());
            System.out.println(e.toString());
            //e.printStackTrace();
        }
        System.out.println("看看我执行了吗?");


        // 打印红色字体
        System.out.println("\033[31m" + 1 + "\033[0m");
        System.err.println(1);



        /* 抛出处理
            throws 写在方法定义处 表示声明一个异常
            public void 方法名()throws 异常类名1，异常类名2...{}

            throw 写在方法内 结束方法 手动抛出异常
            public void 方法名(){
                throw new NULLPointerException();  如果此处碰到了这种异常 后面的代码就不执行了
            }

            编译时异常 必须写
            运行时异常 可以不写
         */

        // 求数组最大值
        int[] arr3 = {1,2,3,4,5};
        int max = 0;

        try{
            max = getMax(arr3);
        }catch(NullPointerException e){
            System.out.println("空指针异常");
        }catch(ArrayIndexOutOfBoundsException e){
            e.printStackTrace();
            System.out.println("索引越界异常");
        }
        System.out.println(max);

        /* 抛出、调用的使用
                抛出: 告诉调用者错了 写在方法里边
                捕获: 不让程序停止  写在主函数里

          */


        // 在setter中使用抛出异常
        Scanner sc = new Scanner(System.in);
        Student2 S = new Student2();
        while(true){
            try{
                System.out.println("输入姓名");
                String name = sc.nextLine();
                S.setName(name);  // 可能报错位置1

                System.out.println("输入年龄");
                String ageStr = sc.nextLine();
                int age = Integer.parseInt(ageStr);  // 可能报错位置2
                S.setAge(age);  // 可能报错位置3

                break;
            }catch(NumberFormatException e){
                System.out.println("年龄格式有误");
                // .printStackTrace();
                // continue;
            }catch(NameFormatException3 e){
                System.out.println("姓名长度有误");
            }catch(RuntimeException e){
                // RuntimeException 级别更大 要写在下面
                // 此处可以不写RuntimeException 自定义两个异常 表示姓名和年龄

                System.out.println("姓名或年龄范围有误");
                // e.printStackTrace();
                // continue;
            }
        }
        System.out.println(S);



        /* 自定义异常 意义: 为了让控制台的报错信息更加见名知意
            1.定义异常类
            2.写继承关系
            3.空参构造
            4.带参构造

            此时我新建一个文件NameFormatException3 用于存放Student2中name不合法的异常

            写异常名时
            如果是编译时异常 名后必须写 throws XXX{}
            如果是运行时异常可以不写
         */



    }

    // 函数
    // 求数组最大值
    public static int getMax(int[] arr) throws NullPointerException,ArrayIndexOutOfBoundsException{
        if(arr == null){
            /* 数组不存在
                手动创建一个异常对象 并把这个对象交给方法的调用者处理
                此时方法就会结束 下面的代码就不会再执行了
             */

            throw new NullPointerException();
        }
        if(arr.length==0){
            // 数组为空
            throw new ArrayIndexOutOfBoundsException();
        }

        System.out.println("看看我执行了吗?");
        int max=arr[0];
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] > max){
                max = arr[i];
            }
        }
        return max;
    }


}
