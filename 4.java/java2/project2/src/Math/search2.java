package Math;

import java.util.ArrayList;

public class search2 {
    public static void main(String[] args) {
        /* 查找算法
            1.基本查找 顺序查找
            2.二分查找 折半查找
            3.分块查找
            4.插值查找
            5.斐波那契查找
            6.树表查找
            7.哈希查找
         */



        // 1.基本查找 顺序查找
        // 从0索引开始依次查找
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int key = 11;
        boolean b = sequentialSearch(arr, key);
        System.out.println(b);

        // 考虑重复元素 输出每个索引
        ArrayList<Integer> list = sequentialSearch2(arr, key);
        System.out.println(list);



        // 2.二分查找 折半查找
        /* 数据必须有序
            1.min max必须在查找范围之内
            2.mid在min和max中间
            3.如果要查找的元素在mid左边 min不变 max=mid-1
            4.如果要查找的元素在mid右边 max不变 min=mid+1
            5.如果要查找的元素在mid位置 直接返回mid
         */
        int[] arr2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        System.out.println(binarySearch(arr2, 6));



        // 3.插值查找 二分查找改进
        // mid = min + (key-arr[min]) / (arr[max] - arr[min]) * (max-min)



        // 4.斐波那契查找
        // mid = min + F(k-1) - 1   F(k) = F(k-1) + F(k-2)



        // 5.分块查找 fenKuai2

    }


    // 1.顺序查找
    public static boolean sequentialSearch(int[] arr, int key) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == key) {
                return true;
            }
        }
        return false;
    }

    // 1.顺序查找 考虑重复元素 输出每个索引
    public static ArrayList<Integer> sequentialSearch2(int[] arr, int key) {
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == key) {
                list.add(i);
            }
        }
        return list;
    }



    // 2.二分查找 折半查找
    public static int binarySearch(int[] arr, int key) {
        int min = 0;
        int max = arr.length - 1;
        int mid = (min + max) / 2;

        while (true) {

            if (arr[mid] == key) {
                return mid;
            }

            if (key < arr[mid]) {
                max = mid - 1;
            }
            else if (key > arr[mid]) {
                min = mid + 1;
            }
            else{
                return mid;
            }
        }
    }

}
