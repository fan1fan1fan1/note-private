package xian6;

public class RunDemo2 implements Runnable {
    @Override
    public void run(){
        // 书写线程要执行的代码

        for (int i = 0; i < 5; i++) {
            //System.out.println("hello world");

            // 先获取当前线程对象
            Thread t = Thread.currentThread();
            System.out.println(t.getName()+"hello world");

            // System.out.println(Thread.currentThread().getName()+"hello world"); 链式编程
        }
    }
}