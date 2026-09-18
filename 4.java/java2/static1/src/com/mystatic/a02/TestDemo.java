package com.mystatic.a02;

public class TestDemo {
    public static void main(String[] args) {
        // 测试工具类
        int[] arr = {1, 2, 3, 4, 5};

        String result = ArrayUtil.printArr(arr);
        System.out.println(result);

        double average = ArrayUtil.getAverage(arr);
        System.out.println(average);

    }
}
