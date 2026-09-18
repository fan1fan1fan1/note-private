import java.util.*;
import java.util.function.Consumer;

public class collection1 {
    public static void main(String[] args) {
        /* 集合体系结构
            1.两个接口
            Collection 单列集合 一次只能添加一个元素
            Map 双列集合 每次添加一对元素
        */



        /* 2.对应内容
            Collection 下属各有一些实现类
                List 有序可重复有索引
                Set 无序不重复无索引
            Map 键值对
         */



        /* 3.Collection包含的实现类
            List:
                ArrayList
                LinkedList
                Vector
            Set:
                TreeSet
                HashSet
                LinkedHashSet
         */



        /* Collection 单列集合的祖宗接口 功能是全部单列集合都可以继承使用的

            接口 不能直接创建对象 创建实现类的对象

            方法:
            添加 boolean add(E e)     如果是list系列 永远返回true 如果是set系列 已存在有重复返回false
            删除 boolean remove(E e)  不能通过索引删除 只能通过对象删除 删除成功返回true 删除元素不存在返回false
            int size()
            boolean isEmpty()
            清空 void clear()
            判断是否包含某元素 boolean contains(object obj)  equals原理 如果集合中存储自定义对象 需要重写equals方法
            Object[] toArray()
         */

        Collection c = new ArrayList();
        c.add("a");
        System.out.println(c);

        System.out.println(c.size());
        System.out.println(c.isEmpty());
        System.out.println(c.contains("a"));
        System.out.println(c.toArray());
        System.out.println(c.remove("a"));
        System.out.println(c);
        c.clear();
        System.out.println(c);




        Collection<String> c1 = new ArrayList<>();
        c1.add("a");
        System.out.println(c1);

        System.out.println(c1.size());
        System.out.println(c1.isEmpty());
        System.out.println(c1.contains("a"));
        System.out.println(c1.toArray());
        System.out.println(c1.remove("a"));
        System.out.println(c1);
        c1.clear();
        System.out.println(c1);



        /* Collection的遍历方式
            1.迭代器遍历 不依赖索引 集合专用的遍历方式
            2.增强for遍历
            3.Lambda表达式遍历

            迭代器遍历 Iterator
                Iterator<E> iterator() 返回迭代器对象，默认指向当前集合的0索引
                boolean hasNext()      判断当前位置是否有元素 有返回true 没有返回false
                E next()               获取当前位置的元素 并将迭代器对象移给下一个位置

            1.当迭代器指向了数据最末false时 报错 NoSuchElementException
            2.迭代器遍历完毕指针不会复位
            3.循环只能用一次next方法 如果需要多次遍历 只能重新创建迭代器对象
            4.迭代器遍历过程中不能用集合对象修改元素
         */



        List<String> list = new ArrayList<>();
        list.add("a");
        list.add("b");
        list.add("c");
        list.add("d");

        Iterator<String> it = list.iterator(); // 创建迭代器 默认指向0索引

        while(it.hasNext()){ // 判断当前指向位置是否有元素 有true执行循环 没有false跳出循环
            String str1 = it.next(); // 获取当前指针元素 移动指针
            System.out.println(str1);

            // 迭代器遍历过程中不能用集合对象修改元素
            // list.remove(str1); 会报错 ConcurrentModificationException

            // 迭代器遍历过程中如果要删除元素 只能用迭代器的删除方法
            if (str1.equals("b")){
                it.remove();
            }

            System.out.println(list);
        }

        Iterator<String> it2 = list.iterator(); // 如果需要多次遍历 重新创建迭代器对象
        while(it2.hasNext()){
            String str2 = it2.next();
            System.out.println(str2);

            // 如果hasNext循环中用了两次next方法 在循环最后一轮的最后一个next方法会报错 因为指针指向了空
        }



        /* 增强for遍历
            底层是一个迭代器 为了简化迭代器代码
            适用于所有的单列集合和数组

            格式:
            for(元素数据类型 变量名 : 数组名/集合名){
                循环体;
            }

            快捷输入 集合名字.for
                    list.for
         */

        for (String str : list){
            // str是一个第三方变量中间变量 过程中表示集合中的每一个数据 修改str值 不改变结果
            // 在此处对str进行修改 结果不会改变

            System.out.println(str);
        }



        /* Lambda表达式遍历
            适用于所有的单列集合和数组

            格式:
            集合名.forEach(变量名 -> {
                循环体;
            });

            Lambda表达式
            default void forEach(Consumer<? super T> action) {
                Objects.requireNonNull(action);
                for (T t : this) {
                    action.accept(t);
                }
            }
         */

        // 匿名内部类
        list.forEach(new Consumer<String>() {
            @Override
            public void accept(String str) {  // 此处str仍然是中间变量
                System.out.println(str);
            }
        });

        // Lambda表达式
        list.forEach(str -> {
            System.out.println(str);
        });

        list.forEach(str -> System.out.println(str));

    }
}
