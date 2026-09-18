public class helloworld1 {
    public static void main(String[] args){
        System.out.println("HelloWorld");
    }



    // 常见cmd命令
    /*
    盘符 冒号       : 切盘
    dir           : 查看当前路径下的内容
    cd 目录        : 进入单级目录    tab目录
    cd ..         : 回退到上一级目录
    cd 目录1\目录2..: 进入多级目录
    cd \          : 回退到盘符
    cls           : 清屏
    exit          : 退出
    */



    // 命令符中操作
    /*
        首先确定代码文件所在路径 然后在命令行中输入路径
        (也可以直接在文件管理中操作
        点击上方搜索路径 即点击这个代码路径 直接敲入cmd 同样可以进入命令行)

        javac + 文件名.java
        通过javac工具 会把java文件变成类型 后缀名变成class

        java + 文件名

        回车
        即运行该指令
     */



    // 配置环境变量
    /*
        java已经默认添加了一些环境变量
        但如果需要使用的工具没在环境变量中就需要手动添加环境变量

        首先将已有的Java环境变量删除

        (在java文件夹中选中bin 复制文件路径

        在环境变量中添加)
        不推荐

        在path并列位置上
        新建系统变量 JAVA_HOME

        将路径粘贴到变量值上(删除路径中的bin 只要前部分的路径)

        再次进入path
        添加  %JAVA_HOME%\bin
     */



    /* 应用
        java SE 桌面应用开发 (更推荐c c++)
        java ME 嵌入电子设备(电脑 相机)和小型移动设备(手机)
        java EE web网站开发(推荐)

        IDEA Clion Pycharm
        企业开发springcloud
        android 鸿蒙
        科学计算matlab
        大数据开发hadoop
        游戏开发
     */



    /* java特性
       面向对象
       多线程
       开源
       跨平台(操作系统)
            由于兼容性问题 当改变平台时 java的代码内容需要更改
            java通过将代码在虚拟机中使用并运行来实现跨平台 jvm
    */



    /* JDK java development kit       java开发工具包
        JVM java virtual machine 虚拟机
        核心类库
        开发工具: javac编译工具 java运行工具 jdb调试工具 jhat内存分析工具...

       JRE  java运行环境
        (如果已有java文件情况下 就不需要开发工具)
        JVM虚拟机
        核心类库
    */



    // public class HelloWorld{
        public static void main1(String[] args) {
            System.out.println("HelloWorld");

            int[] arr = {10, 20, 50, 70, 200, 90};
            int max = arr[0];
            for(int i = 0; i < arr.length; i++){
                if(arr[i] > max){
                    max = arr[i];
                }
            }
            System.out.println(max);
        }
}
