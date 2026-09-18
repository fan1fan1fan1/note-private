import java.io.*;
import java.net.*;

public class Internate7 {
    public static void main(String[] args) throws IOException {
        /* 网络编程
            在网络通信协议下，不同计算机上运行的程序，进行的数据传输。

            应用场景：即时通信、网游对战、金融证券、国际贸易、邮件、等等。

            不管是什么场景，都是计算机跟计算机之间通过网络进行数据传输。
            Java中可以使用java.net包下的技术轻松开发出常见的网络应用程序。

            常见的软件架构BS和CS

            C/S: Client/Server  客户端/服务器  -> 下载 软件
                在用户本地需要下载并安装客户端程序，在远程有一个服务器端程序。

                特点: 1.画面可以做的非常精美，用户体验好
                     2.需要开发客户端，也需要开发服务端
                     3.用户需要下载和更新的时候太麻烦

            B/S: Browser/Server 浏览器/服务器  -> 访问 网址
                只需要一个浏览器，用户通过不同的网址。客户访问不同的服务器

                特点：1.不需要开发客户端，只需要页面+服务端
                     2.用户不需要下载，打开浏览器就能使用
                     3.如果应用过大，用户体验受到影响
         */



        /* 网络编程三要素
            ip      位置(目标)   设备在网络中的地址，是唯一的标识。
            端口号   软件        应用程序在设备中唯一的标识。
            协议     方式 规则   数据在网络中传输的规则，常见的协议有UDP、TCP、http、https、ftp。
         */


        System.out.println("----------------------------------------------------------------------------");


        /* ip
            全称：Internet Protocol，是互联网协议地址，也称IP地址。是分配给上网设备的数字标签。
            上网设备在网络中的地址，是唯一的
            常见的IP分类为IPv4、IPv6

            IPv4   全称：Internet Protocol version4，互联网通信协议第四版。
                采用32位地址长度，分成4组 32bit
                11000000 10101000 00000001 01000010(4字节) -> 点分+进制表示法 -> 192.168.1.66
                数量是有限的
                    ↓
            IPv6   全称：Internet Protocol version6，互联网通信协议第六版。
                由于互联网的蓬勃发展，IP地址的需求量愈来愈大，而IPv4的模式下IP的总数是有限的。
                采用128位地址长度，分成8组。
                数量有2^128个

                00100000 00000001 0000110-*1 10111000 00000000 00000000 00000000 00100011
                00000000 00001000 00001000 00000000 00100000 00001100 01000001 01111010
                                                ↓
                                        冒分十六进制表示法
                                                ↓
                            2001:0DB8:0000:0023:0008:0800:200C:417A
                                                ↓
                                            省略前面的0
                                                ↓
                                   2001:DB8:0:23:8:800:200C:417A

                如果压缩完有很多0:
                     FF01:0:0:0:0:0:0:1101 -> 0位压缩表示法 -> FF01::1101

            ipv4利用局域网节省ip  同空间共享同一个ip eg.网吧

            特殊ip地址
                127.0.0.1，也可以是localhost：是回送地址也称本地回环地址，也称本机IP，永远只会寻找当前所在本机。

                局域网经过路由器 每个路由器给你分配不同的ip ip可能产生变化
                127ip不经过路由器 直接通过网卡通信

            常用的CMD命令
                ipconfig：查看本机IP地址
                ping：检查网络是否连通

            用来表示ip的类 InetAddress
                static InetAddress getByName(String host) 确定主机名称的IP地址。主机名称可以是机器名称，也可以是IP地址
                String getHostName()                      获取此IP地址的主机名
                String getHostAddress()                   返回文本显示中的IP地址字符串

         */

        //1.获取InetAddress的对象
        //IP的对象 一台电脑的对象
        InetAddress address = InetAddress.getByName("nine");
        System.out.println(address);

        String name = address.getHostName(); // 如果没有主机名 会返回ip
        System.out.println(name);

        String ip = address.getHostAddress();
        System.out.println(ip);


        System.out.println("----------------------------------------------------------------------------");


        /* 端口号
            应用程序在设备中唯一的标识。

            端口号：由两个字节表示的整数，取值范围：0~65535
            其中0~1023之间的端口号用于一些知名的网络服务或者应用。
            我们自己使用1024以上的端口号就可以了。

            注意：一个端口号只能被一个应用程序使用。
         */


        /* 协议
            计算机网络中，连接和通信的规则被称为网络通信协议

            UDP协议
                用户数据报协议(UserDatagramProtocol)
                UDP是面向无连接(无需网络连接)通信协议。
                速度快，有大小限制一次最多发送64K，数据不安全，易丢失数据
            TCP协议
                传输控制协议TCP(Transmission Control Protocol)
                TCP协议是面向连接的通信协议。
                速度慢，没有大小限制，数据安全。

        */


        System.out.println("---------------------------------------------------------------------------");


         /* UDP通信程序（接收数据）
            1.找快递公司         创建接收端的DatagramSocket对象
            2.接收箱子           接收打包好的数据
            3.从箱子里面获取礼物  解析数据包
            4.签收走人           释放资源
         */


        //1.创建DatagramSocket对象（快递公司）
        /* 细节：
            在接收的时候，一定要绑定端口
            而且绑定的端口一定要跟发送的端口保持一致
         */
        DatagramSocket ds1 = new DatagramSocket(10086);

        //2.接收数据包
        byte[] bytes1 = new byte[1024];
        DatagramPacket dp1 = new DatagramPacket(bytes1, bytes1.length);
        ds1.receive(dp1); //该方法是阻塞的 程序执行到这一步的时候，会在这里死等 等发送端发送消息

        //3.解析数据包
        byte[] data = dp1.getData();
        int len = dp1.getLength();
        InetAddress address2 = dp1.getAddress();
        int port1 = dp1.getPort();

        System.out.println("接收到数据" + new String(data, 0, len));
        System.out.println("该数据是从"+ address2 +"这台电脑中的"+ port1 +"这个端口发出的");

        //4.释放资源
        ds1.close();



        /*
            UDP通信程序（发送数据）
                1.找快递公司      创建发送端的DatagramSocket对象
                2.打包礼物        数据打包(DatagramPacket)
                3.快递公司发送包裹 发送数据
                4.付钱走人        释放资源
         */

        //1.创建DatagramSocket对象（快递公司）
        /* 细节：
            绑定端口，以后我们就是通过这个端口往外发送
            空参：所有可用的端口中随机一个进行使用
            有参：指定端口号进行绑定
         */
        DatagramSocket ds = new DatagramSocket();

        //2.打包数据
        String str ="你好威啊!!!";
        byte[] bytes = str.getBytes();

        InetAddress address1 = InetAddress.getByName("127.0.0.1");

        int port = 10086;

        DatagramPacket dp = new DatagramPacket(bytes, bytes.length, address1, port);

        //3.发送数据
        ds.send(dp);

        //4.释放资源
        ds.close();

        // 一定要先运行接收端 再运行发送端 且接收端和发送端不能在同一个文件里 实际肯定是两个东西进行发送接收


        System.out.println("---------------------------------------------------------------------------");


        /* UDP的三种通信形式 单播 组播 广播
            单播  以前的代码就是单播
            组播  组播地址：224.0.0.0~239.255.255.255
                 其中224.0.0.0~224.0.0.255为预留的组播地址
            广播  广播地址：255.255.255.255
         */


        // 组播 发送端

        // 创建MulticastSocket对象
        MulticastSocket ms = new MulticastSocket();

        // 创建DatagramPacket对象

        String s="你好，你好!";
        //byte[] bytes = s.getBytes();
        InetAddress address3 = InetAddress.getByName("224.0.0.1"); //此处要指定组播地址
        //int port = 10000;
        DatagramPacket datagramPacket = new DatagramPacket(bytes, bytes.length, address3, port) ;

        // 调用MulticastSocket发送数据方法发送数据
        ms.send(datagramPacket);

        //释放资源
        ms.close();




        // 组播接收端 不能写在同一个文件 可以写多个 都匹配上方发送端 -> 组播

        //1. 创建MulticastSocket对象
        //MulticastSocket ms = new MulticastSocket(10000);

        //2.将将当前本机，添加到224.0.0.上的这一组当中

        InetAddress address4 = InetAddress.getByName("224.0.0.1");
        ms.joinGroup(address4);

        //3. 创建DatagramPacket数据包对象
        //byte[] bytes = new byte[1024];
        //DatagramPacket dp = new DatagramPacket(bytes, bytes.length);

        //4.接收数据
        ms.receive(dp);

        //5. 解析数据
        //byte[] data = dp.getData();
        //int len = dp.getLength();
        //String ip = dp.getAddress().getHostAddress();
        //String name = dp.getAddress().getHostName();
        System.out.println("ip为："+ip+"，主机名为："+ name +"的人，发送了数据："+ new String(data, 0, len));

        //6.释放资源
        ms.close();


        System.out.println("---------------------------------------------------------------------------");

        /* 广播
            广播代码和单播非常相似
            就是把
            InetAddress address1 = InetAddress.getByName("127.0.0.1");
            中的127.0.0.1
            变成255.255.255.255即可
         */


        System.out.println("---------------------------------------------------------------------------");

        /* TCP
            TCP通信协议是一种可靠的网络协议，它在通信的两端各建立一个Socket对象
            通信之前要保证连接已经建立
            通过Socket产生IO流来进行网络通信

            http

            客户端 发送数据 -> 输出流
            服务器 接收数据 -> 输入流

            步骤
                客户端
                    1.创建客户端的Socket对象(Socket)与指定服务端连接 Socket(String host, int port)
                    2.获取输出流，写数据                           OutputStream getOutputStream()
                    3.释放资源                                   void close()
                服务端
                    1.创建服务器端的Socket对象                     (ServerSocket)ServerSocket(int port)
                    2.监听客户端连接，返回一个Socket对象             Socket accept()
                    3.获取输入流，读数据，并把数据显示在控制台         InputStream getInputStream()
                    4.释放资源                                    void close()

            程序要先运行服务端
         */

        // TCP发送数据 输出流
        //1.创建Socket对象
        //细节：签创建对象的同时会连接服务端 如果连接不上，代码会报错
        // 三次握手协议
        Socket socket = new Socket("127.0.0.1",10000);

        //2.可以从连接通道中获取输出流
        OutputStream os =socket.getOutputStream();
        //写出数据 此处如果写入中文 在接收数据流需要写一个转换流 转换字节编码 防止乱码
        os.write("你好你好".getBytes());

        //3.释放资源
        // 四次挥手协议
        os.close();
        socket.close();



        // TCP接收数据 不能写在同一个文件 输入流

        //1.创建对象ServerSocker
        ServerSocket ss = new ServerSocket(10000);

        //2.监听客户端的链接
        Socket socket1 = ss.accept();

        //3.从连接通道中获取输入流读取数据
        InputStream is = socket.getInputStream();
        InputStreamReader isr = new InputStreamReader(is);  // 转换流
        BufferedReader br = new BufferedReader(isr);  // 缓冲流 提高读取效率
        int b;
        while ((b = br.read()) != -1) {
            System.out.print((char) b);
        }

        //4.释放资源
        socket1.close();
        ss.close();



        /* TCP三次握手协议 确保连接建立
           TCP四次挥手协议 确保链接断开 且数据处理完毕
         */




        System.out.println("---------------------------------------------------------------------------");
        System.out.println("---------------------------------------------------------------------------");
        System.out.println("---------------------------------------------------------------------------");
        System.out.println("---------------------------------------------------------------------------");
        System.out.println("---------------------------------------------------------------------------");

    }
}
