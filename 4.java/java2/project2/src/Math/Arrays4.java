package Math;

import java.util.Arrays;
import java.util.Comparator;

public class Arrays4 {
    public static void main(String[] args) {
        // Arrays 操作数组的工具类 也是一个API

        /* 常见方法
            toString 数组转字符串
            sort 排序
            copyOf 复制
            copyOfRange 复制范围
            fill 填充
            binarySearch 二分查找

         */
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};

        // 1.toString
        System.out.println(Arrays.toString(arr));

        // 2.二分查找 前提有序且必须升序
        // 如果查找元素不存在 返回值为(负插入点减一 -key-1)
        int index = Arrays.binarySearch(arr, 5);
        System.out.println(index);

        // 3.拷贝
        int[] arr2 = Arrays.copyOf(arr, 5);
        System.out.println(Arrays.toString(arr2));

        // 4.拷贝带范围 包头不包尾 包左不包右
        // from旧数组长度 to新数组长度
        // 如果to大于旧数组长度 用0填充
        // 如果to小于旧数组长度 截取到to位置 部份拷贝
        int[] arr3 = Arrays.copyOfRange(arr, 2, 5);
        System.out.println(Arrays.toString(arr3));

        // 5.填充
        Arrays.fill(arr, 1, 3, 100);
        System.out.println(Arrays.toString(arr));

        // 6.排序 快速排序 升序
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));



        // 排序 不想实现升序 重载方法 (插入排序+二分查找)
        // 只能使用引用类型 如果是基本类型 使用其包装类
        Integer[] arr4 = {26, 45, 61, 52, 38, 95, 81};
        Arrays.sort(arr4, new Comparator<Integer>() {
            // 第二个参数是接口 需要传递接口实现类 使用匿名内部类
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1 - o2;
                // o1-o2升序  o2-o1降序
                // 返回值 负数 表示插入数小 放前面
                // 正数 表示插入数大 放后面 0表示相等
            }
        });

        System.out.println(Arrays.toString(arr4));














    }
}
