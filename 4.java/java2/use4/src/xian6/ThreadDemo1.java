package xian6;

public class ThreadDemo1 extends Thread{

    @Override
    public void run(){
        // 书写线程要执行的代码

        for (int i = 0; i < 5; i++) {
            //System.out.println("hello world");

            System.out.println(getName()+"hello world");

            // Thread.yield()
        }
    }
}
