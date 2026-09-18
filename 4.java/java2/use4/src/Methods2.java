import java.util.*;
import java.util.function.Function;
import java.util.function.IntFunction;
import java.util.stream.Collectors;

import static java.lang.Integer.parseInt;

public class Methods2 {
    public static void main(String[] args){
        // 方法引用 把已经有的方法拿过来用 当作函数式接口抽象方法的方法体

        /* 假如我有一个排序函数 需要设置排序规则
            Arrays.sort(arr, XXX)

            XXX此处我应该写一个声明 然后在下方重写函数 return o2-o1

            但如果此时我已经有一个排序函数了 我就可以直接把函数名引到XXX上
         */

        /* 方法引用条件
            1.引用处必须是函数式接口 比如Comparator compare
            2.被引用的方法必须存在
            3.被引用方法的形参和返回值需要跟抽象方法保持一致
            4.被引用方法的功能要能满足当前需求
         */

        // 需求: 创建一个数组 进行倒序排列
        Integer[] arr = {3,5,1,4,6};

        Arrays.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2-o1;
            }
        });

        // lambda表达式
        Arrays.sort(arr, (Integer o1, Integer o2)->{
            return o2-o1;
        });

        System.out.println(Arrays.toString(arr));

        // lambda表达式简化
        Arrays.sort(arr,(o1,o2)->o2-o1);

        // 方法引用
        // Arrays.sort(arr, 方法所在类名::方法名);
        Arrays.sort(arr, Methods2::method1);



        /* 排序规则
            Comparator接口的compare方法返回值规则：
            当returno1-02时，是升序排序（若
            结果为负，在前；为正，在前）。
            当returno2-01时，是降序 （倒序）排序（逻
            辑相反：若结果为负，02在前：为正.01在前
            ）。
            简单来说，return o2-o1是
            通过反转两个元素的比较逻辑
            从而让数组从大到小排列，
            达到倒序的目的
         */



        // 1.引用静态方法 类名::静态方法名
        ArrayList<String> list = new ArrayList<>();
        Collections.addAll(list, "1","2","3","4","5"); // 变成int类型
        list.stream().map(Integer::parseInt).forEach(s-> System.out.println(s));


        /* 2.引用成员方法 对象::成员方法
            其他类 其他类对象名::方法名
            本类   this::方法名
            父类   super::方法名
         */
        ArrayList<String> list1 = new ArrayList<>();
        Collections.addAll(list1, "张无忌","张强","周芷若");
        StringOperation so = new StringOperation(); // 只输出首字张 且长度为3的串
        list1.stream().filter(so::stringJudge).forEach(s -> System.out.println(s));

        /* 静态方法中不能使用this 因此我们得创建本类对象
            StringOperation so = new StringOperation();
            用本类的对象再去引用string judge方法
         */



        /* 3.引用构造方法 类名::new
            需要创建一个类 创建一个对象 才会引用构造方法

            封装成Student对象 String->Student:map() Student不能在本类
            原本String对象 经过map 变成了Student对象 输出结果为Student对象
         */
        ArrayList<String> list2 = new ArrayList<>();
        Collections.addAll(list2, "张无忌,15","周芷若,14","张强,23");
        Student2[] arr1 = list2.stream()
                .map(Student2::new)  // 每个String转Student
                .toArray(Student2[]::new);  // 转换为Student[]数组



        /* 根据上述我们可以知道
            引用本类的成员方法、父类的成员方法  不能写在静态方法中
            因为静态方法里没有this

            我们可以使用其他调用方式
            1.使用类名引用成员方法 类名::成员方法
                1.引用四条原则
                2.第一个参数表示被引用方法的调用者，决定了可以引用哪些类中的方法
                  在Stream流当中第一个参数: 流里的每一个数据
                  假设流里面的数据是字符串 只能引用String这个类中方法
                3.第二个参数到最后一个参数，跟被引用方法的形参保持一致，如果没有第二个参数
                  说明被引用的方法需要是无参的成员方法

                  也就是说 类名::方法名 只要被引用的方法形参和抽象方法的第二个参数后面保持一致即可

                但这种方法不能引用所有类的成员方法
                是要跟抽象方法的第一个参数有关 这个参数是什么类型 那么就只能引用这个类中方法

            2.引用数组的构造方法 数据类型[]::new

         */



        // 1.大小写转换
        ArrayList<String> list3 = new ArrayList<>();
        Collections.addAll(list3, "aaa","bbb","ccc");
        // 现在我要把所有字母变成大写 toUpperCase
        list3.stream().map(new Function<String, String>() {
            @Override
            public String apply(String s){
                return s.toUpperCase();
            }
        }).forEach(s -> System.out.println(s));

        // 使用类名引用成员方法
        list3.stream().map(String::toUpperCase).forEach(s-> System.out.println(s));


        // 2.引用数组的构造方法 把流中的数据收集到数组中
        ArrayList<Integer> list4 = new ArrayList<>();
        Collections.addAll(list4,1,2,3,4);
        Integer[] arr2 = list4.stream().toArray(new IntFunction<Integer[]>() {
            @Override
            public Integer[] apply(int value) {
                return new Integer[value];
            }
        });

        // 使用数组的构造方法
        List<Integer> list5 = new ArrayList<>();
        Collections.addAll(list5, 1,2,3,4,5);
        Integer[] arr3 = list5.stream().toArray(Integer[]::new);
        System.out.println(Arrays.toString(arr3));



        /* 3.集合中存储一些字符串的数据，比如：张三，23。
            收集到Student类型的数组当中

            引用了Stduent2里的构造方法 目的是把流里面的数据变成student2对象
         */
        //1.创建集合并添加元素
        ArrayList<String> list6 = new ArrayList<>();
        Collections.addAll(list6, "张无忌，15","周芷若，14");
        //2.先把字符串变成Student对象，然后再把Student对象收集起来
        Student2[] arr5 = list6.stream().map(Student2::new).toArray(Student2[]::new);
        //打印数组                       应该把new放在别的文件里 在这里创建了一个Stduent2的的数组对象 并把流中的数据收集到这个数组中
        System.out.println(Arrays.toString(arr5));



        /* 4.创建集合对象
            学生 包括:学生name age
            要求获取学生姓名放到数组中 使用方法引用完成
         */
        ArrayList<Student2> list7 = new ArrayList<>();
        Collections.addAll(list7, new Student2("张三",15), new Student2("李四",16));
        String[] arr6 = list7.stream().map(Student2::getName).toArray(String[]::new);
        // 把流中的数据收集到数组中             调用类中的成员方法
        // 也就是说 类名::方法名 只要被引用的方法形参和抽象方法的第二个参数后面保持一致即可
        System.out.println(Arrays.toString(arr6));



        /* 使用方法引用技巧:
            1.现在有没有一个方法符合我当前的需求
            2.如果有这样的方法，这个方法是否满足引用的规则
            静态   类名::方法名
            成员方法
            构造方法  类名::new

         */
















    }
    public static int method1(int num1,int num2){
        return num2 - num1;
    }

    /*public static int parseInt(String s){
        return parseInt(s,10);
      }*/

    static class StringOperation{
        boolean stringJudge(String s){
            return s.startsWith("张") && s.length() == 3;
        }
    }




}
