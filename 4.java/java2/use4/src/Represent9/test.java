package Represent9;

public class test {
    public static void main(String[] args){
        /* 动态代理
            直接修改代码为侵入式修改 不提倡
            使用代理修改 -> 无侵入式的给代码增加额外功能

            代理可以转移部分职责
            eg.明星 和 经纪人 公司


        如何为Java对象创建一个代理对象?
                java.lanq.reflect.Proxy类：提供了为对象产生代理对象的方法：

        public static Object newProxyInstance(ClassLoader loader, Class<?>[] interfaces, InvocationHandler h
        参数一：用于指定用哪个类加载器，去加载生成的代理类
        参数二：指定接口，这些接口用于指定生成的代理长什么，也就是有哪些方法
        参数三：用来指定生成的代理对象要干什么事情
         */
        //1. 获取代理的对象
        BigStar bigStar = new BigStar("鸡哥");
        agent proxy = ProxyUtil.createProxy(bigStar);
        //2.调用唱歌的方法
        String result = proxy.sing("只因你太美");
        System.out.println(result);


    }
}
