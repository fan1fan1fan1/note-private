package xian6;

public class Desk6 {
    // 控制生产者和消费者执行

    public static int foodFlag = 0; // 标记此时是否存在已执行完命令

    public static int count = 10; // 总个数 执行次数 结束条件

    public static Object Lock = new Object(); // 锁对象
}
