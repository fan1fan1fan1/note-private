package xian6;

import java.util.concurrent.*;

public class test {
    public static void main(String[] ars) throws ExecutionException, InterruptedException {
        /* 多线程
            线程 程序运行的最小单位 应用软件中相互独立 可以同时运行的功能
            多个线程就是多线程 同时执行多个任务

            并发 同时有多个指令在单个CPU上交替执行
            并行 同时有多个指令在单个CPU上同时执行
            并发并行可以同时发生

            电脑CPU  2核4线程、4核8线程、8核16线程、16核32线程、32核64线程 有很多很多的种类 代表能同时运行多少线程

            多线程的实现
            1.继承Thread类的方式进行实现
            2.实现Runnable接口的方式进行实现
            3.利用Callable接口和Future接口方式实现

            继承Thread类的方式进行实现
            一个Thread表示表示一个线程 想运行多线程就可以创建多个Thread对象
                1.定义一个类用来继承Thread
                2.重写run方法
                3.创建子类对象 并启动线程
         */

        // 创建子类对象
        ThreadDemo1 t1 = new ThreadDemo1();
        ThreadDemo1 t2 = new ThreadDemo1();
        // 起名字
        t1.setName("线程1");
        t1.setName("线程2");
        // 启动线程
        t1.start();
        t2.start();



        /* 实现Runnable接口的方式进行实现
            1.定义类实现接口
            2.重写run方法
            3.创建Thread类对象 并开启线程
         */
        RunDemo2 t3 = new RunDemo2();  // 任务对象
        RunDemo2 T3 = new RunDemo2();  // 任务对象
        Thread t4 = new Thread(t3);
        Thread T4 = new Thread(t3);
        t4.setName("线程1");
        T4.setName("线程2");
        t4.start();
        T4.start();



        /* 利用Callable接口和Future接口方式实现
            可以获取多线程运行结果

            1.创建类
            2.重写call()方法 有返回值
            3.创建类对象 表示多线程任务
            4.创建Future接口实现类对象 管理多线程运行结果
            5.创建Thread类对象 表示线程 并启动
         */
        Mycallable3 mc = new Mycallable3();
        FutureTask<Integer> ft = new FutureTask<>(mc);  // 记得传参数
        Thread T = new Thread(ft);
        T.start();
        Integer result = ft.get();
        System.out.println(result);



        /* Thread常见成员方法
            1.String getName()                返回此线程的名称 有默认名字Thread-
            2.void setName(String name)       设置线程的名字（构造方法也可以设置名字）

            在类中继承父类方法 命名方法二
                public MyThread(){}
                public MyThread(String name) {
                    super(name);
                }
            在主函数中可以直接创建名字
                MyThread t1 = new MyThread( name:"飞机”)；


            3.static Thread currentThread()   获取当前线程的对象
                当JVM虚拟机启动之后，会自动的启动多条线程
                其中有一条线程就叫做main线程
                他的作用就是去调用main方法，并执行里面的代码
                在以前，我们写的所有的代码，其实都是运行在main线程当中


            4.static void sleep(long time)    让线程休眠指定的时间，单位为毫秒
                1、哪条线程执行到这个方法，那么哪条线程就会在这里停留对应的时间
                2、方法的参数：就表示睡眠的时间，单位毫秒    1=1000毫秒
                3、当时间到了之后，线程会自动的醒来，继续执行下面的其他代码


            5.setPriority(int newPriority)    设置线程的优先级
            6.final int getPriority()         获取线程的优先级
                抢占式调度 随机性    优先级1-10档 默认5
                优先级越高 抢到cpu的概率大 也不一定一定先执行



            7.final void setDaemon(boolean on)设置为守护线程 备胎
                当非守护线程结束 守护线程也会结束 提前终止 且并不是立刻结束 有反应加载时间

            8.public static void yield()      出让线程/礼让线程
                出让执行权 尽可能让结果均匀 并不会全部让
                在类里写 循环内  Thread.yield()
            9.public static void join()       插入线程/插队线程
                在主函数里写 t.join()
         */


        // 3.哪条线程执行到这个方法，此时获取的就是哪条线程的对象
        Thread t = Thread.currentThread( );
        String name = t.getName();
        System.out.println(name);//main


        // 4.睡眠
        System.out.println("11111111111");
        Thread.sleep(50);  // 5000为5秒
        System.out.println("22222222222");


        // 5.优先级
        System.out.println(t1.getPriority());
        System.out.println(t.getPriority());
        // 可以直接赋值
        t1.setPriority(1);


        // 6.守护线程
        t1.setDaemon(true);



        /* 线程安全问题
            卖票

            执行线程代码时需要把对象锁起来
            synchronized(锁){ 共享代码 }

            特点1：锁默认打开，有一个线程进去了，锁自动关闭
            特点2：里面的代码全部执行完毕，线程出来，锁自动打开

            不能写在循环外面 写在判断外面
            锁对象必须唯一obj 同样的任务不同线程必须使用同一个锁 可以随意写Object

            常用obj写法  synchronized(主函数文件名.class){ 共享代码 }
                                           test.class
            就能保证唯一
         */



        /* 同步方法
            不写synchronized判断 可以写synchronized方法 同步方法
            修饰符 synchronized 函数(){}

            特点1：同步方法是锁住方法里面所有的代码
            特点2：锁对象不能自己指定 非静态：this
                                    静态：当前类的字节码文件对象
         */



        /* Lock锁
            synchronized锁是自动上锁 自动释放锁
            Lock锁对象提供手动上锁 手动释放锁
            void lock()    上锁
            void unlock()  释放锁

            Lock是接口 不能直接实例化 创建实现类ReentrantLock
            构造方法  ReentrantLock()


            死锁 锁的嵌套 是错误
            eg.吃饭问题 两个人 一双筷子 一次只能拿一根 如果a拿了一根 b拿了一根 形成死锁
            不写嵌套锁就行
         */



        /* 生产者和消费者 (等待唤醒机制)
            eg.厨师和吃货 需要桌子作为媒介 同时 一定得是厨师先执行
            吃货检查桌子是否有已存在的指令-> 吃货 执行指令/wait ->唤醒厨师执行命令
            厨师检查桌子是否有已完成的指令 -> wait/厨师完成指令 -> 厨师把指令结果放在桌子上 -> 厨师唤醒吃货 notify -> 吃货执行命令

            相关方法
                唤醒
                void wait()当前线程等待，直到被其他线程唤醒
                void notify()随机唤醒单个线程
                void notifyAll()唤醒所有线程 常用
         */

        //创建线程的对象
        Cook6 c = new Cook6();
        Foodie6 f = new Foodie6();
        //给线程设置名字
        c.setName("厨师");
        f.setName("吃货");
        //开启线程
        c.start();
        f.start();



        /* 线程状态
            新建 就绪 运行 阻塞 等待 计时等待 死亡

            新建状态(NEW)           创建线程对象
            就绪状态(RUNNABLE)      start方法
            阻塞状态(BLOCKED)       无法获得锁对象
            等待状态(WAITING)       wait方法
            计时等待(TIMED WAITING) sleep方法
            结束状态(TERMINATED)    全部代码运行完毕
         */



        /* 线程池
            给线程池添加任务 线程池会自动添加线程 执行任务 然后把线程归还
            下一次再添加任务时 会复用上一个线程
            如果上一个线程还未归还 会再次新建一个线程


            原理
                创建一个池子，池子中是空的
                提交任务时，池子会创建新的线程对象，任务执行完毕，线程归还给池子
                下回再次提交任务时，不需要创建新的线程，直接复用已有的线程即可
                但是如果提交任务时，池子中没有空闲线程，也无法创建新的线程，任务就会排队等待

            代码步骤
                1，创建线程池
                2，提交任务
                3，所有的任务全部执行完毕，关闭线程池(正式项目中 服务器 并不关闭)

            线程池的实现:  Executors 线程池的工具类通过调用方法返回不同类型的线程池对象。

            public static ExecutorService newCachedThreadPool()             创建一个没有上限的线程池 上限为int最大值
            public static ExecutorService newFixedThreadPool(int nThreads)  创建有上限的线程池
         */

        // 1.获取线程池对象
        ExecutorService pool1 = Executors.newCachedThreadPool();
        ExecutorService pool2 = Executors.newFixedThreadPool(3);

        // 2.提交任务
        pool1.submit(new MyRunnable4());
        pool2.submit(new MyRunnable4()); // 可重复写 名字只会有三种 线程最多三种

        // 3.销毁线程池 不必要
        pool1.shutdown();



        /* 自定义线程池
            核心元素一：正式员工数量                               核心线程数量
            核心元素二：餐厅最大员工数                             程池中最大线程的数量
            核心元素三：临时员工空闲多长时间被辞退（值）              空闲时间（值）
            核心元素四：临时员工空闲多长时间被辞退（单位）            空闲时间（单位）
            核心元素五：排队的客户                                 阻塞队列
            核心元素六：从哪里招人                                 创建线程的方式
            核心元素七：当排队人数过多，超出顾客请下次再来（拒绝服务）  要执行的任务过多时的解决方案

            任务拒绝策略
                常用
                    ThreadPoolExecutor.AbortPolicy          默认策略：丢弃任务并抛出RejectedExecutionException异常
                不常用
                    ThreadPoolExecutor.DiscardPolicy        丢弃任务，但是不抛出异常 这是不推荐的做法
                    ThreadPoolExecutor.Discard0ldestPolicy  抛弃队列中等待最久的任务 然后把当前任务加入队列中(抛弃等待的 第一个任务)
                    ThreadPoolExecutor.CallerRunsPolicy     调用任务的run()方法绕过线程池直接执行
         */



        /* 线程池最大大小 最大的并行数
            四核八线程 -> cpu有四个大脑 -> 通过超线程技术可以把原本的四个大脑模拟成八个 -> 八线程 最大并行数8

            线程池合适大小
                CPU 密集型运算 使用计算更多
                    大小 -> 最大并行数+1

                I/0 密集型运算 读取cpu 数据库 文件更多   更常用
                    大小 -> 最大并行数 * 期望CPU利用率 * [ 总时间(CPU计算时间+等待时间) / CPU 计算时间]
                                 32  *   100%    *   任务执行需要时间+加载数据时间/任务执行需要时间

            此电脑为32个线程
            要获取本地电脑线程个数
         */
        //向Java虚拟机返回可用处理器的数目
        int count = Runtime.getRuntime().availableProcessors( );
        System.out.println(count);



        /* 多线程扩展 少使用 面试
            volatile
            JMM
            悲观锁、乐观锁、CAS
            原子性
            并发工具类
         */

    }
}
