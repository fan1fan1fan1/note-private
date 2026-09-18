import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class SetPlus7 {
    public static void main(String[] args){
        // 随机抽取案例 -> 斗地主

        // 1.计算n个数据和
        int[] arr = {1, 5, 6, 4, 8};
        int sum = getSum(arr);
        System.out.println(sum);



        /* 可变参数
            格式: 属性类型...姓名  int...args

            方法形参的个数是可以发生变化的 0 1 2 3
            不需要确定形参个数的计算方法

            在方法的形参中最多只能写一个可变参数
            可变参数 可理解为一个大胖子 有多少吃多少

            如果除了可变参数外还有其他形参 那么可变参数要写在最后
            如果把可变参数写在了前面 那么数据输入时所有的数据会被可变参数吃掉 后面的形参报错

            public static int getSun(int a, int...args);
         */



        /* Collections 集合工具类
            不是个集合

            addAll 批量添加元素
            shuffle 打乱

            public static <T> boolean addAll(Collection<T> c, T... elements)
            批量添加元素

            public static void shuffle(List<?> list)
            打乱List集合元素的顺序

            public static <T> void sort(List<T> list)
            排序

            public static <T> void sort(List<T> list, Comparator<T> c)
            根据指定的规则进行排序

            public static <T> int binarySearch (List<T> list, T key)
            以二分查找法查找元素

            public static <T> void copy(List<T> dest, List<T> src)
            拷贝集合中的元素

            public static <T> int fill (List<T> list, T obj)
            使用指定的元素填充集合

            public static <T> void max/min(Collection<T> coll)
            根据默认的自然排序获取最大/小值

            public static <T> void swap(List<?> list, int i, int j)
            交换集合中指定位置的元素
         */


        // 1.创建集合对象
        ArrayList<String> list = new ArrayList<>();

        // 2.批量添加元素
        Collections.addAll(list, "abc","bnn");

        // 3.打印集合
        System.out.println(list);

        // 4.打乱
        Collections.shuffle(list);

        System.out.println(list);



        // 2.根据班级里N个学生姓名年龄 实现随机点名器
        ArrayList<String> list2 = new ArrayList<>();
        Collections.addAll(list,"a","b","c");

        // 此处有两种方法 方法一 随机取索引
        Random r = new Random();
        int index = r.nextInt(list.size());
        String name = list.get(index);
        System.out.println(name);

        // 方法二 打乱 然后取索引0元素
        Collections.shuffle(list);
        String name2 = list.get(0);
        System.out.println(name2);



        // 3.根据班级N个学生进行随机抽取 要求男生概率0.7 女生概率0.3
        /* Random随机数 只能随机单个元素 不能影响范围和面

            方法: 假设N等于10 男生有1 2 3 4..人 女生有a b c d..人

            我们设随机抽取结果为1111111000  7个1 3个0
            如果抽取到1 就从男生中选一个 抽到0 就从女生中选一个
         */

        // 1.创建集合
        ArrayList<Integer> list3 = new ArrayList<>();

        // 2.添加数据
        Collections.addAll(list3,1,1,1,1,1,1,1);
        Collections.addAll(list3,0,0,0);

        // 3.打乱
        Collections.shuffle(list);

        // 4.随机抽取
        Random r3 = new Random();
        int index3 = r.nextInt(list3.size());
        int number = list3.get(index3);
        System.out.println(number);

        // 5.创建集合存储男女
        ArrayList<String> boyList = new ArrayList<>();
        ArrayList<String> girlList = new ArrayList<>();
        Collections.addAll(boyList,"1","2","3","4");
        Collections.addAll(girlList,"a","b","c","d");

        // 6.判断boyList还是girlList
        if(number == 1){
            // boy
            int boyIndex = r.nextInt(boyList.size());
            String name4 = boyList.get(boyIndex);
            System.out.println(name4);
        }
        else{
            // girl
            int girlIndex = r.nextInt(girlList.size());
            String name5 = girlList.get(girlIndex);
            System.out.println(name5);
        }



        /* java想添加多个数据 或者一次性存储多个数据方法
            1.for循环遍历输入是scanf
            2.Collections.addAll
         */



        // 4.仍然随机抽人 但被抽到的不会再次被抽到 直到循环结束 开启第二轮

        // 抽出一个删除一个 api remove删除方法 返回被删除值
        ArrayList<String> list4 = new ArrayList<>();
        Collections.addAll(list4,"a","b","c","d");
        Random r4 = new Random();
        int count = list4.size();

        /*
        for (int i = 0; i < list4.size(); i++) {
            int index4 = r.nextInt(list.size());
            String name7 = list.remove(index);
            System.out.println(name7);
        }
        报错 报错原因 每次进行循环 集合长度就减一 只能输出部分数据
         */
        ArrayList<String> list5 = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            // 删除过程
            int index4 = r.nextInt(count);
            String name7 = list4.remove(index);

            // 添加被删除的元素 方便第二次循环
            list5.add(name);

            System.out.println(name7);
        }

        // 一轮点名结束后 list原空 list新拥有所有元素 赋值给原来的元素 第二轮循环
        list4.addAll(list5);
        list5.clear();


    }

    // 1
    public static int getSum(int...args){
        int sum = 0;
        for(int i : args){
            sum += i;
        }
        return sum;
    }
}
