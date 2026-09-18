package practice;

import java.util.Arrays;
import java.util.Comparator;

public class test1 {
    public static void main(String[] args){
        /* 按照要求进行排序
            定义数组存储一些女朋友对象 利用Arrays中的sort方法进行排序
            要求1 属性有姓名 年龄 身高
            要求2 按照年龄大小进行排序 年龄相同的按身高排序 身高相同按照姓名排序

         */
        String s1 = "a";
        String s2 = "b";
        System.out.println(s1.compareTo(s2)); // 按照字典顺序比较字符



        // 定义数组
        Person1[] arr = new Person1[4];
        arr[0] = new Person1("a", 18, 1.8);
        arr[1] = new Person1("b", 19, 1.9);
        arr[2] = new Person1("c", 18, 1.7);
        arr[3] = new Person1("d", 17, 1.6);

        // 排序
        Arrays.sort(arr, (o1, o2) -> {
            // 年龄相同的按身高排序
            if(o1.getAge() == o2.getAge()){
                return (int)(o1.getHeight() - o2.getHeight());
            }
            // 年龄不同的按年龄排序
            else{
                return o1.getAge() - o2.getAge();
            }
        });


        Arrays.sort(arr, new Comparator<Person1>() {
            @Override
            public int compare(Person1 o1, Person1 o2) {
                double temp = o1.getAge() - o2.getAge();

                // 按年龄排序
                if(temp == 0){
                    temp = o1.getAge() - o2.getAge();
                }

                // 按身高排序
                if(temp == 0){
                    temp = (int)(o1.getHeight() - o2.getHeight());
                }
                // 按姓名排序
                if(temp == 0){
                    temp = o1.getName().compareTo(o2.getName());
                }

                if(temp > 0){
                    return 1;
                }
                else if(temp < 0){
                    return -1;
                }
                else{
                    return 0;
                }

            }
        });



        // Lambda排序
        Arrays.sort(arr, (o1, o2) -> {
            double temp = o1.getAge() - o2.getAge();

            // 年龄相同的按身高排序
            if(o1.getAge() == o2.getAge()){
                return (int)(o1.getHeight() - o2.getHeight());
            }
            // 身高相同的按姓名排序
            if(o1.getHeight() == o2.getHeight()){
                return o1.getName().compareTo(o2.getName());
            }

            if(temp > 0){
                return 1;
            }
            else if(temp < 0){
                return -1;
            }
            else{
                return 0;
            }

        });

        // 输出
        for(int i = 0; i < arr.length; i++){
            System.out.println(arr[i].getName() + " " + arr[i].getAge() + " " + arr[i].getHeight());
        }

    }
}
