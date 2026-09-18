package com.mystatic.a02;

public class ArrayUtil {
    // 工具类小练习
    /* 按照要求编写一个数组工具类 ArrayUtil
         提供一个工具类方法printArr 用于返回整数数组内容
         提供一个工具方法getAerage 用于返回平均值
         定义一个测试类TestDemo调用该工具类方法 返回结果
    */


    // 属性      私有化构造方法 创建一个工具类
    private ArrayUtil(){

    }

    // 方法1 (拼接字符串)     定义为静态 方便调用
    public static String printArr(int[] arr){
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for(int i = 0; i < arr.length; i++){
            if(i == arr.length - 1){
                sb.append(arr[i]);
            }
            else{
                sb.append(arr[i]).append(", ");
            }
        }
        sb.append("]");

        // 执行完结果使StringBuilder 变回字符串
        return sb.toString();
    }

    // 方法2 (求平均值)
    public static double getAverage(int[] arr){
        // 定义一个变量 用于存储总和
        int sum = 0;
        for(int i = 0; i < arr.length; i++){
            sum += arr[i];
        }
        // 求平均值
        return (double) sum / arr.length;
    }

}
