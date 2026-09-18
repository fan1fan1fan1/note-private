package Generics4;

public class test1 {
    public static void main(String[] args){
        // MyArrayList1<String> list = new MyArrayList1<String>();
        // 在测试类中指定可以指定数据类型 E    String

        MyArrayList1<Integer> list = new MyArrayList1<Integer>();
        list.add(123);
        list.add(456);
        list.add(789);

        int i = list.get(0);
        System.out.println(i);

        System.out.println(list);

    }
}
