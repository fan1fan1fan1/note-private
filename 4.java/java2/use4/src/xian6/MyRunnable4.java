package xian6;

// 同步代码块
/*
public class picket4 extends Thread {
    // 这是一个卖票的例子 一共100张票 三个窗口卖

    static int ticket = 0;//0 ~ 99
    static Object obj = new Object(); // 锁对象

    @Override
    public void run() {

        while (true) {
            // 同步代码块
            synchronized (obj){

                if (ticket < 100) {

                    try {
                        Thread.sleep(100);
                    }
                    catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    ticket++;
                    System.out.println(getName() + "正在卖第" + ticket);

                }

                else {
                    break;
                }

            }
        }

    }

}
*/

// 同步方法
public class MyRunnable4 implements Runnable{
    int ticket = 0;
    @Override
    public void run() {
        //1.循环
        while(true){
            //2.同步代码块（同步方法）ctrl alt m
            if (method()) break;
        }
    }

    // this
    public synchronized boolean method(){
        //3.判断共享数据是否到了末尾，如果到了末尾
        if (ticket == 5) {
            return true;
        } else {
            //4.判断共享数据是否到了末尾，如果没有到末尾
            ticket++;
            System.out.println(Thread.currentThread().getName() + "在卖第" + ticket + "张票!!!");
        }
        return false;
    }
}
