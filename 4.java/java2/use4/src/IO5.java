import org.apache.commons.io.FileUtils;

import java.io.*;
import java.nio.charset.Charset;
import java.util.Arrays;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;
import java.util.zip.ZipOutputStream;

public class IO5 {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        /* IO流 用于读写文件中的数据
            根据流的方向分类:
                读 output 输入流
                写 input 输出流
            根据操作文件类型分类:
                字节流 InputStream字节输入流 OutputStream字节输出流
                字符流(纯文本文件) Reader字符输入流 Writer字符输出流

            都是抽象类 不能直接创建对象

            字节流
            InputStream字节输入流  FileInputStream
            OutputStream字节输出流 FileOutputStream
         */

        // 输出流
        // 1.创建对象 选择第一种处理异常的方法
        FileOutputStream fos = new FileOutputStream("D:\\22820\\Desktop\\code\\java\\a.txt");
        // 2.写出数据 选择第一种处理异常的方法
        fos.write(97);
        // 3.释放数据 此处不释放数据 这个创建的文件夹在电脑中就无法删除 《病毒》
        fos.close();


        System.out.println("-------------------------------------------------");


        /* 细节
            1.创建的参数是路径或者file对象 如果指定的文件不存在会先创建 如果存在就会清空
            2.写入时 写的时ASCII码值
            3.使用后一定要释放
            4.三种写入方法 write

            void write(int b)      写入一个数据
            void write(byte[] b)   写入一个字节的数据
            void write(byte[] b, int off, int len) 数组部分  (数组,起始索引,个数)
         */


        // 1.创建对象
        FileOutputStream fos1 = new FileOutputStream("D:\\22820\\Desktop\\code\\java\\a.txt",true);

        // 2.写入数据
        byte[] bytes = {97,98,99,100};
        fos1.write(bytes,1,3);

        // 3.释放 fos1.close();


        System.out.println("-------------------------------------------------");


        /* 实现续写
            FileOutputStream fos1 = new FileOutputStream("\\\",true/false);
            有第二个参数 续写开关 这样原写的数据就不会被清空
         */
        String str = "abc";
        byte[] arr = str.getBytes();
        System.out.println(Arrays.toString(arr));


        // 实现换行 添加换行符 \r\n回车换行(是两步) 在java中可以只写一个有补充作用
        String wrap = "\r\n";
        byte[] bytes2 = wrap.getBytes();
        fos1.write(bytes2);

        String str2 = "666";
        byte[] bytes3 = str2.getBytes();
        fos1.write(bytes3);

        fos1.close();


        System.out.println("-------------------------------------------------");


        // 输入流
        // 1.创建对象 如果这个路径不存在就报错了
        FileInputStream fis = new FileInputStream("D:\\22820\\Desktop\\code\\java\\a.txt");

        // 2.读取数据
        int b1 = fis.read();  // 调用一次 读取一个数据 读出来是ASCII
        System.out.println(b1);
        System.out.println((char)b1); // 可以使用强转获取数据字符

        /* 读不到了输出-1
            如果数据中有一个数字是-1 会分开读 '-' '1'
         */

        // 循环读入
        int b;
        while((b = fis.read()) != -1){
            /* 1.写法 while( () != -1){}  然后再写b
               2.此处read必须写一个第三方变量b
                如果不写 循环读入 第一次在while判断 读了a 进入循环 读取b输出
                                第二次循环判断读了c 进入循环 读取d输出 丢了很多数据
             */
            System.out.println((char)b);
        }

        // 3.释放 fis.close();


        System.out.println("-------------------------------------------------");


        // 案例 文件拷贝
        // 1.创建对象
        FileInputStream fis1 = new FileInputStream("D:\\22820\\Desktop\\code\\java\\屏幕录制.mp4");
        FileOutputStream Fos1 = new FileOutputStream("D:\\22820\\Desktop\\code\\java\\b.mp4");

        // 2.拷贝
        int B;
        while((B=fis1.read()) != -1){
            Fos1.write(B);
        }

        // 释放 先开的后关闭
        Fos1.close();
        fis1.close();


        System.out.println("-------------------------------------------------");

        /* FileInputStream 一次都多个字节
            public int read()
            public int read(byte[] buffer)  也是read方法的重载
                在这种方法中 我们通常尽可能把数组装满 可以理解为数组容量越大读取越快
                每一次会读取数组长度个数个字节

            eg. 假设数据源中一共有abcde的字节 我用长度2的数组
                第一次 读取ab 输出ab
                第二次 读取cd 输出cd
                第三次 只剩一个元素了 但数组长度2 我们尽可能把数组装满
                      读取e c被e覆盖 输出ed
                第四次 读取不到了 -1 输出ed

                如果不想要第三次的残留数据d 我们可以在System.out.println(Str) 处添加参数(Bytes,0,len)
         */

        byte[] Bytes = new byte[2]; // byte[] Bytes = new byte[1024*1024*5];
        int len = fis.read(Bytes);  // 2
        System.out.println(len);  // 返回本次读取了几个字节

        String Str = new String(Bytes);
        System.out.println(Str);  // 输出当前数组存储的字节 有可能跟len读取的不一样
        /* System.out.println(new String(Bytes,0,len));
            跟上方出现过的while读取冲突了 此处注释 但是可用

            这种方法要使用 需要重复定义len 重复写定义len 到输出String的代码
         */



        // 循环方法:
        int Len;
        byte[] Bytes1 = new byte[1024*1024*5];
        while((Len = fis1.read(Bytes1)) != -1){
            Fos1.write(Bytes1,0,Len);
        }

        Fos1.close();
        fis1.close();


        System.out.println("-------------------------------------------------");

        /* 想要得到读取执行时间
            1.long start = System.currentTimeMillis();

            2.********** (FileInputStream** FileOutputStream**  ... close()**)

            3.long end = System.currentTimeMillis();
            4.System.out.println(end - start);

            输出毫秒 ms
         */


        System.out.println("-------------------------------------------------");

        /* 有关文件的异常判断 其实不用 直接抛出就行
            可以使用接口 AutoCloseable

            FileOutputStream fos = new
            try(fos){
                write read
            }catch(Exception){

            }finally{
                close
            }
         */


        System.out.println("-------------------------------------------------");

        /* 字节流读取中文会出现乱码-> 未读取完整数据 或 编码和解码方式不统一
            计算机的存储规则 二进制 1位是一个bit(比特位)
            8位一组是一个字节 也就是计算机最小存储单元

            ASCII 英 字母->ASCII码 前面补0 一共8位

            GBK 英 中 两个字节 16位 8位一组 高位字节+低位字节
                高位字节一定以1开头 第一个字节转成十进制是负数 第二个不一定

            Unicode 英 中 汉字  万国码 1-4个字节 不一定

            英语一定以0开头 为了中英文区分
         */

        /* 编码方法   idea默认使用utf-8
            public byte[] getBytes()                   默认方法
            public byte[] getBytes(String charsetName) 指定方法

            解码方法
            String(byte[] bytes)                       默认方法
            String(byte[] bytes,String charsetName)    指定方法
         */


        System.out.println("-------------------------------------------------");

        /* 字符流    字节流+字符集
            适用于纯文本文件操作

            Reader字符输入流   FileReader操作本地文件
                FileReader(File file)                  文件不存在就报错
                FileReader(String pathname)

            Writer字符输出流   FileWriter操作本地文件
                int read() 读取
                int read(char[] buffer) 同时读取多个

                FileWriter(File file) 创建关联本地文件   文件不存在会创建文件
                FileWriter(String pathname)
                FileWriter(File file,boolean append)        ,续写
                FileWriter(String pathname,boolean append)  ,续写

            int close()
         */

        // 1.创建对象
        FileReader fr = new FileReader("D:\\22820\\Desktop\\code\\java\\a.txt");

        // 2.读取数据 空参
        /* read()
            底层也是字节流 默认一个字节一个字节读取 中文一次读取多个
            读取后会解码变成十进制 返回十进制 字符集上数字
            想要数据再次进行强转 (char)ch
         */
        // 空参需要字符
        int ch;
        while((ch = fr.read()) != -1){
            System.out.println((char)ch);
        }

        // 3.释放资源 fr.close()


        // 2.读取数据 带参
        // 带参需要数组
        char[] chars = new char[2];
        int len1;
        while((len1 = fr.read(chars)) != -1){
            // 数组数据变成字符串再打印
            System.out.println(new String(chars,0,len));
        }
        fr.read();



        // 字符输出流
        FileWriter fw= new FileWriter("D:\\22820\\Desktop\\code\\java\\a.txt",true); // 续写
        fw.write(25105);
        fw.write("你好啊");
        //fw.close();

        // 写入一个字符数组
        char[] chars1 = {'a','b','c'};
        fw.write(chars);
        fw.close();


        System.out.println("-------------------------------------------------");

        // 字符高级流
        /* 1.字符缓冲流
            流加上缓冲区 不能直接读取数据 把基本流包装成高级流 提高效率

            字节缓冲流
            BufferedInputStream  入
            BufferedOutputStream 出

            字符缓冲流
            BufferedReader 入
            BufferedWriter 出
            String readLine() 读取一行数据
            void newLine()    跨平台换行
         */

        // 练习: 拷贝
        // 1.创建缓冲流对象
        BufferedInputStream bis = new BufferedInputStream(new FileInputStream("D:\\22820\\Desktop\\code\\java\\a.txt"));
        BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream("D:\\22820\\Desktop\\code\\java\\a.txt"));

        // 2.循环读取并写到目的地
        /* int b2;
            while((b = bis.read()) != -1){bos.write(b);}
         */
        byte[] bytes1 = new byte[1024];
        int len2;
        while((len2 = bis.read(bytes1)) != -1){
            bos.write(bytes1,0,len2);
        }

        // 3.释放资源
        bos.close();
        bis.close();


        // 字符缓冲输入流
        BufferedReader br = new BufferedReader(new FileReader("D:\\22820\\Desktop\\code\\java\\a.txt"));
        // String line = br.readLine();  读取一整行 不读取会回车换行
        // System.out.println(line);
        String line;
        while(((line = br.readLine()) != null)){
            System.out.println(line);
        }

        br.close();

        // 字符缓冲输出流
        BufferedWriter bw = new BufferedWriter(new FileWriter("D:\\22820\\Desktop\\code\\java\\a.txt",true));
        bw.write("111");  // 如果此时文件里有数据会被清空覆盖   打开续写开关 在文件后面
        bw.newLine(); // 换行
        bw.write("222");
        bw.newLine();

        bw.close();


        System.out.println("-------------------------------------------------");

        /* 转换流 当字节流想使用字符流的方法时
            字符流和字节流的桥梁
            读入：字节流转字符流
            输出：字符流转字节流
         */

        // 写入
        // 被替代了
        // 1.创建转换流对象并指定字符编码 此处第二个形参不跟文件写在一起 写在括号外
        InputStreamReader isr = new InputStreamReader(new FileInputStream("D:\\22820\\Desktop\\code\\java\\a.txt"),"GBK");

        // 替代版本
        FileReader fr1 = new FileReader("D:\\22820\\Desktop\\code\\java\\a.txt", Charset.forName("GBK"));

        // 2.读取数据
        int ch1;
        while((ch = fr1.read()) != -1){
            System.out.println((char)ch);
        }

        // 3.释放资源
        isr.close();


        // 写出
        //OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream("D:\\22820\\Desktop\\code\\java\\a.txt"),"GBK");
        FileWriter fw1 = new FileWriter("D:\\22820\\Desktop\\code\\java\\a.txt",Charset.forName("GBK"));

        fw1.write("111");  // 查看方式 左侧文件栏找到该文件 右键open in explorer
        fw1.close();


        System.out.println("-------------------------------------------------");

        /* 序列化流 字节 输出流
            把java文件中的对象写到本地文件中
            ObjectOutputStream
            writeObject
         */

        // 1.创建学生对象
        Student2 stu = new Student2("z",23);

        // 2.创建序列化流的对象/对象操作输出流
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("D:\\22820\\Desktop\\code\\java\\a.txt"));

        // 3.写出数据 此处需要实现Serializable接口
        // Serializable接口里没有抽象方法 标记接口 一但实现了这个接口 就代表Student2类可以被序列化
        oos.writeObject(stu);

        // 4.释放
        oos.close();


        System.out.println("-------------------------------------------------");

        /* 反序列化流 输入流
            ObjectInputStream
            readObject
         */

        // 1.创建反序列化流对象
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("D:\\22820\\Desktop\\code\\java\\a.txt"));

        // 2.读取数据 此处需要抛出异常 强转

        Student2 o = (Student2)ois.readObject();

        // 3.打印对象
        System.out.println(o);

        // 4.释放资源
        ois.close();


        /* 反序列化流 对象操作输入流 如果实现了Serializable接口
            会生成一个版本号
            创建对象时 对象内部数据就包含了这个版本号 如果加载进文件了 版本号也会出现在文件里
            但如果此时更改代码数据 就会生成新的版本号 此时在读取文件 就会报错 版本号不一样

            解决办法 不让版本号发生变化
            手动定义版本号 在类中
            1.private static final long SeriaLVersionUID = 1L;
            2.设置 序列化 勾选最下方jvm 这样在创建 SeriaLVersionUID 时会提醒版本号 并自动创建
            3.ctrl n 在类中搜索一个类 比如ArrayList 抄一个版本号 不推荐


            如果在类中 有部分变量不想参与到序列化本地文件
            该变量定义前加关键字transient   瞬态关键字
         */


        System.out.println("-------------------------------------------------");

        /* 打印流 只能写 只有输出流
            PrintStream 字节  刷新无用
            PrintWriter 字符 有缓冲区 效率更高

            只能操作目的地 不操作打印源
            有特有方法 数据原样写出 可以自动刷新
         */

        /* 字节
            1.创建对象
            public PrintStream(OutputStream/File/String)  输出
            public PrintStream(String fileName, Charset charset)  指定字符编码
            public PrintStream(OutputStream out, boolean autoFlush)  刷新
            public PrintStream(OutputStream out, boolean autoFlush, String encoding)  指定字符+刷新

            2.操作
            public void write(int b)  输出(常规方法 不打印字符 ASCII码)
            public void println(XXX xx)  打印 刷新 换行
            public void print(XXX xx)  打印 不换行
            public void printf(String format, Object... args)  带占位符打印 不换行
         */
        // 1.创建对象
        PrintStream ps = new PrintStream(new FileOutputStream("D:\\22820\\Desktop\\code\\java\\a.txt"), true,Charset.forName("UTF-8"));
        // ctrl p查看可以使用的形参

        // 2.写出数据
        ps.println(97);
        ps.print(true);
        ps.printf("%s","阿珍");

        // 3.释放资源
        ps.close();


        /* 字符
            public PrintWriter(Write/File/String)  输出
            public PrintWriter(String fileName, Charset charset)  指定字符编码
            public PrintWriter(Write w, boolean autoFlush)  刷新
            public PrintWriter(OutputStream out, boolean autoFlush, Charset charset)  指定字符编码+刷新

            public void write()
            public void println()
            public void print(XXX xx)
            public void printf()
         */
        // 1.创建对象
        // 2.写出数据
        // 3.释放资源


        PrintStream ps1 = System.out;
        ps.println("123");
        /* 系统标准输出流
            不能关闭

            System.out.println() 链式编程
            打印流的应用 PrintStream
         */


        System.out.println("-------------------------------------------------");

        /* 解压缩流 读         压缩流  写

            解压缩 .zip
            把压缩包中每一个ZipEntry按照层级拷贝到本地另一个文件夹中
         */
        // 1.创建待解压缩文件
        File src = new File("D:\\22820\\Desktop\\code\\java\\a.zip");

        // 2.创建文件目的地 如果待解压是文件夹 此创建文件夹
        File dest = new File("D:\\22820\\Desktop\\code\\java");

        // 3.解压 引用函数  重复运行(循环) 会获取内部文件 当文件访问完了返回null
        unzip(src,dest);



        // 4.压缩 把每一个文件/文件夹看成ZipEntry对象放到压缩包中
        // 压缩文件 创建压缩包
        File dest1 = new File("D:\\22820\\Desktop\\code\\java");
        // 压缩方法
        toZip(src,dest1);


        // 压缩文件夹
        /*
        File src = new File("D:\\aaa待压缩文件夹");

        File destParent = src.getParentFile(); 父级路径

        File dest = new File(destParent,src.getName() + ".zip"); 父级路径下的压缩包

        创建压缩流关联压缩包
        ZipOutputStream zos = new ZipOutputStream(new FileOutputStream(dest));

        获取每个文件 放入压缩包
        toZip(src,zos,src.getName());

        释放资源

         */


        System.out.println("-------------------------------------------------");

        /* Commons-io
            使用步骤
                1.在项目中创建一个文件夹：lib
                2.将jar包复制粘贴到lib文件夹
                3.右键点击jar包，选择Add as Library->点击OK
                4.在类中导包使用

            常用方法
                1.FileUtils类(文件相关)
                static void copyFile(File srcFile, File destFile)               复制文件
                static void copyDirectory(File srcDir, File destDir)            复制文件夹 直接复制出新文件夹
                static void copyDirectoryToDirectory(File srcDir, File destDir) 复制文件夹 直接赋值一个原文件夹出来 多一层文件夹
                static void deleteDirectory(File directory)                     删除文件夹
                static void cleanDirectory(File directory)                      清空文件夹
                static String readFileToString(File file, Charset encoding)     读取文件中的数据变成成字符串
                static void write(File file, CharSequence data, String encoding) 写出数据

                2.IOUtils类（流相关）
                public static int copy(InputStream input, OutputStream output)  复制文件
                public static int copyLarge(Reader input, Writer output)        复制大文件
                public static String readLines(Reader input)                    读取数据
                public static void write(String data, OutputStream output)      写出数据

            操作
                1.右击项目新建目录 名称lib
                2.选择commons-io资料 粘贴到lib里
                3.右击commons-io 最下方添加到库
                4.在当前文件中导入这个类
         */

        // 复制文件
        // src待复制文件 和dest复制文件/压缩文件(上一部分)都准备好了
        FileUtils.copyFile(src,dest);

        // 复制文件夹
        File src2 = new File("D:\\22820\\Desktop\\code\\java\\aaa");
        File dest2 = new File("D:\\22820\\Desktop\\code\\java\\bbb");
        FileUtils.copyDirectory(src2,dest2);


        System.out.println("-------------------------------------------------");

        /* Hutool
            IoUtil              流操作工具类
            FileUtil            文件读写和操作的工具类
            FileTypeUtil        文件类型判断工具类
            WatchMonitor        目录、文件监听
            ClassPathResource   针对ClassPath中资源的访问封装
            FileReader          封装文件读取
            FileWriter          封装文件写入

            file：根据参数创建一个file对象 父级路径不存在报错
            touch：根据参数创建文件 父级路径不存在创建父级路径
            writeLines:把集合中的数据写出到文件中，覆盖模式。
            appendLines：把集合中的数据写出到文件中，续写模式。
            readLines：指定字符编码，把文件中的数据，读到集合中。
            readUtf8Lines：按照UTF-8的形式，把文件中的数据，读到集合中
            copy：拷贝文件或者文件夹

            FileUtil.file("D:\\22820\\Desktop\\code\\java\\aaa"); // 创建文件对象 可以拼接路径
            file.createNewFile();
            file.touch(file);
         */



        System.out.println("-------------------------------------------------");
    }

    // 解压方法
    public static void unzip(File src, File dest) throws IOException {
        // 解压本质: 把压缩包中每一个ZipEntry按照层级拷贝到本地另一个文件夹中

        // 1.创建解压缩流 用来读取压缩包中数据
        ZipInputStream zip = new ZipInputStream(new FileInputStream(src));

        /* 2.读取 获取每一个zipentry对象  ctrl alt v自动补全左边
        ZipEntry nextEntry = zip.getNextEntry();

        System.out.println(nextEntry);
         */


        ZipEntry entry;
        while((entry = zip.getNextEntry()) != null){
            System.out.println(entry);

            // 判断 文件 文件夹
            if(entry.isDirectory()){
                // 文件夹
                // 在dest内部新建文件
                File file = new File(dest,entry.toString());
                file.mkdirs();

            }else{
                // 文件
                FileOutputStream fos = new FileOutputStream(new File(dest,entry.toString()));
                int b;
                while((b=zip.read()) != -1){
                    // 写到目的地
                    fos.write(b);
                }
                fos.close();
                zip.closeEntry();  // 压缩的一个文件处理完了
            }
        }
        zip.close();
    }

    // 压缩文件方法
    public static void toZip(File src,File dest) throws IOException {
        // 1.创建压缩流关联压缩包
        ZipOutputStream zos = new ZipOutputStream(new FileOutputStream(new File(dest,"a.zip")));
        // 2.写出 创建ZipEntry对象 表示压缩包里面的每一个文件和文件夹
        ZipEntry entry = new ZipEntry("a.txt");     // 压缩包里的路径
        // 3.把ZipEntry对象放到压缩包当中
        zos.putNextEntry(entry);

        // 4.数据 把src文件中的数据写到压缩包当中
        FileInputStream fis = new FileInputStream(src);
        int b;
        while((b= fis.read()) != -1){
            zos.write(b);
        }

        zos.closeEntry();
        zos.close();
    }

    // 压缩文件夹方法
    public static void toZip(File src,ZipOutputStream zos,String name) throws IOException { // String name 压缩包内部路径
        // 1.进入src文件夹
        File[] files = src.listFiles();

        // 2.遍历得到每个文件
        for(File file:files){
            // 3.判断是文件
            if(file.isFile()){
                ZipEntry entry = new ZipEntry(name+"\\"+file.getName()); // 此处“”如果写file 输出绝对路径
                zos.putNextEntry(entry);

                // 读取文件数据 放到压缩包里
                FileInputStream fis = new FileInputStream(file);

                int b;
                while((b = fis.read()) != -1){
                    zos.write(b);
                }

                fis.close();
                zos.closeEntry();
            }else{
                // 4.判断文件夹 递归
                 toZip(file,zos,name+"\\"+file.getName());
            }
        }
    }

}
