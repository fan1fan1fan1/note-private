package Generics4;

import java.util.Arrays;

public class MyArrayList1<E> {
    /* 泛型类
        当一个类中 某个变量的数据类型不确定时 可以定义泛型类

        类名 + <标志符>
        其中E表示一共不确定的类型
        在测试类中创建对象时就可以指定这个类型E
        此处E可以理解为变量 但不是用来记录数据的 而是记录数据的类型
        标志不唯一
     */

    Object[] obj = new Object[10];
    int size;

    public boolean add(E e){
        // 使用了一个不确定的数据类型E E为类型 e为对象

        obj[size] = e;
        size++;
        return true;
    }

    public E get(int index){
        return (E)obj[index];
        // 此处有一个数据类型强转 类型E转换为返回值数据类型
    }

    @Override
    public String toString(){
        // 重写继承了Object方法 将结果以字符串形式输出
        return Arrays.toString(obj);
    }

}
