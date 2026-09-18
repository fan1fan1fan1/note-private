import java.io.*;
import java.nio.charset.Charset;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class Zlaji0 {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        // 1.创建待解压缩文件
        File src = new File("D:\\22820\\Desktop\\code\\java\\a.zip");

        // 2.创建文件目的地
        File dest = new File("D:\\22820\\Desktop\\code\\java");

        // 3.解压 引用函数
        unzip(src, dest);
    }

    public static void unzip(File src, File dest) throws IOException {
        // 解压本质: 把压缩包中每一个ZipEntry按照层级拷贝到本地另一个文件夹中

        // 1.创建解压缩流 用来读取压缩包中数据
        ZipInputStream zip = new ZipInputStream(new FileInputStream(src));

        // 2.读取 获取每一个zipentry对象  ctrl alt v自动补全左边
        ZipEntry nextEntry = zip.getNextEntry();

        System.out.println(nextEntry);
    }
}
