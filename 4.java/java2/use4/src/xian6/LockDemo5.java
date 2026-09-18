package xian6;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LockDemo5 extends Thread {
    static Lock lock = new ReentrantLock();

    static int ticket = 0;//0 ~ 99

    @Override
    public void run() {
        while (true) {
            lock.lock();
            try {
                if (ticket == 100) {
                    break;
                } else {
                    Thread.sleep(10);
                    ticket++;
                    System.out.println(getName() + "正在卖第" + ticket);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                lock.unlock();  //  防止多个线程影响线程停止 写在finally
            }
        }
    }
}

