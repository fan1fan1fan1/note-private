import java.util.*;
import java.util.function.BiConsumer;
import java.util.function.Consumer;

public class Set6 {
    public static void main(String[] args){
        /* Set
            Collection有两种实现类 list和set
            set系列集合和list基础语法相同 但没有索引 无序

            存储字符串并遍历
            利用set系列集合 添加字符串 并使用多种方式遍历
            1.迭代器
            2.增强for
            3.Lambda表达式
         */

        // 1.创建set集合对象 利用多态
        Set<String> s = new HashSet<>();

        // 2.添加元素 返回布尔值
        boolean r1 = s.add("张三");
        boolean r2 = s.add("张三");

        System.out.println(r1); // true
        System.out.println(r2); // false
        System.out.println(s);  // [张三]

        // set集合元素去重 第一次添加添加成功 第二次添加添加失败
        // set集合无序 因此打印时没有顺序 随机



        // 3.迭代器遍历
        Iterator<String> it = s.iterator();
        while(it.hasNext()){
            String str = it.next();
            System.out.println(str);
        }

        // 4.增强for遍历
        for(String str : s){
            System.out.println(str);
        }

        // 5.Lambda表达式
        s.forEach(str -> System.out.println(str));



        /* HashSet
            底层是哈希表

            哈希表 用于数据增删改查 由数组、链表、红黑树组成
            哈希值 对象的整数表现形式 根据hashCode方法算出来的int类型的整数
                  该方法定义在Object类中 所有对象都可以调用
                  一般情况会重写hashCode方法 利用对象内部属性值计算哈希值

            如果不重写 就利用Object类方法 不同对象计算出来的哈希值是不同的
            如果重写了 不同对象只要属性值相同 计算出来的哈希值就是相同的
            小部分情况下 不同的属性值也可能计算出相同的哈希值(哈希碰撞)

            添加元素
            根据哈希值与数组长度计算出应存入的位置
            int index = (数组长度) & (哈希值);
            判断当前位置是否为null 如果是null就存入
            如果不是null 就利用equals方法比较属性值是否相同

            如果相同 就不存
            如果不同 就利用链表存储
                    原位置有元素 我们直接把新元素挂在旧元素下方 形成链表
                    再次添加 判断是否为相同元素 如果是不同元素 再次挂在下面
                    相同元素不存

            加载因子 0.75
            每次创建的数组一共有16个位置 16*0.75=12
            当数组内已经存了12个元素 数组会扩容成原来的2倍

            当链表长度大于8且数组长度大于64时 链表会自动转成红黑树
         */

        Student s1 = new Student("张三", 18);
        Student s2 = new Student("张三", 18);
        System.out.println(s1.hashCode());
        System.out.println(s2.hashCode());


        /*  1.HashSet无序 存取顺序不同
            2.HashSet没有索引
            3.HashSet不重复
         */



        /* 案例 利用HashSet去重
            创建一个存储学生对象的集合 存储多个学生对象 并遍历
            如果学生对象的成员变量相同 我们就认为是同一个对象
         */

        // 1.创建对象
        Student S1 = new Student("张三", 23);
        Student S2 = new Student("李四", 20);
        Student S3 = new Student("王五", 19);
        
        // 2.创建集合用于添加学生
        HashSet<Student> hs = new HashSet<>();

        // 3.添加元素
        System.out.println(hs.add(S1));  // true false
        System.out.println(hs.add(S2));
        System.out.println(hs.add(S3));

        // 4.打印集合
        System.out.println(hs);



        /* LinkedHashSet
            Collection -> Set -> HashSet -> LinkedHashSet

            LinkedHashSet有序、不重复、无索引 这里的有序指保证存储和取出元素的顺序一致
            底层仍然是哈希表 但除了元素外多了一个双链表(记录元素间地址值) 用于记录顺序

            双链表: 从第二个元素开始 形成双链表 第一个元素和第二个元素互相指向对方的地址

            添加元素时如果指向的位置已经有元素了 会把新元素放在原元素的下面 形成双链表
         */

        // 1.创建对象
        Student s3 = new Student("z",23);
        Student s4 = new Student("s",23);
        Student s5 = new Student("a",23);

        // 2.创建集合对象
        LinkedHashSet<Student> lhs = new LinkedHashSet<>();

        // 3.添加元素
        System.out.println(lhs.add(s3));
        System.out.println(lhs.add(s4));
        System.out.println(lhs.add(s5));

        // 4.打印集合
        System.out.println(lhs);



        /* TreeSet
            不重复、无索引、可排序(按照元素的默认规则由小到大排 ASCII码升序排列)
            底层逻辑是红黑树

            说 字符和字符串默认排序是按照字典顺序进行排列的 说法是错误的
            是巧合 刚好逻辑相同
         */

        // 1.创建TreeSet对象
        TreeSet<Integer> ts = new TreeSet<>();

        // 2.添加元素
        ts.add(4);
        ts.add(4);
        ts.add(6);

        // 3.遍历集合
        Iterator<Integer> it2 = ts.iterator();
        while(it.hasNext()){
            // Integer i = it2.next();
            int i = it2.next(); // 自动拆箱
            System.out.println(i);
        }

        // 增强for
        for (int t : ts) {
            System.out.println(t);
        }

        // Lambda
        ts.forEach(i-> System.out.println(i));



        // 1.创建对象
        Student s6 = new Student("z",23);
        Student s7 = new Student("s",23);
        Student s8 = new Student("a",23);

        // 2.创建集合对象
        TreeSet<Student> ts2 = new TreeSet<>();

        /*
        3.添加元素
        ts2.add(s6);
        ts2.add(s7);

        4.打印集合
        System.out.println(ts2); // 报错
        报错原因 在添加元素时 因为没比较字符串规则大小 TreeSet有序
         */


        /* TreeSet两种比较大小方式
            方法一 默认排序 自然排序 javabean类实现Comparable接口指定比较规则
                    改变class类名 implement 取消报错
            方法二 比较器排序 创建TreeSet对象时 传递比较器Comparator制定规则

            使用原则 默认都是用第一种 如果第一种不能满足要求 使用第二种
         */



        // 方法一 Student类实现Comparable接口 重写里面的抽象方法 在指定比较规则
        // 需要创建新的接口实现类Student2 不需要要重写hashcode和equal方法

        /* 1.创建集合
            o1表示要添加元素
            o2表示以添加元素
            返回值规则和之前相同
         */
        TreeSet<String> ts3 = new TreeSet<>(new Comparator<String>(){
            @Override
            public int compare(String o1, String o2){
                // 按照长度排序
                int i = o1.length() - o2.length();

                // 如果一样长则按照首字母排序
                i = i == 0 ? o1.compareTo(o2) : i;
                 // i == 0 使用默认方法比较大小    如果i不等于0 以上述判断结果为准



                /* 假设这个类中有很多属性 语文成绩 数学成绩 英语成绩 按照成绩排名排序
                    (语文>数学>英语)

                    int i = sum1 - sum2 总成绩差值
                    i = i == 0 ? this.getChinese() - o.getChinese() : i;
                    i = i == 0 ? this.getMath() - o.getMath() : i;

                    先比较总成绩 如果i==0 说明总成绩成绩相等 比较语文成绩 得到差值或者原来的i
                    如果仍然i==0 说明语文成绩也相等 比较数学成绩 得到差值或者原来的i
                    如果仍然i==0 说明数学成绩也相等 比较英语成绩 得到差值或者原来的i
                 */

                return i;
            }
        });

        // 2.添加元素
        ts3.add("a");
        ts3.add("b");
        ts3.add("c");

        // 3.打印集合
        System.out.println(ts3);



        /* 双列集合
            键值对 字典 键值对对象称Entry
            键不能重复 值可以重复
            键值一一对应 每一个键只有一个值
         */



        /* Map的常见API
            Map是双列集合的顶层接口 双列集合可继承使用Map的API

            put 添加
            remove 删除
            clear
            containsKey 判断包含的键
            containsValue 判断包含的值
            isEmpty
            size
         */

        // 1.创建对象
        Map<String,String> m = new HashMap<>();
             // 键  值


        // 2.添加元素
        m.put("a", "b");
        m.put("1", "2");
        m.put("c", "d");


        // 3.修改元素
        String value2 = m.put("1","3");

        // 3把2覆盖了 现在键值对输出时 1对应3
        System.out.println(value2); // 输出被覆盖的元素 2


        // 4.删除
        String res = m.remove("c");
        System.out.println(res);


        // 5.判断存在
        boolean k = m.containsKey("a");
        System.out.println(k);


        // 6.打印集合
        System.out.println(m);


        /* 双列集合 添加修改元素
            如果键不存在 直接把键值对对象添加到Map集合中 返回null
            如果键存在   覆盖原有键值对对象 把被覆盖的值(value)返回

            删除元素
            删除一个 将会删除整个键值对对象 并返回值(value)
         */



        /* 遍历
            1.键找值
                单列集合存储所有的键 遍历单列集合 get获取每个元素(键)对应的值

            2.依次获取键值对
                通过键值对对象进行遍历

            3.Lambda表达式
                default void forEach(BiConsumer<? super K, ? super V> action)
         */



        // 1.键找值
        Set<String> keys = m.keySet(); // 创建单列集合
        for(String key : keys){  // 遍历单列集合 得到每一个键
            System.out.println(key);

            // 通过键获取对应的值
            String value1 = m.get(key);
            System.out.println(key + "=" + value1);
        }



        // 2.依次获取键值对

        // 第一步 获取所有键值对对象 返回一个set集合
        // m.entrySet(); 然后按ctrl+alt+v
        Set<Map.Entry<String, String>> entries = m.entrySet();

        /* 另外一种做法
            导包 import java.util.Map.Entry;

            Set<Entry<String, String>> entries = m.entrySet();
         */

        // 第二步 遍历这个集合 得到每一个键值对对象
        for (Map.Entry<String, String> entry : entries) {
            // 调用get方法获取键和值
            String key = entry.getKey();
            String value = entry.getValue();
            System.out.println(key + "=" + value);

            // for循环过程: 先获取了第一个元素的key 然后获取第一个元素的value 然后循环获取第二个
        }



        // 3.Lambda表达式 遍历
        m.forEach((key,value) -> System.out.println(key + "=" + value));



        /* HashMap
            特点 1.HashMap是Map里面的一个实现类。
                2.没有额外需要学习的特有方法，直接使用Map里面的方法就可以了。
                3.特点都是由键决定的：无序、不重复、无索引
                4.HashMap跟HashSet底层原理是一模一样的，都是哈希表结构

            添加新元素时 如果位置上有元素 会把新元素挂在原元素下方
            如果长度超过数组&8(64)时 自动形成红黑树
         */



        /* 案例一
            创建一个HashMap集合 键是学生对象(Student) 值是籍贯(String)
            存储三个键值对元素 并遍历

            要求同名同年龄认为是同一个学生

            在类中重写方法
            @Override
            public boolean equals(Object o) {
                if (this == o) return true;
                if (o == null || getClass() != o.getClass()) return false
                Student student = (Student) o;
                return age == student.age && Objects.equals(name, student.name);
            }
            @Override
            public int hashCode() {
                return Objects.hash(name, age);
            }
            public String toString() {
                return "Student{name = " + name + ", age = " + age + "}";
            }
        }
         */



        /* 案例二
            某班80个学生 去四个经典 A B C D 每个学生只能选择一个景点 统计去哪个景点人最多

            统计思想 两种方法:
                1.计数器思想 定义一个count  ++
                2.Map集合 利用集合统计
                for(String name : list){
                    if(map.containsKey(name)){
                        map.put(name, map.get(name) + 1); 集合思想

                        int count = map.get(name); 计数器思想
                        count++;
                        map.put(name, count);
                    }else{
                        map.put(name, 1);
                    }
                }

            求最大值
            int max = 0;
            Set<Map.Entry<String, Integer>> entries = map.entrySet();
            for(Map.Entry<String, Integer> entry : entries){
                if(entry.getValue() > max){
                    max = entry.getValue();
                }
            }

            打印最大值
            for(Map.Entry<String, Integer> entry : entries){
                if(entry.getValue() == max){
                    System.out.println(entry.getKey() + "=" + entry.getValue());
                }
            }
         */



        // LinkedHashMap 有序 不重复 无索引 哈希表+双链表
        // 1.创建集合
        LinkedHashMap<String, Integer> L = new LinkedHashMap<>();

        // 2.添加元素
        L.put("a",123);

        // 3.遍历
        for(Map.Entry<String, Integer> entry : L.entrySet()){
            System.out.println(entry.getKey() + "=" + entry.getValue());
        }



        /* TreeMap
            不重复 无索引 可排序(对键排序 默认从小到大(规则可自拟))

            排序规则: 1.实现Comparable接口 指定排序规则
                    2.重写compareTo方法 创建集合时传递Comparator比较器对象 指定排序规则
         */



        /* 案例一
            键 整数id
            值 字符串表示商品名称
            要求 按照id升序排列 按照id降序排列
         */

        // 1.创建集合
        TreeMap<Integer, String> T = new TreeMap<>(new Comparator<Integer>() {
            // 自定义排序方法 方法二 重写compare方法
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        });

        // 2.添加元素
        T.put(1, "a");
        T.put(2, "b");
        T.put(3, "c");

        // 3.遍历
        for(Map.Entry<Integer, String> entry : T.entrySet()){
            System.out.println(entry.getKey() + "=" + entry.getValue());
        }



        /* 案例二
            键 学生对象
            值 籍贯
            要求 按照学生年龄升序排列 年龄一样按姓名字母排列 都相同视为同一人

            实现Comparable接口 指定排序规则
            class Student implements Comparable<Student>{
                @Override
                public int compareTo(Student o) {
                    int i = this.getAge() - o.getAge();
                    return i == 0 ? this.getName().compareTo(o.getName()) : i;
                }
            }
         */



        /* 统计思想 两种方法:
                1.计数器思想 定义一个count  ++
                2.Map集合 利用集合统计

            如果题目中没有对结果进行排序 默认使用 HashMap
            如果题目中要求对结果进行排序 就使用 TreeMap

            键表示要统计的内容
            值 统计次数
         */



        // eg.统计一个字符串 出现各个字母次数
        // 1.创建对象
        String S = "aaabbbccc";

        // 2.创建集合
        TreeMap<Character,Integer> tm = new TreeMap<>();

        // 3.遍历得到每一个字符
        for(int i = 0; i < S.length(); i++){
            char c = S.charAt(i);
            // 拿着c到集合中判断是否存在 如果存在就+一次 如果不存在就设置该字符 并为第一次出现 1

            if(tm.containsKey(c)){
                int count = tm.get(c);
                count++;
                tm.put(c,count);
            }
            else{
                tm.put(c,1);
            }
        }

        // 4.遍历集合 StringBuilder或者StringJoiner

        // StringBuilder
        StringBuilder sb = new StringBuilder();
        tm.forEach(new BiConsumer<Character, Integer>() {
            @Override
            public void accept(Character key, Integer value) {
                sb.append(key).append("(").append(value).append(")");
            }
        });
        System.out.println(sb);

        // StringJoiner
        StringJoiner sj = new StringJoiner("","","");
                                           // 开始标记  结束标记  间隔符号 都设置为0
        tm.forEach((key,value)->sj.add(key + "").add("(").add(value + "").add(")"));
        System.out.println(sj);               // 非字符串的数据 后边要 + ""

    }



    // 类
    class Student2 implements Comparable<Student2>{
        private String name;
        private int age;

        public Student2(){};

        public Student2(String name, int age){
            this.name = name;
            this.age = age;
        }

        public String getName(){
            return name;
        }
        public int getAge(){
            return age;
        }
        public void setName(String name){
            this.name = name;
        }
        public void setAge(int age){
            this.age = age;
        }

        public String toString(){
            return "Student{name = " + name + ", age = " + age + "}";
        }

        @Override
        public int compareTo(Student2 o) {
            // 在此处制定排序规则
            // 我想按照年龄升序进行排列
            System.out.println("this:" + this);
            System.out.println("o:" + o);
            return this.getAge() - o.getAge();

            /* 排序规则
                return this.getAge() - o.getAge();

                this表示要添加的元素
                o表示已有元素

                返回值
                如果为负数 说明要添加的元素小 存左边
                如果为正数 说明要添加的元素大 存右边
                如果为0 不存
             */
        }
    }



    static class Student{
        String name;
        int age;
        public Student(String name, int age){
            this.name = name;
            this.age = age;
        }

        @Override
        public boolean equals(Object o) {
            if (o == null || getClass() != o.getClass()) return false;
            Student student = (Student) o;
            return age == student.age && Objects.equals(name, student.name);
        }

        @Override
        public int hashCode() {
            return Objects.hash(name, age);
        }
    }

}
