package Math;

public class sort3 {
    public static void main(String[] args) {
        /* 排序算法
            1.冒泡排序
            2.选择排序
            3.插入排序
            4.快速排序

            5.希尔排序
            6.归并排序
            7.基数排序
            8.堆排序
            9.桶排序
            10.计数排序
         */
        int[] arr = {26, 45, 61, 52, 38, 95, 81};



        /* 1.冒泡排序
            1.相邻数据两两比较 小的放前面 大的放后面
            2.一轮循环结束 最大值在所有数据的最右侧
            3.第二轮在上一轮的所有最大值中继续比较
            4.如果数组中一共有n个数据 那么循环一共执行n-1次
         */
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - 1 - i; j++) {
                // -1防止索引越界   -i提高效率 也可以不要
                if(arr[i] > arr[i+1]){
                    int temp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = temp;
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }



        /* 2.选择排序
            1.从0索引开始 拿着每一个元素与后面的元素比较 小的放前面 大的放后面
            2.第一轮结束后 最小的元素就确定
            3.第二轮循环开始从索引1得到最小值 以此类推
         */
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = i+1; j < arr.length; j++) {
                if(arr[i] > arr[j]){
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }



        /* 3.插入排序
            1.认为左边部分(0,n)数据有序 右边部分(n+1,末尾)数据无序 然后根据左边顺序调整右边
            2.遍历得到右边无序的每张牌 插在有序数据里面
            3.遍历其他数据 插入进左边(插入方法 先跟左边最后一个数据比较 若小就跟前一个比)
            4.n的范围 0-最大索引
         */

        // 1.找到有序和无序两组 也就是无序开始的索引
        int startIndex1 = -1;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] > arr[i+1]){ // 顺序开始无序了 从这个索引开始为无序开始
                startIndex1 = i + 1;
                break;
            }
        }

        // 2.遍历从startIndex开始到最后一个元素 一次得到无序的组中的每一个元素
        for (int i = startIndex1; i < arr.length; i++) {
            // 把遍历到的数据插入到左边有序的组中

            // 记录当前要插入数据的索引
            int j = i;

            while(j > 0 && arr[j] < arr[j-1]){  // 无序 需要插入
                int temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
                j--; // 为了得到当前j的正确位置
            }
            // 得到了j的正确位置后 执行for的下一个循环 判断无序组下一个元素
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }



        /* 4.快速排序
            1.递归算法
                递归一定要有出口 否则会有栈(内存)溢出
            2.把0索引作为基准数 确定基准数在数组中的正确位置
            3.比基准数小的全部在左边 比基准数大的全部在右边
            4.准备start索引和end索引 分别从头和尾寻找
                start找到比基准数大的 end找到比基准数小的 两个索引交换位置
                直到start和end指向了同一个位置 这就是基准数位置
         */

        int startIndex = 0;
        int endIndex = arr.length - 1;
        int baseNum = arr[startIndex];

        while(startIndex < endIndex){
            // 从右往左找 一定得先找end 后找start
            while(arr[endIndex] >= baseNum && startIndex < endIndex){
                endIndex--;
            }
            // 从左往右找
            while(arr[startIndex] <= baseNum && startIndex < endIndex){
                startIndex++;
            }
            // 交换
            int temp = arr[startIndex];
            arr[startIndex] = arr[endIndex];
            arr[endIndex] = temp;
        }
        // 当start和end指向了同一个元素的时候 循环就会结束
        // 基准数归位
        int temp = arr[startIndex];
        arr[startIndex] = arr[0];
        arr[0] = temp;

        // 递归调用 start和end
        quickSort(arr, 0, startIndex - 1);
        quickSort(arr, startIndex + 1, endIndex);



        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }


















    }

    // 递归求1-n的和
    public static int sum(int n){
        if(n == 1){  // 出口
            return 1;
        }

        return n + sum(n-1); // 递归
    }

    // 递归求阶乘
    public static int jie(int n){
        if(n == 1){
            return 1;
        }

        return n * (jie(n-1));
    }

    // 快速排序函数写法
    public static void quickSort(int[] arr, int startIndex, int endIndex) {
        int start = startIndex;
        int end = endIndex;
        int baseNum = arr[start];
        while (start < end) {
            // 从右往左找 一定得先找end 后找start
            while (arr[end] >= baseNum && start < end) {
                end--;
            }
            // 从左往右找
            while (arr[start] <= baseNum && start < end) {
                start++;
            }
            // 交换
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
        }
    }





}
