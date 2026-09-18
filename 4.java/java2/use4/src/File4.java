import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

public class File4 {
    public static void main(String[] args) throws IOException {
        /* 比如当我们进行拼图游戏时
            玩到一半需要存档
            此时需要一个文件的位置用于传输 和 一个传输的方法
            这个文档的位置为File 即路径
            这个传输的方法是IO流

            我们把路径分为相对路径和绝对路径 相对路径是不带盘符的
            相对路径 "a.txt"  "abc\\a.txt"
            绝对路径 "C:\\a.txt"  "C:\\abc\\a.txt"

            File对象就表示一个路径 可以是文件路径 也可以是文件夹路径
            这个路径可以存在也可以不存在

            方法
            public File(String pathname)            根据文件路径创建文件对象
            public File(String parent, String child)根据父路径名字符串和子路径名字符串创建文件对象
            public File(File parent, String child)  根据父路径对应文件对象和子路径名字符串创建文件对象
         */

        // 根据字符串表示的路径 变成file对象
        String str = "D:\\User\\alienware\\Desktop\\a.txt";
        File f1 = new File(str);  // 此时str不再是一个字符串了 而是一个真实的路径
        System.out.println(f1);


        // 父级路径 C:\\Users\\a\\d\\v
        // 子级路径 v

        String parent = "C:\\Users\\a\\d\\v";
        String child = "v";
        File f2 = new File(parent, child);
        System.out.println(f2);

        File f3 = new File(parent + "\\" + child);
        System.out.println(f3);

        /* 转义字符 \  在Linux系统中是/
            java底层第一步是获取你的操作系统 根据你的操作系统 使用不同的路径分隔图
            因此使用构造方法更好 不用把代码写死
         */
        File f4 = new File(parent,child);
        System.out.println(f4);



        /* File常见成员方法
            判断获取
            public boolean isDirectory()判断此路径名表示的File是否为文件夹
            public boolean isFile()判断此路径名表示的File是否为文件
            public boolean exists()判断此路径名表示的File是否存在
            public long length()返回文件的大小（字节数量）
            public String getAbsolutePath()返回文件的绝对路径
            public String getPath()返回定义文件时使用的路径
            public String getName()返回文件的名称，带后缀
            public long lastModified()返回文件的最后修改时间（时间毫秒值）

            创建 删除
            public boolean createNewFile()创建一个新的空的文件
            public boolean mkdir()创建单级文件夹
            public boolean mkdirs()创建多级文件夹
            public boolean delete()删除文件、空文件夹

            获取遍历
            public String[] list()返回目录下的所有文件和文件夹的名称数组
            public File[] listFiles()返回目录下的所有文件和文件夹的File数组
         */

        // 判断
        System.out.println(f1.isDirectory());
        System.out.println(f1.isFile());
        System.out.println(f1.exists());
        System.out.println(f1.getAbsolutePath());
        System.out.println(f1.getPath());
        System.out.println(f1.lastModified());

        // 单位字节  果果是M或者G 就除以1024 除以一次1024->M 除以第二次1024->G
        // 这个方法不能获取文件夹大小 获取文件夹大小需要累加所有文件
        System.out.println(f1.length());

        // a.txt -> a文件名、txt扩展名    文件夹:返回文件夹名
        System.out.println(f1.getName());


        /* 1.createNewFile()
             1.如果当前路径不存在 返回true 如果已经存在一个了 返回false  路径是唯一的
             2.如果父级路径不存在 报错IOException
             3.该方法只能创建文件 可以没有后缀名
         */
        File f5 = new File("D:\\22820\\Desktop\\code\\java\\a.txt");
        boolean b = f5.createNewFile();  // 此处异常选择第一个
        System.out.println(b);

        // 2.mkdir() 创建文件夹 目录
        File f6 = new File("D:\\22820\\Desktop\\code\\java\\a");
        boolean b1 = f6.mkdir();
        System.out.println(b1);

        // 3.mkdirs() 创建多级文件夹
        File f7 = new File("D:\\22820\\Desktop\\code\\java\\a\\b");
        boolean b2 = f7.mkdirs();
        System.out.println(b2);

        /* 4.delete 只能删除文件和空文件夹
            如果删除的是文件，则直接删除，不走回收站。
            如果删除的是空文件夹，则直接删除，不走回收站
            如果删除的是有内容的文件夹，则删除失败
         */
         System.out.println(f5.delete());
         System.out.println(f6.delete());

         /* 5.listFiles()获取遍历
            file的路径不存在或是文件时 返回null
            空文件返回长度为0的数组
            需要权限的文件返回null
          */
         File[] files = f7.listFiles();
         for(File file : files){
            System.out.println(file);
         }



        // 案例一 在aaa文件夹中创建一个a.txt
        // 1.如果aaa已经存在了 此处创建失败
        File file = new File("myfile\\aaa");
        // 2.创建新文件夹
        file.mkdir();
        // 3.拼接父级路径和子级路径
        File src = new File(file,"a.txt"); // 创建文件
        /*  boolean bb = src.createNewFile();
            if(bb){ System.out.println("创建成功"); }
            else{ System.out.println("创建失败"); }
         */


        // 案例二 寻找文件夹中以avi结尾的文件(不考虑子文件夹)
        File file1 = new File("D:\\22820\\Desktop\\code\\java\\aa");
        boolean b3 = haveAVI(file);  // 寻找函数
        System.out.println(b3);


        /* 案例三 寻找文件夹中以avi结尾的文件(考虑子文件夹)
            1.进入文件夹 2.遍历数组 3.判断(文件) 4.判断(文件夹)
         */
        File src1 = new File("D:\\22820\\Desktop\\code\\java\\aa");
        findAVI(src);

    }

    // 寻找函数
    public static boolean haveAVI(File file) {
        if(file == null || !file.isDirectory()){
            return false;
        }
        File[] files = file.listFiles();  // files.for tap
        for (File f : files) {
            if (f.isFile() && f.getName().endsWith(".avi")) {
                return true;
            }
        }

        return false;
    }

    public static boolean findAVI(File src){
        if(src == null || !src.isDirectory()){
            return false;
        }

        // 1.进入文件夹
        File[] files = src.listFiles();  // files.for tap
        // 2.遍历数组
        for (File f : files) {
            if (f.isFile()){
                // 3.判断 文件
                String name = f.getName();
                if(name.endsWith(".avi")){
                    System.out.println(f);
                }
            }
            else{
                // 4.判断 文件夹
                findAVI(f);  // 递归 再次遍历子文件夹
            }
        }
        return false;
    }
}
