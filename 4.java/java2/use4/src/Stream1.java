import java.util.*;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.IntFunction;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Stream1 {
    public static void main(String[] args){
        /* 创建不可变集合
            of方法

            static<E> List<E> of(E...elements) 指定为list类型
            static<E> Set<E> of(E...elements) 指定为set类型
            static<K,V> Map<K, V> of(E...elements) 指定为map类型

            细节set: 创建set类型时 里面的参数必须是唯一的
            细节map: map集合是成对出现的 默认0 1索引为一对 2 3索引为一对
                    键是不能重复的
                    map里的of方法 参数有上限 最多20个参数 10对
          */

        // 实例 list类型
        List<String> list = List.of("a","b");
        System.out.println(list.get(0)); // 获取索引元素
        for(String s : list){
            System.out.println(s);
        }


        // 案例 创建一个普通集合 变成不可变集合
        HashMap<String, String> hm = new HashMap<>();
        hm.put("a","b");

        // 创建不可变集合
        Map<String, String> map = Map.copyOf(hm);
        System.out.println(map);



        /* Stream
            流是数据渠道 用于操作数据源(集合、数组等)所生成的元素序列
            集合讲的是数据 流讲的是计算

            注意:
                1.流自己不会存储元素
                2.流不会改变源对象 会返回一个持有结果的新流
                3.流操作是延迟执行的 这意味着他们会等到需要结果的时候才执行

            结合了Lambda表达式 简化操作

            1.得到一条流水线 把数据放上去
                单列集合 default Stream<E> stream() Collections
                双列集合 无 通过key set或entry set转成单列结合
                数组 Arrays.stream(T[] array) Arrays工具类中静态方法
                一堆零散数据 value.of(T...value) Stream接口中静态方法
            2.使用中间方法 进行筛选、映射等操作
            3.使用终端方法 进行匹配、查找、聚合等操作
            利用Stream流的的api进行操作
         */

        ArrayList<String> list2 = new ArrayList<>();
        list2.add("张无忌");
        list2.add("周芷若");
        list2.add("赵敏");

        list2.add("张强");
        list2.add("张三丰");
        /* 把所有以“张”开头的元素存储到新集合中
           把“张”开头的，长度为3的元素再存储到新集合
           遍历打印最终结果
        */

        // 1.一般方法
        /*
        ArrayList<String> list3 = new ArrayList<>();
        for(String s : list2){
            if(s.startsWith("张")){
                list3.add(s);
            }
        }
        for(String s : list3){
            if(s.length() == 3){
                list3.add(s);
            }
        }
        System.out.println(list3);
         */

        // 2.Stream流操作
        list2.stream().filter(s -> s.startsWith("张"))
            .filter(s -> s.length() == 3)
            .forEach(System.out::println);



        // 1.单列集合获取Stream流
        ArrayList<String> list5 = new ArrayList<>();
        Collections.addAll(list5,"a","b","c");

        // 2.获取流水线 放上去
        Stream<String> stream1 = list5.stream();

        // 3.使用终结方法打印一个流水线上所有数据
        list5.stream().forEach(s -> System.out.println(s));



        // 1.双列集合获取Stream流
        // 创建集合
        HashMap<String,Integer> hm2 = new HashMap<>();

        // 2.添加数据
        hm2.put("aaa", 111);
        hm2.put("bbb", 222);

        // 3.获取Stream流 方法一
        hm2.keySet().stream().forEach(s -> System.out.println(s));
        // 方法二
        hm2.entrySet().stream().forEach(s -> System.out.println(s));



        // 1.数组获取Stream流
        // 创建数组
        int[] arr = {1,2,3};

        // 2.获取Stream流
        Arrays.stream(arr).forEach(s -> System.out.println(s));

        String[] arr2 = {"a", "b", "c"};
        Arrays.stream(arr2).forEach(s -> System.out.println(s));



        // 1.零散数据(同数据类型)获取Stream流
        Stream.of(1,2,3).forEach(s -> System.out.println(s));
        Stream.of("a", "b", "c").forEach(s -> System.out.println(s));

        // 数组对象使用零散数据的方法 必须是引用类型才可用



        /* Stream流中间方法
            中间方法会返回新的Stream流 原来的Stream流只能使用一次 建议使用链式编程
            修改Stream流中数据 不会改变原集合或数组中数据

            filter()   过滤
            limit()    获取前几个元素
            skip()     跳过前几个元素
            distinct() 元素去重，依赖(hashCode和equals方法 需要重写)
            concat()   合并a和b两个流为一个流
            map()      转换流中的数据类型
         */

        ArrayList<String> list3 = new ArrayList<>();
        Collections.addAll(list3,"a","b","c");

        // 过滤filter 匿名内部类+lambda表达式
        list3.stream().filter(new Predicate<String>() {
            @Override
            public boolean test(String s) {
                // 如果返回值为true表示当前数据留下 如果返回值为false表示当前数据过滤
                s.startsWith("a");
                return false;
            }
        }).forEach(s -> System.out.println(s));

        // 简写
        list3.stream().filter(s -> s.startsWith("a"));



        // 输出前部分limit
        list3.stream().limit(1).forEach(s -> System.out.println(s));

        // 输出后部分skip
        list3.stream().skip(1).forEach(s -> System.out.println(s));

        // 去重 如果list里是Student等引用数据对象 需要手动重写equal和。。方法
        list3.stream().distinct().forEach(s -> System.out.println(s));

        // 合并两个流concat 同数据类型
        Stream.concat(list3.stream(),list5.stream()).forEach(s -> System.out.println(s));


        /* 类型转换map
            第一个类型 流中原本的数据类型
            第二个类型 要转变之后的类型

            apply的形参s 表示每一个流数据
            返回值 表示转换后的数据

            map方法执行完毕后 流上的数据变成整数Integer
            所以在下方forEach当中 s依次表示每一个数据
         */
        ArrayList<String> list4 = new ArrayList<>();
        Collections.addAll(list4, "a-1","b-2");

        list4.stream().map(new Function<String,Integer>(){
            @Override
            public Integer apply(String s){
                String[] arr = s.split("-");  // 根据-把数据隔开

                // 依次将每一组数据分开 a,1  b,2 每次的arr[1]都指向数字
                String ageString = arr[1];
                int age = Integer.parseInt(ageString);
                return age;
            }
        }).forEach(s -> System.out.println(s));

        // 简化
        list4.stream().map(s -> Integer.parseInt(s.split("-")[1]));



        /* Stream流的终结方法
            1.forEach() 遍历
            2.count() 统计
            3.toArray() 收集流中的数据 放到数组中
            4.collect() 收集流中的数据 放到集合中
         */


        /* 1.forEach() 遍历
            Consumer的泛型 表示流中数据的类型
            accept方法的形参s 依次表示流里面的每一个数据
         */
        list4.stream().forEach(new Consumer<String>() {
            @Override
            public void accept(String s) {
                System.out.println(s);
            }
        });

        // 简写
        list4.stream().forEach(s -> System.out.println(s));


        // 2.count() 统计
        long count = list4.stream().count();
        System.out.println(count);


        // 3.toArray() 收集数据放到数组中
        Object[] arr1 = list4.stream().toArray();
        System.out.println(Arrays.toString(arr1));


        /* IntFunction的泛型: 具体类型的数据
            apply的形参: 流中数据的个数 变成数组的长度保持一致
            apply的返回值: 具体类型的数组
            方法体: 就是创建数组
         */
        String[] arr4 = list4.stream().toArray(new IntFunction<String[]>() {
            @Override
            public String[] apply(int value) {
                return new String[value];
            }
        });
        // String[] arr4 = list4.stream().toArray(value -> new String[value]);

        System.out.println(Arrays.toString(arr4));



        /* collect收集方法
            collect(Collector collector)

         */
        Collections.addAll(list4); // list4,"元素1","元素2"


        // 按需求收集1 如果我们要求把数字为1的收集起来 放在list集合中
        List<String> newlist1 = list4.stream()
                .filter(s -> "1".equals(s.split("-")[1]))
                .collect(Collectors.toList());

        // 按需求收集2 如果我们要求把数字为1的收集起来 放在set集合中
        Set<String> newList2 = list4.stream()
                .filter(s -> "1".equals(s.split("-")[1]))
                .collect(Collectors.toSet());
        System.out.println(newList2);



        /* 按需求收集3 如果我们要求把数字为1的收集起来 放在map集合中
            如果元素属性一共有三个值 我以一种为共性收集起来 就不用这个作为新map元素
            比如元素人 属性为姓名性别年龄 我要收集所有男性
            那么我设置 键:姓名 值:年龄

            map集合中键不能重复 否则会报错
         */

        /* Map<String, Integer> map = list.stream()
                .filter(s -> "男".equals(s.split("-")[1]))
                .collect(Collectors.toMap(new Function<String, String>(){
                                               @Override
                                               public String apply(String s){
                                                    return null;
                                               }
                                            },
                        new Function<String,Integer>(){
                            @Override
                            public Integer apply(String s){
                                return null;
                            }
                        }));

             简写 lambda表达式
             list.stream().filter(s -> "男".equals(s.split("-")[1]))
                        .collect(Collectors.toMap(s -> s.split("-")[0],    键的生成规则
                                s -> Integer.parseInt(s.split("-")[2])));  值的生成规则

             System.out.println(map);
         */

        /* toMap(new Function<String, String>(), new Function<String,Integer>())
                    键的生成规则                      值的生成规则

              Function<类型1, 类型2> 类型1表示流中每一个数据类型 类型2表示map集合中键、值的数据类型

              apply中 s依次表示流中每一个数据
                     方法体: 生成键、值的代码   返回值: 已经生成的键、值
         */



        /* 案例1
            定义一个集合 并添加一些整数 1 2 3 4 5 6 7 8 9 10
            过滤奇数 只留下偶数 并将结果保存起来
         */
        ArrayList<Integer> list1 = new ArrayList<>();
        Collections.addAll(list1, 1,2,3,4,5,6,7,8,9,10);

        /* 添加元素的方法
            1. list.add() 一个一个添加
            2. Collections.addAll() 批量添加
         */

        // 过滤奇数 只留下偶数 果将结果保存起来
        ArrayList<Integer> newlist = new ArrayList<>();
        list1.stream().filter(s -> s % 2 == 0)
                .collect(Collectors.toCollection(() -> newlist));

        System.out.println(newlist);



        /* 案例2
            定义一个ArrayList集合 添加以下字符串
                "z,23","l,24","w,25"
            过滤出所有年龄大于23的人 并将结果保存起来 姓名为键 年龄为值
         */
        ArrayList<String> list6 = new ArrayList<>();
        Collections.addAll(list6, "z,23","l,24","w,25");

        /* 过滤出所有年龄大于23的人 并将结果保存起来 姓名为键 年龄为值 */
        Map<String, Integer> map1 = list6.stream()
                .filter(s -> Integer.parseInt(s.split(",")[1]) > 23)
                .collect(Collectors.toMap(s -> s.split(",")[0],
                        s -> Integer.parseInt(s.split(",")[1])));
        /* 我要判断年龄大于23
            首先我要把年龄拿出来 通过，把字符隔开  s.split(",")
            然后取出索引[1]                   s.split(",")[1]
            再变成int类型                     Integer.parseInt(s.split(",")[1])
            判断是否于于23                    Integer.parseInt(s.split(",")[1]) > 23
            如果是 那么我把索引[0]拿出来 打印     s.split(",")[0]
         */

        System.out.println(map1);



        /* 案例3
            现有两个集合 分储存储了6个男生的姓名年龄和6个女生的姓名年龄
            现在我要把这个两个集合合并起来 姓名为键 年龄为值
            并把演员信息封装成actor对象  String->actor 类型转换 map
         */
        ArrayList<String> list7 = new ArrayList<>();
        Collections.addAll(list7, "z,23","l,24","w,25");
        ArrayList<String> list8 = new ArrayList<>();
        Collections.addAll(list8, "a,23","b,24","c,25");

        Map<String, Actor> map2 = Stream.concat(list7.stream(), list8.stream()) // concat合并
                .collect(Collectors.toMap(s -> s.split(",")[0],   // 类型转换
                        s -> new Actor(s.split(",")[0], Integer.parseInt(s.split(",")[1]))));
                               // 相当于在这创建了一个Arraylist          String转换成int
        System.out.println(map2);


    }
    static class Actor{
        String name;
        int age;

        public Actor(String name, int age) {
            this.name = name;
            this.age = age;
        }
    }
}
